// Navbar component
export function renderNavbar() {
  // Navbar is rendered in index.html statically for performance
  return '';
}

export function initNavbar(toggleThemeFn) {
  const hamburger = document.getElementById('hamburger');
  const navLinks = document.getElementById('navLinks');
  const themeToggle = document.getElementById('themeToggle');

  if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('active');
      navLinks.classList.toggle('open');
    });
  }

  if (themeToggle && toggleThemeFn) {
    themeToggle.addEventListener('click', toggleThemeFn);
  }
}
