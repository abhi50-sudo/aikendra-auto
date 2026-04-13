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
  const diffClass = idea.difficulty ? idea.difficulty.toLowerCase() : 'beginner';
  const diffEmoji = { beginner: '🟢', intermediate: '🟡', advanced: '🔴' }[diffClass] || '🟢';
  const categoryEmoji = {
    'SaaS': '💡', 'Content Creation': '🎬', 'Automation Tools': '⚙️',
    'Developer Tools': '💻', 'Marketing Tools': '📣', 'Productivity Tools': '⚡',
    'E-commerce Tools': '🛒', 'Coding': '💻', 'Writing': '✍️'
  }[idea.category] || '💡';

  return `
    <a href="/startup-ideas/${idea.slug}" class="idea-card animate-in" data-link>
      <div class="idea-card-top">
        <div class="idea-card-icon">${categoryEmoji}</div>
        <div class="idea-card-badges">
          <span class="badge badge-${diffClass}">${diffEmoji} ${idea.difficulty}</span>
        </div>
      </div>
      <h3>${idea.title}</h3>
      <p>${idea.summary}</p>
      <div class="idea-card-meta">
        ${idea.marketSize ? `<div class="idea-meta-item"><span class="idea-meta-label">Market</span><span class="idea-meta-value">${idea.marketSize.split(' ')[0]}</span></div>` : ''}
        ${idea.timeToMVP ? `<div class="idea-meta-item"><span class="idea-meta-label">MVP</span><span class="idea-meta-value">${idea.timeToMVP}</span></div>` : ''}
      </div>
      <div class="idea-card-footer">
        <span class="badge" style="background:var(--bg-tertiary);color:var(--text-secondary);">${idea.category}</span>
        <span class="idea-card-cta">Explore →</span>
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
