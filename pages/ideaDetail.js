// Startup Idea Detail Page

export function renderIdeaDetail(slug) {
  const idea = window.__AK_IDEAS.find(i => i.slug === slug);

  if (!idea) {
    return `
      <div class="static-page">
        <div class="container" style="text-align:center;padding:6rem 0;">
          <h1>Idea Not Found</h1>
          <p style="color:var(--text-secondary);margin:var(--space-lg) 0;">The startup idea you're looking for doesn't exist.</p>
          <a href="/startup-ideas" class="btn btn-primary" data-link>Browse All Ideas</a>
        </div>
      </div>
    `;
  }

  const diffClass = idea.difficulty.toLowerCase();

  return `
    <div class="container">
      <div class="detail-hero">
        <div style="margin-bottom:var(--space-lg);">
          <a href="/startup-ideas" class="btn btn-secondary btn-sm" data-link>← Back to Ideas</a>
        </div>
        <div class="detail-info">
          <h1>${idea.title}</h1>
          <p>${idea.summary}</p>
          <div class="detail-tags">
            <span class="badge badge-${diffClass}">${idea.difficulty}</span>
            <span class="badge">${idea.category}</span>
            ${idea.tags.map(t => `<span class="badge" style="background:var(--bg-tertiary);color:var(--text-secondary);">${t}</span>`).join('')}
          </div>
        </div>
      </div>

      <div class="detail-body">
        <div class="detail-section">
          <h2>Problem Statement</h2>
          <p>${idea.problem}</p>
        </div>

        <div class="detail-section">
          <h2>Proposed Solution</h2>
          <p>${idea.solution}</p>
        </div>

        <div class="detail-section">
          <h2>Target Users</h2>
          <p>${idea.targetUsers}</p>
        </div>

        <div class="detail-section">
          <h2>Revenue Model</h2>
          <p>${idea.revenueModel}</p>
        </div>

        <div class="detail-section">
          <h2>Example Implementation</h2>
          <p>${idea.exampleImplementation}</p>
        </div>

        <div class="detail-section">
          <h2>At a Glance</h2>
          <div class="grid grid-3" style="gap:var(--space-md);">
            <div class="card" style="padding:var(--space-lg);">
              <p style="color:var(--text-tertiary);font-size:var(--font-xs);font-weight:600;text-transform:uppercase;margin-bottom:var(--space-xs);">Difficulty</p>
              <p><span class="badge badge-${diffClass}">${idea.difficulty}</span></p>
            </div>
            <div class="card" style="padding:var(--space-lg);">
              <p style="color:var(--text-tertiary);font-size:var(--font-xs);font-weight:600;text-transform:uppercase;margin-bottom:var(--space-xs);">Category</p>
              <p style="font-weight:600;color:var(--text-primary);">${idea.category}</p>
            </div>
            <div class="card" style="padding:var(--space-lg);">
              <p style="color:var(--text-tertiary);font-size:var(--font-xs);font-weight:600;text-transform:uppercase;margin-bottom:var(--space-xs);">Tags</p>
              <p style="font-weight:600;color:var(--text-primary);">${idea.tags.join(', ')}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  `;
}
