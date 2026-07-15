// References section reorganization

(function() {
  'use strict';

  // Reorganize reference definitions in a custom format
  const refSection = document.getElementById('references');
  if (!refSection) return;

  const defs = refSection.querySelectorAll('dt, dd');
  if (defs.length === 0) return;

  // Create a wrapper for better organization
  const refList = document.createElement('dl');
  refList.className = 'references-list';

  defs.forEach(el => {
    const clone = el.cloneNode(true);
    refList.appendChild(clone);
  });

  refSection.innerHTML = '';
  refSection.appendChild(refList);

  // Update TOC entry for references if it exists
  const tocLink = document.querySelector('#toc a[href="#references"]');
  if (tocLink && tocLink.closest('li')) {
    const parent = tocLink.closest('li');
    parent.classList.add('references-toc-item');
  }
})();
