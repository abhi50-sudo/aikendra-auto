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

  // --- SITEMAP.XML ---
  const SITE_URL = 'https://aikendra.com';
  const today = new Date().toISOString().split('T')[0];
  
  let urls = [];
  
  // Core pages
  const corePages = [
    { loc: '/', changefreq: 'daily', priority: '1.0' },
    { loc: '/ai-tools', changefreq: 'daily', priority: '0.9' },
    { loc: '/startup-ideas', changefreq: 'weekly', priority: '0.8' },
    { loc: '/submit', changefreq: 'monthly', priority: '0.5' },
    { loc: '/about', changefreq: 'monthly', priority: '0.4' },
    { loc: '/contact', changefreq: 'monthly', priority: '0.3' },
    { loc: '/privacy', changefreq: 'monthly', priority: '0.2' },
    { loc: '/terms', changefreq: 'monthly', priority: '0.2' },
  ];
  corePages.forEach(p => urls.push(p));
  
  // Tool pages
  tools.forEach(tool => {
    if (!tool.slug) return;
    urls.push({ loc: `/ai-tools/tool/${tool.slug}`, changefreq: 'weekly', priority: '0.7' });
  });
  
  // Idea pages
  ideas.forEach(idea => {
    if (!idea.slug) return;
    urls.push({ loc: `/startup-ideas/${idea.slug}`, changefreq: 'weekly', priority: '0.6' });
  });
  
  // Category pages
  categories.forEach(cat => {
    const slug = cat.toLowerCase().replace(/ & /g, '-').replace(/ /g, '-');
    urls.push({ loc: `/ai-tools/${slug}`, changefreq: 'weekly', priority: '0.6' });
  });
  
  const sitemapXml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map(u => `  <url>
    <loc>${SITE_URL}${u.loc}</loc>
    <lastmod>${today}</lastmod>
    <changefreq>${u.changefreq}</changefreq>
    <priority>${u.priority}</priority>
  </url>`).join('\n')}
</urlset>`;
  
  fs.writeFileSync(path.join(DIST_DIR, 'sitemap.xml'), sitemapXml);
  console.log(`Generated sitemap.xml with ${urls.length} URLs.`);
  
  // robots.txt
  const robotsTxt = `User-agent: *
Allow: /

Sitemap: ${SITE_URL}/sitemap.xml`;
  fs.writeFileSync(path.join(DIST_DIR, 'robots.txt'), robotsTxt);
  console.log('Generated robots.txt.');

  console.log('Static Site Generation complete!');
}

generateStaticPages();
