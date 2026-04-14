// Homepage — Directory-First Layout with Full SEO Optimization
import { toolCard, ideaCard } from '../components/card.js';

const categories = [
  { slug: 'all', name: 'All', icon: '📁' },
  { slug: 'writing', name: 'Writing', icon: '✍️' },
  { slug: 'image-generation', name: 'Image Gen', icon: '🎨' },
  { slug: 'video-creation', name: 'Video', icon: '🎬' },
  { slug: 'audio-voice', name: 'Audio', icon: '🎙️' },
  { slug: 'coding-development', name: 'Coding', icon: '💻' },
  { slug: 'productivity', name: 'Productivity', icon: '📋' },
  { slug: 'marketing', name: 'Marketing', icon: '📢' },
  { slug: 'finance', name: 'Finance', icon: '🛡️' },
  { slug: 'automation', name: 'Automation', icon: '⚡' },
  { slug: 'research', name: 'Research', icon: '🔬' },
];

function getCategorySlug(categoryName) {
  return categoryName.toLowerCase().replace(/ & /g, '-').replace(/ /g, '-');
}

function formatDate(dateStr) {
  const d = new Date(dateStr);
  const now = new Date();
  const diff = now - d;
  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  if (days === 0) return 'Today';
  if (days === 1) return 'Yesterday';
  if (days < 7) return `${days}d ago`;
  if (days < 30) return `${Math.floor(days/7)}w ago`;
  return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
}

function toolRow(t) {
  return `
    <a href="/ai-tools/tool/${t.slug}" class="tool-grid-card" data-link data-category="${getCategorySlug(t.category)}">
      <div class="tool-grid-card-top">
        <span class="tool-grid-logo" ${t.logo && t.logo.includes('http') ? `style="padding:0;background:transparent;overflow:hidden;"` : ''}>
          ${t.logo && t.logo.includes('http') ? `<img src="${t.logo.trim()}" alt="${t.name} logo - ${t.category} AI Tool" onerror="this.parentElement.innerHTML='🤖'; this.parentElement.style='';" style="width:100%;height:100%;object-fit:cover;border-radius:var(--radius-md);">` : (t.logo || '🤖')}
        </span>
        <div class="tool-grid-title-wrap">
          <h3>${t.name}</h3>
        </div>
        <span class="tool-grid-pricing">${t.pricing || 'Free'}</span>
      </div>
      <p class="tool-grid-desc">${t.shortDescription}</p>
      <div class="tool-grid-footer">
        <span class="tool-grid-cat">${t.category}</span>
        <span class="tool-grid-date">${formatDate(t.dateAdded)}</span>
      </div>
    </a>
  `;
}

function ideaRow(i) {
  const diffClass = i.difficulty === 'Beginner' ? 'beginner' : i.difficulty === 'Intermediate' ? 'intermediate' : 'advanced';
  return `
    <a href="/startup-ideas/${i.slug}" class="tool-grid-card idea-card" data-link>
      <div class="tool-grid-card-top">
        <span class="tool-grid-logo">💡</span>
        <div class="tool-grid-title-wrap">
          <h3>${i.title}</h3>
        </div>
        <span class="badge badge-${diffClass}">${i.difficulty}</span>
      </div>
      <p class="tool-grid-desc">${i.summary}</p>
      <div class="tool-grid-footer">
        <span class="tool-grid-cat">${i.category}</span>
      </div>
    </a>
  `;
}

function getCategoryStats(tools) {
  const stats = {};
  tools.forEach(t => {
    stats[t.category] = (stats[t.category] || 0) + 1;
  });
  return stats;
}

function getPricingStats(tools) {
  const stats = { Free: 0, Freemium: 0, Paid: 0, 'Open Source': 0, Other: 0 };
  tools.forEach(t => {
    const p = t.pricing || 'Free';
    if (stats[p] !== undefined) stats[p]++;
    else stats.Other++;
  });
  return stats;
}

