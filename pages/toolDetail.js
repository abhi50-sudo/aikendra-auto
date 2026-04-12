// Tool Detail Page

export function renderToolDetail(slug) {
  const tool = window.__AK_TOOLS.find(t => t.slug === slug);

  if (!tool) {
    return `
      <div class="static-page">
        <div class="container" style="text-align:center;padding:6rem 0;">
          <h1>Tool Not Found</h1>
          <p style="color:var(--text-secondary);margin:var(--space-lg) 0;">The tool you're looking for doesn't exist.</p>
          <a href="/ai-tools" class="btn btn-primary" data-link>Browse AI Tools</a>
        </div>
      </div>
    `;
  }

  return `
    <div class="container">
      <div class="detail-hero">
        <div style="margin-bottom:var(--space-lg);">
          <a href="/ai-tools" class="btn btn-secondary btn-sm" data-link>← Back to Tools</a>
        </div>
        <div class="detail-hero-inner">
          <div class="detail-logo" ${tool.logo && tool.logo.includes('http') ? 'style="padding:0;background:transparent;"' : ''}>
            ${tool.logo && tool.logo.includes('http') ? `<img src="${tool.logo.trim()}" alt="${tool.name} Logo" onerror="this.parentElement.innerHTML='🤖'; this.parentElement.style='';" style="width:100%;height:100%;object-fit:cover;border-radius:24px;">` : (tool.logo || '🤖')}
          </div>
          <div class="detail-info">
            <h1>${tool.name}</h1>
            <p>${tool.shortDescription}</p>
            <div class="detail-tags">
              <span class="badge">${tool.category}</span>
              ${(tool.tags || []).filter(t => t !== tool.category).map(t => `<span class="badge" style="background:var(--bg-tertiary);color:var(--text-secondary);">${t}</span>`).join('')}
            </div>
            <a href="${tool.website || '#'}" target="_blank" rel="noopener" class="btn btn-primary">Visit Website ↗</a>
          </div>
        </div>
      </div>

      <div class="detail-body">
        <div class="detail-section">
          <h2>About ${tool.name}</h2>
          <p style="white-space: pre-wrap;">${tool.description || tool.shortDescription}</p>
        </div>

        ${tool.features && tool.features.length ? `
          <div class="detail-section">
            <h2>Key Features</h2>
            <ul>
              ${tool.features.map(f => `<li>${f}</li>`).join('')}
            </ul>
          </div>
        ` : ''}

        <div class="detail-section">
          <h2>Details</h2>
          <div class="grid grid-3" style="gap:var(--space-md);">
            <div class="card" style="padding:var(--space-lg);">
              <p style="color:var(--text-tertiary);font-size:var(--font-xs);font-weight:600;text-transform:uppercase;margin-bottom:var(--space-xs);">Category</p>
              <p style="font-weight:600;color:var(--text-primary);">${tool.category}</p>
            </div>
            <div class="card" style="padding:var(--space-lg);">
              <p style="color:var(--text-tertiary);font-size:var(--font-xs);font-weight:600;text-transform:uppercase;margin-bottom:var(--space-xs);">Added</p>
              <p style="font-weight:600;color:var(--text-primary);">${tool.dateAdded && !isNaN(new Date(tool.dateAdded)) ? new Date(tool.dateAdded).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }) : 'Recently Added'}</p>
            </div>
            <div class="card" style="padding:var(--space-lg);">
              <p style="color:var(--text-tertiary);font-size:var(--font-xs);font-weight:600;text-transform:uppercase;margin-bottom:var(--space-xs);">Website</p>
              <a href="${tool.website || '#'}" target="_blank" rel="noopener" style="font-weight:600;font-size:var(--font-sm);">${(tool.website || '').replace('https://', '').replace(/(^\w+:|^)\/\//, '').split('/')[0] || 'Link'}</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  `;
}
