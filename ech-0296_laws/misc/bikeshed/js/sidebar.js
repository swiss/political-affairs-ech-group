// Sidebar toggle functionality

(function() {
  'use strict';

  // Create sidebar toggle button if TOC exists
  const nav = document.getElementById('toc');
  if (!nav) return;

  const body = document.body;
  const isNarrow = window.innerWidth < 900;

  if (isNarrow) {
    nav.classList.add('toc-sidebar');
    nav.id = 'toc-nav';

    const toggle = document.createElement('button');
    toggle.id = 'toc-toggle';
    toggle.textContent = '≡ Contents';
    toggle.classList.add('toc-toggle-button');

    document.body.insertBefore(toggle, nav);

    toggle.addEventListener('click', function() {
      nav.classList.toggle('expanded');
    });

    // Close sidebar when clicking on a link
    nav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', function() {
        nav.classList.remove('expanded');
      });
    });
  }
})();
