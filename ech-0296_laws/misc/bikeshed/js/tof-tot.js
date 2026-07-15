// Table of Figures and Table of Tables generation

(function() {
  'use strict';

  // Generate list of figures
  const tofSection = document.getElementById('tof');
  if (tofSection) {
    const figures = document.querySelectorAll('figure:not(.no-tof)');
    if (figures.length > 0) {
      const tofList = document.createElement('ol');
      tofList.className = 'tof-list';

      figures.forEach((fig, index) => {
        const caption = fig.querySelector('figcaption');
        const link = document.createElement('li');

        if (caption) {
          const a = document.createElement('a');
          a.textContent = `Figure ${index + 1}: ${caption.textContent}`;
          link.appendChild(a);
        }

        tofList.appendChild(link);
      });

      tofSection.appendChild(tofList);
    }
  }

  // Generate list of tables
  const totSection = document.getElementById('tot');
  if (totSection) {
    const tables = document.querySelectorAll('figure.table:not(.no-tot)');
    if (tables.length > 0) {
      const totList = document.createElement('ol');
      totList.className = 'tot-list';

      tables.forEach((fig, index) => {
        const caption = fig.querySelector('figcaption');
        const link = document.createElement('li');

        if (caption) {
          const a = document.createElement('a');
          a.textContent = `Table ${index + 1}: ${caption.textContent}`;
          link.appendChild(a);
        }

        totList.appendChild(link);
      });

      totSection.appendChild(totList);
    }
  }
})();
