// Reusable card components

export function toolCard(tool) {
  return `
    <div class="tool-card animate-in">
      <div class="tool-card-header">
        <div class="tool-logo" ${tool.logo && tool.logo.includes('http') ? 'style="padding:0;background:transparent;overflow:hidden;"' : ''}>
          ${tool.logo && tool.logo.includes('http') ? `<img src="${tool.logo.trim()}" alt="" onerror="this.parentElement.innerHTML='🤖'; this.parentElement.style='';" style="width:100%;height:100%;object-fit:cover;border-radius:var(--radius-md);">` : (tool.logo || '🤖')}
        </div>
        <h3>${tool.name}</h3>
      </div>
      <p>${tool.shortDescription}</p>
      <div class="tool-card-footer">
        <span class="badge">${tool.category}</span>
        <div style="display:flex;gap:var(--space-sm);">
          <a href="/ai-tools/tool/${tool.slug}" class="btn btn-secondary btn-sm" data-link>Details</a>
          <a href="${tool.website}" target="_blank" rel="noopener" class="btn btn-primary btn-sm">Visit ↗</a>
        </div>
      </div>
    </div>
  `;
}

export function ideaCard(idea) {
  const diffClass = idea.difficulty.toLowerCase();
  return `
    <a href="/startup-ideas/${idea.slug}" class="idea-card animate-in" data-link>
      <h3>${idea.title}</h3>
      <p>${idea.summary}</p>
      <div class="idea-card-footer">
        <span class="badge badge-${diffClass}">${idea.difficulty}</span>
        <span class="badge">${idea.category}</span>
      </div>
    </a>
  `;
}

export function categoryCard(cat) {
  return `
    <a href="/ai-tools/${cat.slug}" class="category-card animate-in" data-link>
      <span class="category-icon">${cat.icon}</span>
      <span class="category-name">${cat.name}</span>
      <span class="category-count">${cat.count} tools</span>
    </a>
  `;
}
