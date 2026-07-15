// Copy to clipboard button for code examples

(function() {
  'use strict';

  // Add copy button to code examples
  const examples = document.querySelectorAll('.example, .note');

  examples.forEach(example => {
    const preEl = example.querySelector('pre');
    if (!preEl) return;

    // Check if button already exists
    if (example.querySelector('.ech-copy-btn')) return;

    // Make parent relative if not already
    if (window.getComputedStyle(example).position === 'static') {
      example.style.position = 'relative';
    }

    // Create copy button
    const button = document.createElement('button');
    button.className = 'ech-copy-btn';
    button.setAttribute('aria-label', 'Copy code to clipboard');
    button.textContent = '📋';

    button.addEventListener('click', function(e) {
      e.preventDefault();

      // Get code text
      const code = preEl.textContent;

      // Copy to clipboard
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(code).then(() => {
          button.textContent = '✓';
          setTimeout(() => {
            button.textContent = '📋';
          }, 2000);
        });
      } else {
        // Fallback for older browsers
        const textarea = document.createElement('textarea');
        textarea.value = code;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);

        button.textContent = '✓';
        setTimeout(() => {
          button.textContent = '📋';
        }, 2000);
      }
    });

    example.appendChild(button);
  });
})();
