// Contact Page

export function renderContact() {
  return `
    <div class="static-page">
      <div class="container">
        <h1>Contact Us</h1>
        <p>Have a question, suggestion, or partnership inquiry? We'd love to hear from you.</p>

        <div class="form-card" style="margin-top:var(--space-2xl);">
          <form id="contactForm">
            <div class="form-group">
              <label>Your Name <span class="required">*</span></label>
              <input type="text" class="form-control" name="name" required />
            </div>
            <div class="form-group">
              <label>Email Address <span class="required">*</span></label>
              <input type="email" class="form-control" name="email" required />
            </div>
            <div class="form-group">
              <label>Subject <span class="required">*</span></label>
              <input type="text" class="form-control" name="subject" required />
            </div>
            <div class="form-group">
              <label>Message <span class="required">*</span></label>
              <textarea class="form-control" name="message" rows="5" required></textarea>
            </div>
            <!-- Honeypot -->
            <div class="hp-field" aria-hidden="true">
              <label>Leave empty</label>
              <input type="text" name="fax_number" tabindex="-1" autocomplete="off" />
            </div>
            <button type="submit" class="btn btn-primary btn-lg" style="width:100%;">Send Message</button>
          </form>
          <div id="contactSuccess" class="form-success" style="display:none;">
            <div class="success-icon">📨</div>
            <h3>Message Sent!</h3>
            <p>Thank you for reaching out. We'll get back to you as soon as possible.</p>
          </div>
        </div>
      </div>
    </div>
  `;
}

export function initContact() {
  const form = document.getElementById('contactForm');
  const success = document.getElementById('contactSuccess');

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const hp = form.querySelector('.hp-field input');
    if (hp && hp.value) { form.style.display = 'none'; success.style.display = 'block'; return; }
    form.style.display = 'none';
    success.style.display = 'block';
  });
}
