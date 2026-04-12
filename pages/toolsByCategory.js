// Tools by Category Page
import { toolCard } from '../components/card.js';

const categoryMap = {
  'writing': 'Writing',
  'image-generation': 'Image Generation',
  'video-creation': 'Video Creation',
  'audio-voice': 'Audio & Voice',
  'coding-development': 'Coding & Development',
  'productivity': 'Productivity',
  'marketing': 'Marketing',
  'finance': 'Finance',
  'automation': 'Automation',
  'research': 'Research'
};

export function renderToolsByCategory(slug) {
  const categoryName = categoryMap[slug];
  if (!categoryName) {
    return `
      <div class="static-page">
        <div class="container" style="text-align:center;padding:6rem 0;">
          <h1>Category Not Found</h1>
          <p style="color:var(--text-secondary);margin:var(--space-lg) 0;">The category "${slug}" doesn't exist.</p>
          <a href="/ai-tools" class="btn btn-primary" data-link>View All Tools</a>
        </div>
      </div>
    `;
  }

  const tools = window.__AK_TOOLS.filter(t => t.category === categoryName);

  return `
    <div class="container">
      <div class="page-header">
        <h1>${categoryName} AI Tools</h1>
        <p>Explore ${tools.length} AI tools in the ${categoryName} category.</p>
      </div>
      <div style="margin-bottom:var(--space-xl);">
        <a href="/ai-tools" class="btn btn-secondary btn-sm" data-link>← All Categories</a>
      </div>
      ${tools.length ? `
        <div class="grid grid-3">
          ${tools.map(t => toolCard(t)).join('')}
        </div>
      ` : '<p style="text-align:center;color:var(--text-tertiary);padding:var(--space-3xl);">No tools in this category yet.</p>'}
    </div>
    <div style="height:var(--space-4xl);"></div>
  `;
}
