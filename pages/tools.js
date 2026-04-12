// AI Tools Directory Page
import { toolCard } from '../components/card.js';

const ITEMS_PER_PAGE = 9;

const allCategories = [
  'All', 'Writing', 'Image Generation', 'Video Creation', 'Audio & Voice',
  'Coding & Development', 'Productivity', 'Marketing', 'Finance', 'Automation', 'Research'
];

let currentPage = 1;
let currentCategory = 'All';
let searchQuery = '';

function getFilteredTools() {
  let tools = [...window.__AK_TOOLS];

  if (searchQuery) {
    const q = searchQuery.toLowerCase();
    tools = tools.filter(t =>
      t.name.toLowerCase().includes(q) ||
      t.shortDescription.toLowerCase().includes(q) ||
      t.tags.some(tag => tag.toLowerCase().includes(q))
    );
  }

  if (currentCategory !== 'All') {
    tools = tools.filter(t => t.category === currentCategory);
  }

  return tools;
}

function renderGrid() {
  const tools = getFilteredTools();
  const totalPages = Math.ceil(tools.length / ITEMS_PER_PAGE);
  const start = (currentPage - 1) * ITEMS_PER_PAGE;
  const paged = tools.slice(start, start + ITEMS_PER_PAGE);

  const gridEl = document.getElementById('toolsGrid');
  const pagEl = document.getElementById('toolsPagination');
  const countEl = document.getElementById('toolsCount');

  if (countEl) countEl.textContent = `${tools.length} tools found`;

  if (!paged.length) {
    gridEl.innerHTML = '<p style="text-align:center;color:var(--text-tertiary);padding:var(--space-3xl);grid-column:1/-1;">No tools found matching your criteria.</p>';
    pagEl.innerHTML = '';
    return;
  }

  gridEl.innerHTML = paged.map(t => toolCard(t)).join('');

  // Pagination
  if (totalPages <= 1) {
    pagEl.innerHTML = '';
    return;
  }

  let pagHtml = `<button class="page-btn" ${currentPage === 1 ? 'disabled' : ''} data-page="${currentPage - 1}">←</button>`;
  for (let i = 1; i <= totalPages; i++) {
    pagHtml += `<button class="page-btn ${i === currentPage ? 'active' : ''}" data-page="${i}">${i}</button>`;
  }
  pagHtml += `<button class="page-btn" ${currentPage === totalPages ? 'disabled' : ''} data-page="${currentPage + 1}">→</button>`;
  pagEl.innerHTML = pagHtml;

  pagEl.querySelectorAll('.page-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const p = parseInt(btn.dataset.page);
      if (p >= 1 && p <= totalPages) {
        currentPage = p;
        renderGrid();
        window.scrollTo({ top: 300, behavior: 'smooth' });
      }
    });
  });
}

export function renderTools() {
  currentPage = 1;
  currentCategory = 'All';
  searchQuery = '';

  return `
    <div class="container">
      <div class="page-header">
        <h1>AI Tools Directory</h1>
        <p>Discover and explore curated AI tools across every category.</p>
      </div>

      <div class="filters-bar">
        <input type="text" class="search-input" id="toolsSearch" placeholder="Search AI tools..." />
        <span id="toolsCount" style="color:var(--text-tertiary);font-size:var(--font-sm);white-space:nowrap;"></span>
      </div>

      <div class="filter-chips" id="toolsChips">
        ${allCategories.map(c => `<button class="chip ${c === 'All' ? 'active' : ''}" data-category="${c}">${c}</button>`).join('')}
      </div>

      <div class="grid grid-3" id="toolsGrid" style="margin-top:var(--space-xl);"></div>
      <div class="pagination" id="toolsPagination"></div>
    </div>
    <div style="height:var(--space-4xl);"></div>
  `;
}

export function initTools() {
  renderGrid();

  // Search
  const searchInput = document.getElementById('toolsSearch');
  searchInput.addEventListener('input', () => {
    searchQuery = searchInput.value;
    currentPage = 1;
    renderGrid();
  });

  // Category chips
  document.getElementById('toolsChips').addEventListener('click', (e) => {
    const chip = e.target.closest('.chip');
    if (!chip) return;
    currentCategory = chip.dataset.category;
    currentPage = 1;
    document.querySelectorAll('#toolsChips .chip').forEach(c => c.classList.remove('active'));
    chip.classList.add('active');
    renderGrid();
  });
}
