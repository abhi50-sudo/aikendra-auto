// Startup Ideas Directory Page
import { ideaCard } from '../components/card.js';

const ideaCategories = ['All', 'SaaS', 'Content Creation', 'Automation Tools', 'Developer Tools', 'Marketing Tools', 'Productivity Tools', 'E-commerce Tools'];

let currentCategory = 'All';
let searchQuery = '';

function getFilteredIdeas() {
  let ideas = [...window.__AK_IDEAS];
  if (searchQuery) {
    const q = searchQuery.toLowerCase();
    ideas = ideas.filter(i =>
      i.title.toLowerCase().includes(q) ||
      i.summary.toLowerCase().includes(q) ||
      i.tags.some(t => t.toLowerCase().includes(q))
    );
  }
  if (currentCategory !== 'All') {
    ideas = ideas.filter(i => i.category === currentCategory);
  }
  return ideas;
}

function renderGrid() {
  const ideas = getFilteredIdeas();
  const gridEl = document.getElementById('ideasGrid');
  const countEl = document.getElementById('ideasCount');

  if (countEl) countEl.textContent = `${ideas.length} ideas found`;

  if (!ideas.length) {
    gridEl.innerHTML = '<p style="text-align:center;color:var(--text-tertiary);padding:var(--space-3xl);grid-column:1/-1;">No ideas found matching your criteria.</p>';
    return;
  }
  gridEl.innerHTML = ideas.map(i => ideaCard(i)).join('');
}

export function renderIdeas() {
  currentCategory = 'All';
  searchQuery = '';

  return `
    <div class="container">
      <div class="page-header">
        <h1>AI Startup Ideas</h1>
        <p>Curated AI-powered business ideas for entrepreneurs and builders.</p>
      </div>

      <div class="filters-bar">
        <input type="text" class="search-input" id="ideasSearch" placeholder="Search startup ideas..." />
        <span id="ideasCount" style="color:var(--text-tertiary);font-size:var(--font-sm);white-space:nowrap;"></span>
      </div>

      <div class="filter-chips" id="ideasChips">
        ${ideaCategories.map(c => `<button class="chip ${c === 'All' ? 'active' : ''}" data-category="${c}">${c}</button>`).join('')}
      </div>

      <div class="grid grid-3" id="ideasGrid" style="margin-top:var(--space-xl);"></div>
    </div>
    <div style="height:var(--space-4xl);"></div>
  `;
}

export function initIdeas() {
  renderGrid();

  document.getElementById('ideasSearch').addEventListener('input', (e) => {
    searchQuery = e.target.value;
    renderGrid();
  });

  document.getElementById('ideasChips').addEventListener('click', (e) => {
    const chip = e.target.closest('.chip');
    if (!chip) return;
    currentCategory = chip.dataset.category;
    document.querySelectorAll('#ideasChips .chip').forEach(c => c.classList.remove('active'));
    chip.classList.add('active');
    renderGrid();
  });
}
