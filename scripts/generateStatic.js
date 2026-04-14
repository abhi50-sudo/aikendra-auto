import fs from 'fs';
import path from 'path';

// This script runs AFTER `vite build`.
// It reads the compiled `dist/index.html` and generates a physical folder/file 
// for every tool and startup idea, modifying the <title> and <meta> tags for SEO.

const DIST_DIR = path.join(process.cwd(), 'dist');
const INDEX_PATH = path.join(DIST_DIR, 'index.html');

function generateStaticPages() {
  console.log('Starting Static Site Generation for SEO...');
  
  if (!fs.existsSync(INDEX_PATH)) {
    console.error('dist/index.html not found. Did vite build run?');
    process.exit(1);
  }

  const baseHtml = fs.readFileSync(INDEX_PATH, 'utf-8');
  
  const toolsPath = path.join(process.cwd(), 'data', 'tools.json');
  const ideasPath = path.join(process.cwd(), 'data', 'ideas.json');
  
  const tools = JSON.parse(fs.readFileSync(toolsPath, 'utf-8'));
  const ideas = JSON.parse(fs.readFileSync(ideasPath, 'utf-8'));

  // Utility to replace SEO tags
  const injectSEO = (html, title, description) => {
    let newHtml = html.replace(/<title>.*?<\/title>/, `<title>${title}<\/title>`);
    newHtml = newHtml.replace(/<meta name="description" content=".*?">/, `<meta name="description" content="${description}">`);
    newHtml = newHtml.replace(/<meta property="og:title" content=".*?">/, `<meta property="og:title" content="${title}">`);
    newHtml = newHtml.replace(/<meta property="og:description" content=".*?">/, `<meta property="og:description" content="${description}">`);
    return newHtml;
  };

  // Generate Tool Pages
  tools.forEach(tool => {
    if (!tool.slug) return;
    const title = `${tool.name} — AI Kendra Directory`;
    const desc = tool.shortDescription;
    const pageHtml = injectSEO(baseHtml, title, desc);
    
    const dir = path.join(DIST_DIR, 'ai-tools', 'tool', tool.slug);
    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(path.join(dir, 'index.html'), pageHtml);
  });
  console.log(`Generated ${tools.length} tool SEO pages.`);

  // Generate Idea Pages
  ideas.forEach(idea => {
    if (!idea.slug) return;
    const title = `${idea.title} — AI Kendra Startup Ideas`;
    const desc = idea.summary;
    const pageHtml = injectSEO(baseHtml, title, desc);
    
    const dir = path.join(DIST_DIR, 'startup-ideas', idea.slug);
    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(path.join(dir, 'index.html'), pageHtml);
  });
  console.log(`Generated ${ideas.length} idea SEO pages.`);
  
  // Generate basic categories (AI Tools directory)
  const categories = [...new Set(tools.map(t => t.category))].filter(Boolean);
  categories.forEach(cat => {
    const slug = cat.toLowerCase().replace(/ & /g, '-').replace(/ /g, '-');
    const title = `${cat} AI Tools — AI Kendra`;
    const desc = `Browse the best ${cat} AI tools curated in the AI Kendra directory.`;
    const pageHtml = injectSEO(baseHtml, title, desc);
    
    const dir = path.join(DIST_DIR, 'ai-tools', slug);
    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(path.join(dir, 'index.html'), pageHtml);
  });
  console.log(`Generated ${categories.length} category SEO pages.`);

  // --- SITEMAP INDEX SYSTEM ---
  const SITE_URL = 'https://aikendra.com';
  const today = new Date().toISOString().split('T')[0];
  const TOOLS_PER_SITEMAP = 500;

  function buildUrlset(urls) {
    return `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map(u => `  <url>
    <loc>${SITE_URL}${u.loc}</loc>
    <lastmod>${today}</lastmod>
    <changefreq>${u.changefreq}</changefreq>
  </url>`).join('\n')}
</urlset>`;
  }

  // 1. sitemap-pages.xml — Core static pages
  const pageUrls = [
    { loc: '/', changefreq: 'daily' },
    { loc: '/ai-tools', changefreq: 'daily' },
    { loc: '/startup-ideas', changefreq: 'weekly' },
    { loc: '/submit', changefreq: 'monthly' },
    { loc: '/about', changefreq: 'monthly' },
    { loc: '/contact', changefreq: 'monthly' },
    { loc: '/privacy', changefreq: 'monthly' },
    { loc: '/terms', changefreq: 'monthly' },
  ];
  fs.writeFileSync(path.join(DIST_DIR, 'sitemap-pages.xml'), buildUrlset(pageUrls));
  console.log(`Generated sitemap-pages.xml (${pageUrls.length} URLs).`);

  // 2. sitemap-categories.xml — Category pages
  const categoryUrls = categories.map(cat => {
    const slug = cat.toLowerCase().replace(/ & /g, '-').replace(/ /g, '-');
    return { loc: `/ai-tools/${slug}`, changefreq: 'weekly' };
  });
  fs.writeFileSync(path.join(DIST_DIR, 'sitemap-categories.xml'), buildUrlset(categoryUrls));
  console.log(`Generated sitemap-categories.xml (${categoryUrls.length} URLs).`);

  // 3. sitemap-ideas.xml — Startup idea pages
  const ideaUrls = ideas.filter(i => i.slug).map(idea => ({
    loc: `/startup-ideas/${idea.slug}`, changefreq: 'weekly'
  }));
  fs.writeFileSync(path.join(DIST_DIR, 'sitemap-ideas.xml'), buildUrlset(ideaUrls));
  console.log(`Generated sitemap-ideas.xml (${ideaUrls.length} URLs).`);

  // 4. sitemap-tools-N.xml — Tool pages, split into chunks of 500
  const toolUrls = tools.filter(t => t.slug).map(t => ({
    loc: `/ai-tools/tool/${t.slug}`, changefreq: 'weekly'
  }));
  const toolSitemapFiles = [];
  for (let i = 0; i < toolUrls.length; i += TOOLS_PER_SITEMAP) {
    const chunk = toolUrls.slice(i, i + TOOLS_PER_SITEMAP);
    const fileNum = Math.floor(i / TOOLS_PER_SITEMAP) + 1;
    const filename = `sitemap-tools-${fileNum}.xml`;
    fs.writeFileSync(path.join(DIST_DIR, filename), buildUrlset(chunk));
    toolSitemapFiles.push(filename);
    console.log(`Generated ${filename} (${chunk.length} URLs).`);
  }

  // 5. sitemap_index.xml — Master index
  const allSitemaps = [
    'sitemap-pages.xml',
    'sitemap-categories.xml',
    'sitemap-ideas.xml',
    ...toolSitemapFiles
  ];
  const sitemapIndex = `<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${allSitemaps.map(f => `  <sitemap>
    <loc>${SITE_URL}/${f}</loc>
    <lastmod>${today}</lastmod>
  </sitemap>`).join('\n')}
</sitemapindex>`;

  fs.writeFileSync(path.join(DIST_DIR, 'sitemap_index.xml'), sitemapIndex);
  console.log(`Generated sitemap_index.xml (${allSitemaps.length} sub-sitemaps).`);

  // Keep old sitemap.xml as a combined fallback (Google may still request it)
  const allUrls = [...pageUrls, ...categoryUrls, ...ideaUrls, ...toolUrls];
  fs.writeFileSync(path.join(DIST_DIR, 'sitemap.xml'), buildUrlset(allUrls));
  console.log(`Generated sitemap.xml fallback (${allUrls.length} URLs).`);

  const totalUrls = pageUrls.length + categoryUrls.length + ideaUrls.length + toolUrls.length;
  console.log(`Total indexed URLs: ${totalUrls}`);

  // robots.txt — points to sitemap index
  const robotsTxt = `User-agent: *
Allow: /

Sitemap: ${SITE_URL}/sitemap_index.xml
Sitemap: ${SITE_URL}/sitemap.xml`;
  fs.writeFileSync(path.join(DIST_DIR, 'robots.txt'), robotsTxt);
  console.log('Generated robots.txt.');

  console.log('Static Site Generation complete!');
}

generateStaticPages();
