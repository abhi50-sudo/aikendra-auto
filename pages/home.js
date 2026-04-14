// Homepage — Directory-First Layout (Tools First, SEO at Bottom)
import { toolCard, ideaCard } from '../components/card.js';

const categories = [
  { slug: 'all', name: 'All', icon: '\u{1F4C1}' },
  { slug: 'writing', name: 'Writing', icon: '\u270D\uFE0F' },
  { slug: 'image-generation', name: 'Image Gen', icon: '\u{1F3A8}' },
  { slug: 'video-creation', name: 'Video', icon: '\u{1F3AC}' },
  { slug: 'audio-voice', name: 'Audio', icon: '\u{1F399}\uFE0F' },
  { slug: 'coding-development', name: 'Coding', icon: '\u{1F4BB}' },
  { slug: 'productivity', name: 'Productivity', icon: '\u{1F4CB}' },
  { slug: 'marketing', name: 'Marketing', icon: '\u{1F4E2}' },
  { slug: 'finance', name: 'Finance', icon: '\u{1F6E1}\uFE0F' },
  { slug: 'automation', name: 'Automation', icon: '\u26A1' },
  { slug: 'research', name: 'Research', icon: '\u{1F52C}' },
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
          ${t.logo && t.logo.includes('http') ? `<img src="${t.logo.trim()}" alt="${t.name} - ${t.category} AI Tool" onerror="this.parentElement.innerHTML='&#129302;'; this.parentElement.style='';" style="width:100%;height:100%;object-fit:cover;border-radius:var(--radius-md);">` : (t.logo || '&#129302;')}
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
        <span class="tool-grid-logo">&#128161;</span>
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

export function renderHome() {
  const tools = window.__AK_TOOLS;
  const ideas = window.__AK_IDEAS;

  const featuredTools = tools.filter(t => t.featured);
  const newestTools = [...tools].sort((a, b) => new Date(b.dateAdded) - new Date(a.dateAdded));
  const allTools = [...tools].sort((a, b) => a.name.localeCompare(b.name));

  return `
    <!-- Clean Hero — No clutter -->
    <section class="dir-hero">
      <div class="container">
        <h1>Discover AI Tools & Startup Ideas</h1>
        <p class="dir-hero-stats">${tools.length} AI Tools &#183; ${ideas.length} Startup Ideas &#183; Updated Daily</p>
        <div class="dir-search-wrap">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
          <input type="text" id="dirSearch" placeholder="Search AI tools, startup ideas..." autocomplete="off" />
        </div>
      </div>
    </section>

    <!-- Context Toggle -->
    <section class="dir-context-switch">
      <div class="container">
        <div class="dir-toggle-group" id="contextToggle">
          <button class="dir-toggle-btn active" data-context="tools">&#129302; AI Tools</button>
          <button class="dir-toggle-btn" data-context="ideas">&#128161; Startup Ideas</button>
        </div>
      </div>
    </section>

    <!-- Tab Navigation + Category Pills -->
    <section class="dir-tabs-section" id="tabsSection">
      <div class="container">
        <div class="dir-tabs" id="dirTabs">
          <button class="dir-tab active" data-tab="trending">&#128293; Trending</button>
          <button class="dir-tab" data-tab="new">&#127381; Just Launched</button>
          <button class="dir-tab" data-tab="all">&#128193; All Tools</button>
        </div>
        <div class="dir-category-pills" id="categoryPills">
          ${categories.map(c => `
            <button class="cat-pill ${c.slug === 'all' ? 'active' : ''}" data-cat="${c.slug}">${c.icon} ${c.name}</button>
          `).join('')}
        </div>
      </div>
    </section>

    <!-- Feed — THE MAIN CONTENT -->
    <section class="dir-feed">
      <div class="container">
        <div class="dir-feed-list" id="dirFeed">
          ${featuredTools.map(t => toolRow(t)).join('')}
        </div>
        <div class="dir-feed-empty" id="dirFeedEmpty" style="display:none;">
          <p>No results found. Try a different search or category.</p>
        </div>
      </div>
    </section>

    <!-- Minimal CTA -->
    <section class="dir-cta">
      <div class="container">
        <p>Know an AI tool? <a href="/submit" data-link>Submit it &#8594;</a></p>
      </div>
    </section>

    <!-- SEO-only content — below the fold, for crawlers -->
    <section class="seo-bottom-content">
      <div class="container">
        <h2>What is AI Kendra?</h2>
        <p>AI Kendra is a comprehensive, free-to-use directory of artificial intelligence tools and startup ideas. The platform currently indexes <strong>${tools.length} AI tools</strong> across <strong>${categories.length - 1} categories</strong>, with new tools added daily through automated curation and community submissions. According to <a href="https://explodingtopics.com/blog/ai-tools" target="_blank" rel="noopener">Exploding Topics research</a>, more than 14,700 AI tools were launched in 2025 alone — making curated directories like AI Kendra essential for discovering the right tool.</p>

        <h2>AI Tools by Category and Pricing</h2>
        <p>The following table shows the distribution of AI tools across each category in the AI Kendra directory, along with pricing availability. Data as of ${new Date().toLocaleDateString('en-US', { month: 'long', year: 'numeric' })}:</p>
        <div class="table-responsive">
          <table class="seo-table">
            <thead><tr><th>Category</th><th>Tools Listed</th><th>Free Options</th></tr></thead>
            <tbody>
              ${categories.filter(c => c.slug !== 'all').map(c => {
                const catTools = tools.filter(t => getCategorySlug(t.category) === c.slug);
                const freeCount = catTools.filter(t => ['Free','Freemium','Open Source'].includes(t.pricing)).length;
                return `<tr><td>${c.icon} ${c.name}</td><td>${catTools.length}</td><td>${freeCount}</td></tr>`;
              }).join('')}
              <tr><td><strong>Total</strong></td><td><strong>${tools.length}</strong></td><td><strong>${tools.filter(t => ['Free','Freemium','Open Source'].includes(t.pricing)).length}</strong></td></tr>
            </tbody>
          </table>
        </div>

        <h2>Frequently Asked Questions</h2>
        <details class="faq-item">
          <summary><h3>What is AI Kendra and how does it work?</h3></summary>
          <p>AI Kendra is a curated directory that indexes ${tools.length}+ AI tools across ${categories.length - 1} categories including Writing, Image Generation, Video Creation, Audio, Coding, Productivity, Marketing, Finance, Automation, and Research. Each tool is categorized by function, pricing model, and use case. Users can search, filter by category, and browse trending or newly launched tools — all without registration. According to <a href="https://www.statista.com/topics/3104/ai-market-worldwide/" target="_blank" rel="noopener">Statista</a>, the global AI market is projected to reach $305 billion by 2026.</p>
        </details>
        <details class="faq-item">
          <summary><h3>How are AI tools added to the directory?</h3></summary>
          <p>Tools are added through three sources: (1) a curated backlog of verified, high-quality AI products reviewed by our team, (2) automated discovery from <a href="https://github.com/trending" target="_blank" rel="noopener">GitHub trending repositories</a> with 50+ stars in the AI/ML category, and (3) community submissions via our <a href="/submit" data-link>submit page</a>. On average, 5-8 new tools are added per day. As noted by <a href="https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai" target="_blank" rel="noopener">McKinsey's State of AI report</a>, 72% of organizations now use AI in at least one business function.</p>
        </details>
        <details class="faq-item">
          <summary><h3>What are the best free AI tools in 2026?</h3></summary>
          <p>AI Kendra lists ${tools.filter(t => t.pricing === 'Free').length} completely free AI tools and ${tools.filter(t => t.pricing === 'Freemium').length} freemium tools. Popular free options include ChatGPT for general AI assistance, Canva for design, CapCut for video editing, Craiyon for image generation, and Codeium for code completion. The open-source category includes ${tools.filter(t => t.pricing === 'Open Source').length} tools like Stable Diffusion, Whisper AI, and LangChain.</p>
        </details>
        <details class="faq-item">
          <summary><h3>Is AI Kendra free to use?</h3></summary>
          <p>Yes, AI Kendra is completely free to browse, search, and use. No registration, login, or payment is required. The platform is supported by the community and updated daily with new AI tools and startup ideas.</p>
        </details>
        <details class="faq-item">
          <summary><h3>How can I submit my AI tool to the directory?</h3></summary>
          <p>Visit our <a href="/submit" data-link>Submit page</a> and provide your tool's name, website URL, category, pricing model, and a short description. All submissions are reviewed by our team within 24-48 hours before being published to the directory.</p>
        </details>
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

  let currentContext = 'tools';
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

    feedEl.querySelectorAll('[data-link]').forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        window.history.pushState({}, '', link.getAttribute('href'));
        window.dispatchEvent(new Event('popstate'));
      });
    });
  }

  document.getElementById('contextToggle').addEventListener('click', (e) => {
    const btn = e.target.closest('.dir-toggle-btn');
    if (!btn) return;
    currentContext = btn.dataset.context;
    document.querySelectorAll('.dir-toggle-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    searchQuery = '';
    const searchInput = document.getElementById('dirSearch');
    if(searchInput) searchInput.value = '';
    renderFeed();
  });

  document.getElementById('dirTabs').addEventListener('click', (e) => {
    const tab = e.target.closest('.dir-tab');
    if (!tab) return;
    currentTab = tab.dataset.tab;
    document.querySelectorAll('.dir-tab').forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    renderFeed();
  });

  pillsContainer.addEventListener('click', (e) => {
    const pill = e.target.closest('.cat-pill');
    if (!pill) return;
    currentCat = pill.dataset.cat;
    document.querySelectorAll('.cat-pill').forEach(p => p.classList.remove('active'));
    pill.classList.add('active');
    renderFeed();
  });

  document.getElementById('dirSearch').addEventListener('input', (e) => {
    searchQuery = e.target.value.toLowerCase().trim();
    renderFeed();
  });
}
