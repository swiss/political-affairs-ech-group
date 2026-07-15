// Appendix lettering (A, B, C...) in table of contents

(function() {
  'use strict';

  const toc = document.querySelector('#toc > ol.toc');
  if (!toc) return;

  let appendixCounter = 0;
  const appendixLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

  const items = toc.querySelectorAll('li');
  items.forEach((item, index) => {
    const link = item.querySelector('a');
    if (!link) return;

    // Check if this is an appendix section
    const href = link.getAttribute('href');
    if (href && href.includes('appendix')) {
      const secno = item.querySelector('span.secno');
      if (secno && appendixCounter < appendixLetters.length) {
        const letter = appendixLetters[appendixCounter];
        secno.textContent = letter + '. ';
        appendixCounter++;
      }
    }
  });
})();
