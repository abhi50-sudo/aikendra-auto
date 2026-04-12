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

  console.log('Static Site Generation complete!');
}

generateStaticPages();