export function renderHome() {
  const tools = window.__AK_TOOLS;
  const ideas = window.__AK_IDEAS;

  const featuredTools = tools.filter(t => t.featured);
  const newestTools = [...tools].sort((a, b) => new Date(b.dateAdded) - new Date(a.dateAdded));
  const allTools = [...tools].sort((a, b) => a.name.localeCompare(b.name));
  const catStats = getCategoryStats(tools);
  const priceStats = getPricingStats(tools);

  return `
    <!-- Compact Hero with Definition Pattern & Stats -->
    <section class="dir-hero">
      <div class="container">
        <h1>Discover AI Tools & Startup Ideas</h1>
        <p class="dir-hero-intro">AI Kendra is the most comprehensive directory of artificial intelligence tools, featuring <strong>${tools.length}+ curated AI tools</strong> across <strong>${categories.length - 1} categories</strong> — updated daily with the latest AI products from around the world. Whether you're a developer, marketer, researcher, or entrepreneur, find the perfect AI tool for your workflow.</p>
        <p class="dir-hero-stats">${tools.length} AI Tools · ${ideas.length} Startup Ideas · ${categories.length - 1} Categories · Updated Daily</p>
        <div class="dir-search-wrap">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
          <input type="text" id="dirSearch" placeholder="Search AI tools, startup ideas..." autocomplete="off" />
        </div>
      </div>
    </section>

    <!-- Statistics Section -->
    <section class="dir-stats-bar">
      <div class="container">
        <h2>AI Tools Directory at a Glance</h2>
        <div class="stats-grid">
          <div class="stat-item"><span class="stat-number">${tools.length}+</span><span class="stat-label">AI Tools Listed</span></div>
          <div class="stat-item"><span class="stat-number">${categories.length - 1}</span><span class="stat-label">Categories</span></div>
          <div class="stat-item"><span class="stat-number">${priceStats.Free + priceStats.Freemium + priceStats['Open Source']}</span><span class="stat-label">Free or Freemium</span></div>
          <div class="stat-item"><span class="stat-number">${ideas.length}</span><span class="stat-label">Startup Ideas</span></div>
        </div>
      </div>
    </section>

    <!-- Category Breakdown Table -->
    <section class="dir-table-section">
      <div class="container">
        <h2>How many AI tools are in each category?</h2>
        <p>AI Kendra organizes tools into ${categories.length - 1} major categories. According to our latest data, here is the breakdown of tools per category:</p>
        <div class="table-responsive">
          <table class="seo-table">
            <thead>
              <tr><th>Category</th><th>Tools Available</th><th>Pricing Range</th><th>Top Example</th></tr>
            </thead>
            <tbody>
              ${categories.filter(c => c.slug !== 'all').map(c => {
                const catName = c.slug.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase()).replace('And', '&');
                const count = Object.entries(catStats).find(([k]) => getCategorySlug(k) === c.slug)?.[1] || 0;
                const topTool = tools.find(t => getCategorySlug(t.category) === c.slug);
                return `<tr>
                  <td>${c.icon} <a href="/ai-tools/${c.slug}" data-link>${c.name}</a></td>
                  <td>${count} tools</td>
                  <td>Free–Paid</td>
                  <td>${topTool ? topTool.name : '—'}</td>
                </tr>`;
              }).join('')}
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- Context Toggle -->
    <section class="dir-context-switch">
      <div class="container">
        <div class="dir-toggle-group" id="contextToggle">
          <button class="dir-toggle-btn active" data-context="tools">🤖 AI Tools</button>
          <button class="dir-toggle-btn" data-context="ideas">💡 Startup Ideas</button>
        </div>
      </div>
    </section>

    <!-- Tab Navigation + Category Pills -->
    <section class="dir-tabs-section" id="tabsSection">
      <div class="container">
        <div class="dir-tabs" id="dirTabs">
          <button class="dir-tab active" data-tab="trending">🔥 Trending</button>
          <button class="dir-tab" data-tab="new">🆕 Just Launched</button>
          <button class="dir-tab" data-tab="all">📁 All Tools</button>
        </div>
        <div class="dir-category-pills" id="categoryPills">
          ${categories.map(c => `
            <button class="cat-pill ${c.slug === 'all' ? 'active' : ''}" data-cat="${c.slug}">${c.icon} ${c.name}</button>
          `).join('')}
        </div>
      </div>
    </section>

    <!-- Feed -->
    <section class="dir-feed">
      <div class="container">
        <h2 class="sr-only">Browse AI Tools</h2>
        <div class="dir-feed-list" id="dirFeed">
          ${featuredTools.map(t => toolRow(t)).join('')}
        </div>
        <div class="dir-feed-empty" id="dirFeedEmpty" style="display:none;">
          <p>No results found. Try a different search or category.</p>
        </div>
      </div>
    </section>

    <!-- FAQ Section with Q&A Headings -->
    <section class="dir-faq" id="faqSection">
      <div class="container">
        <h2>Frequently Asked Questions About AI Tools</h2>
        <div class="faq-list">
          <details class="faq-item" open>
            <summary><h3>What is AI Kendra?</h3></summary>
            <p>AI Kendra is a comprehensive, curated directory of ${tools.length}+ artificial intelligence tools and ${ideas.length} startup ideas. It is designed to help developers, marketers, researchers, entrepreneurs, and everyday users discover the best AI-powered products across ${categories.length - 1} categories — from <a href="/ai-tools/writing" data-link>AI writing assistants</a> and <a href="/ai-tools/image-generation" data-link>image generators</a> to <a href="/ai-tools/coding-development" data-link>coding tools</a> and <a href="/ai-tools/automation" data-link>automation platforms</a>. All tools are updated daily.</p>
          </details>
          <details class="faq-item">
            <summary><h3>How does AI Kendra find and verify AI tools?</h3></summary>
            <p>AI Kendra uses a dual-source approach: a curated backlog of verified, high-quality AI tools reviewed by our team, combined with automated discovery from <a href="https://github.com/trending" target="_blank" rel="noopener">GitHub trending repositories</a>. Each tool is categorized, tagged, and verified before being added to the directory. According to <a href="https://explodingtopics.com/blog/ai-tools" target="_blank" rel="noopener">Exploding Topics</a>, over 14,700 AI tools were launched in 2025 alone — making curation essential.</p>
          </details>
          <details class="faq-item">
            <summary><h3>What are the most popular categories of AI tools in 2026?</h3></summary>
            <p>Based on our directory data, the top categories by tool count are: <strong>Image Generation (${catStats['Image Generation'] || 0}+ tools)</strong>, <strong>Productivity (${catStats['Productivity'] || 0}+ tools)</strong>, <strong>Marketing (${catStats['Marketing'] || 0}+ tools)</strong>, and <strong>Writing (${catStats['Writing'] || 0}+ tools)</strong>. The AI coding category is growing fastest, driven by tools like <a href="https://github.com/features/copilot" target="_blank" rel="noopener">GitHub Copilot</a>, <a href="https://cursor.com" target="_blank" rel="noopener">Cursor</a>, and <a href="https://bolt.new" target="_blank" rel="noopener">Bolt.new</a>.</p>
          </details>
          <details class="faq-item">
            <summary><h3>Are the AI tools on AI Kendra free to use?</h3></summary>
            <p>Many are! Of the ${tools.length} tools listed, <strong>${priceStats.Free} are completely free</strong>, <strong>${priceStats.Freemium} offer freemium plans</strong>, and <strong>${priceStats['Open Source']} are open source</strong>. The remaining ${priceStats.Paid} are paid tools. You can filter tools by pricing using the category and tab filters above.</p>
          </details>
          <details class="faq-item">
            <summary><h3>How can I submit my own AI tool to AI Kendra?</h3></summary>
            <p>You can <a href="/submit" data-link>submit your AI tool here</a>. Provide the tool name, website URL, category, pricing, and a brief description. Our team reviews every submission before it goes live. Typically, approved tools appear within 24–48 hours.</p>
          </details>
        </div>
      </div>
    </section>

    <!-- Minimal CTA with Author Attribution -->
    <section class="dir-cta">
      <div class="container">
        <p>Know an AI tool? <a href="/submit" data-link>Submit it →</a></p>
        <p class="dir-cta-author">Curated by the <a href="/about" data-link>AI Kendra team</a> · Data sourced from <a href="https://github.com/trending" target="_blank" rel="noopener">GitHub</a>, <a href="https://producthunt.com" target="_blank" rel="noopener">Product Hunt</a>, and community submissions.</p>
      </div>
    </section>
  `;
}

