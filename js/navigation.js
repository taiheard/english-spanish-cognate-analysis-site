(() => {
  const navToggle = document.querySelector('.site-nav__toggle');
  const nav = document.getElementById('primary-navigation');
  const focusTrapSelectors = 'a[href], button:not([disabled]), textarea, input, select, [tabindex]';

  const closeNavigation = () => {
    if (!nav || !navToggle) return;
    nav.classList.remove('is-open');
    navToggle.setAttribute('aria-expanded', 'false');
    navToggle.focus({ preventScroll: true });
  };

  const toggleNavigation = () => {
    if (!nav || !navToggle) return;
    const isOpen = nav.classList.toggle('is-open');
    navToggle.setAttribute('aria-expanded', String(isOpen));
    if (isOpen) {
      const focusable = nav.querySelectorAll(focusTrapSelectors);
      focusable.length && focusable[0].focus();
    }
  };

  navToggle?.addEventListener('click', toggleNavigation);

  nav?.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      closeNavigation();
    }
  });

  nav?.querySelectorAll('.site-nav__link').forEach((link) => {
    link.addEventListener('click', () => {
      if (window.innerWidth <= 840) {
        closeNavigation();
      }
    });
  });

  const highlightActiveLink = () => {
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    nav?.querySelectorAll('.site-nav__link').forEach((link) => {
      const target = link.getAttribute('href');
      if (!target) return;
      if (target === currentPath) {
        link.classList.add('site-nav__link--active');
        link.setAttribute('aria-current', 'page');
      } else {
        link.classList.remove('site-nav__link--active');
        link.removeAttribute('aria-current');
      }
    });
  };

  highlightActiveLink();
})();
