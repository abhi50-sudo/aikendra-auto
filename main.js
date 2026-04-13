// AI Kendra — Main Router & App Bootstrap
import toolsData from './data/tools.json';
import ideasData from './data/ideas.json';
import { renderNavbar, initNavbar } from './components/navbar.js';
import { renderHome, initHome } from './pages/home.js';
import { renderTools, initTools } from './pages/tools.js';
import { renderToolsByCategory } from './pages/toolsByCategory.js';
import { renderToolDetail } from './pages/toolDetail.js';
import { renderIdeas, initIdeas } from './pages/ideas.js';
import { renderIdeaDetail } from './pages/ideaDetail.js';
import { renderSubmit, initSubmit } from './pages/submit.js';
import { renderAbout } from './pages/about.js';
import { renderContact, initContact } from './pages/contact.js';
import { renderPrivacy } from './pages/privacy.js';
import { renderTerms } from './pages/terms.js';

// Make data globally accessible
window.__AK_TOOLS = toolsData;
window.__AK_IDEAS = ideasData;

// --- Theme ---
function initTheme() {
  const saved = localStorage.getItem('ak-theme') || 'light';
  document.documentElement.setAttribute('data-theme', saved);
}

function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('ak-theme', next);
}

// --- Router ---
const routes = [
  { pattern: /^\/$/, render: renderHome, init: initHome },
  { pattern: /^\/ai-tools$/, render: renderTools, init: initTools },
  { pattern: /^\/ai-tools\/tool\/([^/]+)$/, render: renderToolDetail },
  { pattern: /^\/ai-tools\/([^/]+)$/, render: renderToolsByCategory },
  { pattern: /^\/startup-ideas$/, render: renderIdeas, init: initIdeas },
  { pattern: /^\/startup-ideas\/([^/]+)$/, render: renderIdeaDetail },
  { pattern: /^\/submit$/, render: renderSubmit, init: initSubmit },
  { pattern: /^\/about$/, render: renderAbout },
  { pattern: /^\/contact$/, render: renderContact, init: initContact },
  { pattern: /^\/privacy$/, render: renderPrivacy },
  { pattern: /^\/terms$/, render: renderTerms },
];

function getPath() {
  return window.location.pathname || '/';
}

function navigate(path) {
  window.history.pushState({}, '', path);
  render();
}

function render() {
  const path = getPath();
  const app = document.getElementById('app');

  let matched = false;
  for (const route of routes) {
    const match = path.match(route.pattern);
    if (match) {
      const params = match.slice(1);
      app.innerHTML = route.render(...params);
      if (route.init) route.init(...params);
      matched = true;
      break;
    }
  }

  if (!matched) {
    app.innerHTML = render404();
  }

  // Update active nav link
  updateActiveNav(path);
  // Scroll to top
  window.scrollTo(0, 0);
  // Update page title
  updateTitle(path);
}

function render404() {
  return `
    <div class="static-page">
      <div class="container" style="text-align:center; padding: 6rem 0;">
        <h1 style="font-size: var(--font-5xl); margin-bottom: var(--space-lg);">404</h1>
        <p style="font-size: var(--font-xl);">Page not found</p>
        <a href="/" class="btn btn-primary" style="margin-top: var(--space-xl);" data-link>Back to Home</a>
      </div>
    </div>
  `;
}