export function initHome() {
  const tools = window.__AK_TOOLS;
  const ideas = window.__AK_IDEAS;

  const featuredTools = tools.filter(t => t.featured);
  const newestTools = [...tools].sort((a, b) => new Date(b.dateAdded) - new Date(a.dateAdded));
  const allToolsSorted = [...tools].sort((a, b) => a.name.localeCompare(b.name));

  let currentContext = 'tools'; // 'tools' or 'ideas'
  let currentTab = 'trending';
  let currentCat = 'all';
  let searchQuery = '';

  const feedEl = document.getElementById('dirFeed');
  const emptyEl = document.getElementById('dirFeedEmpty');
  const pillsContainer = document.getElementById('categoryPills');
  const tabsSection = document.getElementById('tabsSection');

  function getToolsForTab(tab) {
    if (tab === 'trending') return featuredTools;
    if (tab === 'new') return newestTools;
    if (tab === 'all') return allToolsSorted;
    return [];
  }

  function renderFeed() {
    if (currentContext === 'ideas') {
      // Show ideas
      tabsSection.style.display = 'none';
      let filtered = ideas;
      if (searchQuery) {
        filtered = ideas.filter(i =>
          i.title.toLowerCase().includes(searchQuery) ||
          i.summary.toLowerCase().includes(searchQuery) ||
          i.category.toLowerCase().includes(searchQuery)
        );
      }
      feedEl.innerHTML = filtered.map(i => ideaRow(i)).join('');
      emptyEl.style.display = filtered.length ? 'none' : 'block';
    } else {
      // Show tools
      tabsSection.style.display = '';
      let filtered = getToolsForTab(currentTab);
      if (currentCat !== 'all') {
        filtered = filtered.filter(t => getCategorySlug(t.category) === currentCat);
      }
      if (searchQuery) {
        filtered = filtered.filter(t =>
          t.name.toLowerCase().includes(searchQuery) ||
          t.shortDescription.toLowerCase().includes(searchQuery) ||
          t.category.toLowerCase().includes(searchQuery)
        );
      }
      feedEl.innerHTML = filtered.map(t => toolRow(t)).join('');
      emptyEl.style.display = filtered.length ? 'none' : 'block';
    }

    // Re-bind data-link clicks
    feedEl.querySelectorAll('[data-link]').forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        window.history.pushState({}, '', link.getAttribute('href'));
        window.dispatchEvent(new Event('popstate'));
      });
    });
  }

  // Context switching (AI Tools vs Startup Ideas)
  document.getElementById('contextToggle').addEventListener('click', (e) => {
    const btn = e.target.closest('.dir-toggle-btn');
    if (!btn) return;
    currentContext = btn.dataset.context;
    document.querySelectorAll('.dir-toggle-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    
    // Reset search
    searchQuery = '';
    const searchInput = document.getElementById('dirSearch');
    if(searchInput) searchInput.value = '';
    
    renderFeed();
  });

  // Tab switching
  document.getElementById('dirTabs').addEventListener('click', (e) => {
    const tab = e.target.closest('.dir-tab');
    if (!tab) return;
    currentTab = tab.dataset.tab;
    document.querySelectorAll('.dir-tab').forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    renderFeed();
  });

  // Category pills
  pillsContainer.addEventListener('click', (e) => {
    const pill = e.target.closest('.cat-pill');
    if (!pill) return;
    currentCat = pill.dataset.cat;
    document.querySelectorAll('.cat-pill').forEach(p => p.classList.remove('active'));
    pill.classList.add('active');
    renderFeed();
  });

  // Inline search
  document.getElementById('dirSearch').addEventListener('input', (e) => {
    searchQuery = e.target.value.toLowerCase().trim();
    renderFeed();
  });
}
