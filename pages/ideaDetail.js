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

  const diffClass = idea.difficulty ? idea.difficulty.toLowerCase() : 'beginner';
  const diffEmoji = { beginner: '🟢', intermediate: '🟡', advanced: '🔴' }[diffClass] || '🟢';
  const categoryEmoji = {
    'SaaS': '💡', 'Content Creation': '🎬', 'Automation Tools': '⚙️',
    'Developer Tools': '💻', 'Marketing Tools': '📣', 'Productivity Tools': '⚡',
    'E-commerce Tools': '🛒', 'Coding': '💻', 'Writing': '✍️'
  }[idea.category] || '💡';

  const sections = [
    { icon: '🚨', title: 'The Problem', content: idea.problem },
    { icon: '✅', title: 'The Solution', content: idea.solution },
    { icon: '👥', title: 'Target Users', content: idea.targetUsers },
    { icon: '💰', title: 'Revenue Model', content: idea.revenueModel },
    { icon: '🛠️', title: 'How to Build It', content: idea.exampleImplementation },
    { icon: '🏆', title: 'Competitive Edge', content: idea.competitiveEdge },
  ].filter(s => s.content);

  return `
    <div class="container" style="max-width:860px;">
      <div style="margin-bottom:var(--space-xl);">
        <a href="/startup-ideas" class="btn btn-secondary btn-sm" data-link>← Back to Ideas</a>
      </div>

      <!-- Hero -->
      <div class="idea-detail-hero">
        <div class="idea-detail-icon">${categoryEmoji}</div>
        <div class="idea-detail-header-text">
          <div class="idea-detail-badges">
            <span class="badge badge-${diffClass}">${diffEmoji} ${idea.difficulty}</span>
            <span class="badge" style="background:var(--bg-tertiary);color:var(--text-secondary);">${idea.category}</span>
            ${(idea.tags || []).map(t => `<span class="badge" style="background:var(--bg-tertiary);color:var(--text-tertiary);font-size:var(--font-xs);">${t}</span>`).join('')}
          </div>
          <h1 style="margin:var(--space-md) 0 var(--space-sm);">${idea.title}</h1>
          <p style="color:var(--text-secondary);font-size:var(--font-lg);line-height:1.6;">${idea.summary}</p>
        </div>
      </div>

      <!-- At a Glance Stats -->
      <div class="idea-stats-grid">
        ${idea.marketSize ? `
        <div class="idea-stat-card">
          <span class="idea-stat-icon">📊</span>
          <div>
            <p class="idea-stat-label">Market Size</p>
            <p class="idea-stat-value">${idea.marketSize}</p>
          </div>
        </div>` : ''}
        ${idea.timeToMVP ? `
        <div class="idea-stat-card">
          <span class="idea-stat-icon">⏱️</span>
          <div>
            <p class="idea-stat-label">Time to MVP</p>
            <p class="idea-stat-value">${idea.timeToMVP}</p>
          </div>
        </div>` : ''}
        <div class="idea-stat-card">
          <span class="idea-stat-icon">📈</span>
          <div>
            <p class="idea-stat-label">Difficulty</p>
            <p class="idea-stat-value">${idea.difficulty}</p>
          </div>
        </div>
      </div>

      <!-- Content Sections -->
      <div class="idea-sections">
        ${sections.map(s => `
          <div class="idea-section-card">
            <h2 class="idea-section-title">${s.icon} ${s.title}</h2>
            <p class="idea-section-body">${s.content}</p>
          </div>
        `).join('')}
      </div>

      <!-- CTA -->
      <div class="idea-cta-box">
        <h3>Ready to build this?</h3>
        <p>Browse our AI tools directory to find the right tools to bring this idea to life.</p>
        <a href="/ai-tools" class="btn btn-primary" data-link>Browse AI Tools →</a>
      </div>
    </div>
    <div style="height:var(--space-4xl);"></div>
  `;
}
