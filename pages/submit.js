// Submit Page — Tabbed form with honeypot spam protection

const toolCategories = ['Writing', 'Image Generation', 'Video Creation', 'Audio & Voice', 'Coding & Development', 'Productivity', 'Marketing', 'Finance', 'Automation', 'Research'];
const ideaCategories = ['SaaS', 'Content Creation', 'Automation Tools', 'Developer Tools', 'Marketing Tools', 'Productivity Tools', 'E-commerce Tools'];
const difficultyLevels = ['Beginner', 'Intermediate', 'Advanced'];

export function renderSubmit() {
  return `
    <div class="container">
      <div class="page-header">
        <h1>Submit to AI Kendra</h1>
        <p>Share an AI tool or startup idea with the community.</p>
      </div>

      <div class="form-card">
        <div class="form-tabs">
          <button class="form-tab active" data-tab="tool">Submit AI Tool</button>
          <button class="form-tab" data-tab="idea">Submit Startup Idea</button>
        </div>

        <!-- Tool Form -->
        <form id="toolForm" class="submit-form">
          <div class="form-group">
            <label>Tool Name <span class="required">*</span></label>
            <input type="text" class="form-control" name="toolName" required />
          </div>
          <div class="form-group">
            <label>Website URL <span class="required">*</span></label>
            <input type="url" class="form-control" name="websiteUrl" placeholder="https://" required />
          </div>
          <div class="form-group">
            <label>Short Description <span class="required">*</span></label>
            <input type="text" class="form-control" name="shortDesc" maxlength="120" placeholder="Max 120 characters" required />
          </div>
          <div class="form-group">
            <label>Full Description</label>
            <textarea class="form-control" name="fullDesc" rows="4" placeholder="Detailed description of the tool..."></textarea>
          </div>
          <div class="form-group">
            <label>Category <span class="required">*</span></label>
            <select class="form-control" name="category" required>
              <option value="">Select category</option>
              ${toolCategories.map(c => `<option value="${c}">${c}</option>`).join('')}
            </select>
          </div>
          <div class="form-group">
            <label>Tags</label>
            <input type="text" class="form-control" name="tags" placeholder="Comma-separated tags (e.g. chatbot, writing, productivity)" />
          </div>
          <div class="form-group">
            <label>Your Email <span class="required">*</span></label>
            <input type="email" class="form-control" name="email" required />
          </div>
          <!-- Honeypot -->
          <div class="hp-field" aria-hidden="true">
            <label>Leave empty</label>
            <input type="text" name="website_url_confirm" tabindex="-1" autocomplete="off" />
          </div>
          <button type="submit" class="btn btn-primary btn-lg" style="width:100%;">Submit Tool</button>
        </form>

        <!-- Idea Form -->
        <form id="ideaForm" class="submit-form" style="display:none;">
          <div class="form-group">
            <label>Idea Title <span class="required">*</span></label>
            <input type="text" class="form-control" name="ideaTitle" required />
          </div>
          <div class="form-group">
            <label>Category <span class="required">*</span></label>
            <select class="form-control" name="ideaCategory" required>
              <option value="">Select category</option>
              ${ideaCategories.map(c => `<option value="${c}">${c}</option>`).join('')}
            </select>
          </div>
          <div class="form-group">
            <label>Problem <span class="required">*</span></label>
            <textarea class="form-control" name="problem" rows="3" placeholder="What problem does this idea solve?" required></textarea>
          </div>
          <div class="form-group">
            <label>Solution <span class="required">*</span></label>
            <textarea class="form-control" name="solution" rows="3" placeholder="How does this idea solve the problem?" required></textarea>
          </div>
          <div class="form-group">
            <label>Target Users</label>
            <input type="text" class="form-control" name="targetUsers" placeholder="Who would use this?" />
          </div>
          <div class="form-group">
            <label>Revenue Model</label>
            <textarea class="form-control" name="revenueModel" rows="2" placeholder="How would this make money?"></textarea>
          </div>
          <div class="form-group">
            <label>Difficulty Level <span class="required">*</span></label>
            <select class="form-control" name="difficulty" required>
              <option value="">Select difficulty</option>
              ${difficultyLevels.map(d => `<option value="${d}">${d}</option>`).join('')}
            </select>
          </div>
          <div class="form-group">
            <label>Your Email <span class="required">*</span></label>
            <input type="email" class="form-control" name="submitterEmail" required />
          </div>
          <!-- Honeypot -->
          <div class="hp-field" aria-hidden="true">
            <label>Leave empty</label>
            <input type="text" name="company_website_url" tabindex="-1" autocomplete="off" />
          </div>
          <button type="submit" class="btn btn-primary btn-lg" style="width:100%;">Submit Idea</button>
        </form>

        <!-- Success Message -->
        <div id="submitSuccess" class="form-success" style="display:none;">
          <div class="success-icon">✅</div>
          <h3>Submission Received!</h3>
          <p>Thank you for your contribution. We'll review your submission and add it to our directory if it meets our criteria.</p>
          <a href="/" class="btn btn-primary" style="margin-top:var(--space-lg);" data-link>Back to Home</a>
        </div>
      </div>
    </div>
    <div style="height:var(--space-4xl);"></div>
  `;
}

export function initSubmit() {
  const tabs = document.querySelectorAll('.form-tab');
  const toolForm = document.getElementById('toolForm');
  const ideaForm = document.getElementById('ideaForm');
  const success = document.getElementById('submitSuccess');

  // Tab switching
  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      if (tab.dataset.tab === 'tool') {
        toolForm.style.display = 'block';
        ideaForm.style.display = 'none';
      } else {
        toolForm.style.display = 'none';
        ideaForm.style.display = 'block';
      }
    });
  });

  // Form submissions
  [toolForm, ideaForm].forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      // Honeypot check
      const hp = form.querySelector('.hp-field input');
      if (hp && hp.value) {
        // Bot detected — silently pretend success
        showSuccess();
        return;
      }

      // In a real app, you'd send to an API here
      // For demo, just show success
      showSuccess();
    });
  });

  function showSuccess() {
    toolForm.style.display = 'none';
    ideaForm.style.display = 'none';
    document.querySelector('.form-tabs').style.display = 'none';
    success.style.display = 'block';
  }
}