function updateActiveNav(path) {
  document.querySelectorAll('.nav-links a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === path || (path.startsWith('/ai-tools') && href === '/ai-tools') || (path.startsWith('/startup-ideas') && href === '/startup-ideas')) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });
}

function updateTitle(path) {
  const meta = {
    '/': { title: 'AI Kendra — Discover AI Tools & Startup Ideas', desc: 'AI Kendra is your central hub to discover the best AI tools and explore startup ideas powered by artificial intelligence.' },
    '/ai-tools': { title: 'AI Tools Directory — AI Kendra', desc: 'Browse and discover curated AI tools across writing, image generation, coding, marketing, and more categories.' },
    '/startup-ideas': { title: 'AI Startup Ideas — AI Kendra', desc: 'Explore curated AI-powered startup ideas with problem statements, solutions, revenue models, and implementation guides.' },
    '/submit': { title: 'Submit an AI Tool or Startup Idea — AI Kendra', desc: 'Submit an AI tool or startup idea to the AI Kendra directory and help the community discover great AI products.' },
    '/about': { title: 'About AI Kendra', desc: 'AI Kendra is a curated discovery platform for AI tools and startup ideas. Learn about our mission and values.' },
    '/contact': { title: 'Contact — AI Kendra', desc: 'Get in touch with the AI Kendra team for questions, suggestions, or partnership inquiries.' },
    '/privacy': { title: 'Privacy Policy — AI Kendra', desc: 'Read the AI Kendra privacy policy to understand how we collect, use, and protect your information.' },
    '/terms': { title: 'Terms of Service — AI Kendra', desc: 'Read the AI Kendra terms of service for using our AI tools and startup ideas directory.' },
  };

  let pageTitle = '';
  let pageDesc = '';

  if (meta[path]) {
    pageTitle = meta[path].title;
    pageDesc = meta[path].desc;
  } else if (path.startsWith('/ai-tools/tool/')) {
    const slug = path.split('/').pop();
    const tool = toolsData.find(t => t.slug === slug);
    pageTitle = tool ? `${tool.name} — AI Kendra` : 'AI Tool — AI Kendra';
    pageDesc = tool ? tool.shortDescription : 'Discover this AI tool on AI Kendra.';
  } else if (path.startsWith('/ai-tools/')) {
    const cat = path.split('/').pop();
    const catName = cat.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
    pageTitle = `${catName} AI Tools — AI Kendra`;
    pageDesc = `Browse the best ${catName} AI tools curated in the AI Kendra directory.`;
  } else if (path.startsWith('/startup-ideas/')) {
    const slug = path.split('/').pop();
    const idea = ideasData.find(i => i.slug === slug);
    pageTitle = idea ? `${idea.title} — AI Kendra` : 'Startup Idea — AI Kendra';
    pageDesc = idea ? idea.summary : 'Explore this AI startup idea on AI Kendra.';
  }

  if (pageTitle) document.title = pageTitle;
  if (pageDesc) {
    const descTag = document.querySelector('meta[name="description"]');
    if (descTag) descTag.setAttribute('content', pageDesc);
    const ogDesc = document.querySelector('meta[property="og:description"]');
    if (ogDesc) ogDesc.setAttribute('content', pageDesc);
    const ogTitle = document.querySelector('meta[property="og:title"]');
    if (ogTitle) ogTitle.setAttribute('content', pageTitle);
  }
}

// --- Global Search ---
function initGlobalSearch() {
  const toggle = document.getElementById('searchToggle');
  const overlay = document.getElementById('searchOverlay');
  const input = document.getElementById('globalSearch');
  const results = document.getElementById('globalSearchResults');
  const close = document.getElementById('searchClose');

  toggle.addEventListener('click', () => {
    overlay.classList.toggle('active');
    if (overlay.classList.contains('active')) {
      input.focus();
      input.value = '';
      results.innerHTML = '';
    }
  });

  close.addEventListener('click', () => {
    overlay.classList.remove('active');
  });

  input.addEventListener('input', () => {
    const q = input.value.toLowerCase().trim();
    if (!q) { results.innerHTML = ''; return; }

    const toolResults = toolsData.filter(t =>
      t.name.toLowerCase().includes(q) || t.shortDescription.toLowerCase().includes(q) || t.category.toLowerCase().includes(q)
    ).slice(0, 4);

    const ideaResults = ideasData.filter(i =>
      i.title.toLowerCase().includes(q) || i.summary.toLowerCase().includes(q) || i.category.toLowerCase().includes(q)
    ).slice(0, 3);

    let html = '';
    if (toolResults.length) {
      toolResults.forEach(t => {
        html += `<a href="/ai-tools/tool/${t.slug}" class="search-result-item" data-link>
          <span class="result-icon" ${t.logo && t.logo.includes('http') ? 'style="padding:0;background:transparent;overflow:hidden;"' : ''}>
            ${t.logo && t.logo.includes('http') ? `<img src="${t.logo.trim()}" alt="" onerror="this.parentElement.innerHTML='🤖'; this.parentElement.style='';" style="width:100%;height:100%;object-fit:cover;border-radius:var(--radius-sm);">` : (t.logo || '🤖')}
          </span>
          <div class="result-info"><h4>${t.name}</h4><p>${t.shortDescription.substring(0, 80)}...</p></div>
        </a>`;
      });
    }
    if (ideaResults.length) {
      ideaResults.forEach(i => {
        html += `<a href="/startup-ideas/${i.slug}" class="search-result-item" data-link>
          <span class="result-icon">💡</span>
          <div class="result-info"><h4>${i.title}</h4><p>${i.summary.substring(0, 80)}...</p></div>
        </a>`;
      });
    }
    if (!toolResults.length && !ideaResults.length) {
      html = '<p style="text-align:center;color:var(--text-tertiary);padding:var(--space-lg);">No results found</p>';
    }
    results.innerHTML = html;

    // Bind search result links
    results.querySelectorAll('[data-link]').forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        overlay.classList.remove('active');
        navigate(link.getAttribute('href'));
      });
    });
  });

  // Close on Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') overlay.classList.remove('active');
  });
}

// --- Link Interceptor ---
function interceptLinks() {
  document.addEventListener('click', (e) => {
    const link = e.target.closest('[data-link]');
    if (link) {
      e.preventDefault();
      const href = link.getAttribute('href');
      if (href && href !== getPath()) {
        navigate(href);
      }
      // Close mobile nav
      document.getElementById('navLinks')?.classList.remove('open');
      document.getElementById('hamburger')?.classList.remove('active');
    }
  });
}

// --- Init ---
function init() {
  initTheme();
  initNavbar(toggleTheme);
  initGlobalSearch();
  interceptLinks();
  render();

  // Handle browser back/forward
  window.addEventListener('popstate', render);
}

// Remove Vite default files
const counterEl = document.getElementById('counter');
if (counterEl) counterEl.remove();

document.addEventListener('DOMContentLoaded', init);
