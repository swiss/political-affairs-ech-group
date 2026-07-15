# eCH-0296 – Erlasse und Gesetzestexte

Spezifikation für die strukturierte Erfassung, Verwaltung und Veröffentlichung von Erlassen und Gesetzestexten in der Schweiz.

## Installation

### Prerequisites

- Python 3.8+
- Node.js 14+
- pip (Python package manager)

### Setup

1. **Install Bikeshed** (if not already installed):
   ```bash
   cd bikeshed
   python3 -m venv .venv
   .venv/bin/pip install bikeshed
   # Or via pipx (recommended):
   pipx install bikeshed
   ```

2. **Install Node dependencies**:
   ```bash
   npm install
   ```

3. **Download dokieli CSS/JS** (already in `output/`):
   - `output/dokieli.css` - dokieli UI styles
   - `output/dokieli.js` - dokieli functionality

## Project Structure

```
ech-0296/
├── bikeshed/              # Bikeshed tool (local install or .venv)
│   ├── .venv/             # Local Python virtual environment
│   ├── index.bs           # Main spec source (Bikeshed format)
│   ├── header.include     # HTML header template
│   └── ...
├── input/                 # Authored content
│   ├── css/               # Custom stylesheets
│   │   ├── appendix.css
│   │   ├── copy-btn.css
│   │   ├── references.css
│   │   ├── tables.css
│   │   └── toc.css
│   ├── js/                # Custom scripts
│   │   ├── sidebar.js
│   │   ├── appendix-toc.js
│   │   ├── references.js
│   │   ├── tof-tot.js
│   │   └── copy-code.js
│   ├── sections/          # Spec sections (markdown)
│   │   ├── main/
│   │   └── appendix/
│   ├── examples/          # Code examples
│   └── images/            # Images and logos
├── output/                # Generated output
│   ├── index.html         # Compiled spec
│   ├── styles.css         # Concatenated CSS
│   ├── scripts.js         # Concatenated JS
│   ├── dokieli.css        # dokieli UI styles
│   ├── dokieli.js         # dokieli functionality
│   ├── basic.css          # dokieli typography layer
│   └── images/
├── misc/                  # Reference materials
└── scripts/               # Build utilities
```

## Development Workflow

### Phase 1: Test Bikeshed Base (without dokieli)

1. Build the specification:
   ```bash
   npm run bikeshed:build
   ```

2. Serve locally:
   ```bash
   npm run serve
   ```

3. Open http://localhost:3000 in your browser

**Checklist**:
- [ ] Title and structure render correctly
- [ ] Table of Contents appears
- [ ] Example 1: 12 lines numbered consistently
- [ ] Example 2: lines 1-22 numbered, lines 6-22 highlighted
- [ ] Copy button works on hover
- [ ] Self-links (¶) appear on hover
- [ ] German captions: "Abbildung" and "Tabelle"
- [ ] Appendix lettering (A, B, C) in TOC

### Phase 2: Test with dokieli

1. Ensure dokieli files are in place:
   ```bash
   ls output/dokieli.css output/dokieli.js output/basic.css
   ```

2. Build and serve:
   ```bash
   npm run build && npm run serve
   ```

**Additional Checklist**:
- [ ] Hamburger menu appears (top-left)
- [ ] Hamburger menu is functional
- [ ] dokieli annotation features work
- [ ] Pre/code blocks not affected by basic.css styling
- [ ] Links don't have unwanted borders

### Phase 3: Watch Mode (Development)

For live reloading during development:
```bash
npm run dev
```

This will watch for changes in:
- `input/sections/` (markdown)
- `input/css/` (stylesheets)
- `input/js/` (scripts)
- `bikeshed/*.bs` (Bikeshed source)

## CSS Cascade Order

Styles are applied in this order (later wins at equal specificity):

1. Bikeshed embedded `<style>` blocks (grid layout, counters, etc.)
2. `dokieli.css` (hamburger menu, annotation UI)
3. `basic.css` (dokieli typography layer)
4. Concatenated `styles.css` from `input/css/*.css`

Our custom CSS in `input/css/` loads last and wins without needing `!important`.

## Common Issues

### Line numbers inconsistent between examples

**Problem**: Example 2 shows numbers only for lines 6-22

**Solution**: Ensure `line-numbers:` directive is in Example 2's include

### Copy button not working

**Problem**: Button appears but copy fails in some browsers

**Solution**: Check that `copy-code.js` has fallback for older browsers

### dokieli hamburger not showing

**Problem**: Menu button doesn't appear

**Solution**: Verify `dokieli.js` is loaded and `dokieli.css` is applied

## Building for Deployment

To build the final output for deployment:

```bash
npm run build
```

This creates:
- `output/index.html` - Compiled specification
- `output/styles.css` - All CSS concatenated
- `output/scripts.js` - All JavaScript concatenated
- `output/dokieli.css` - dokieli UI layer
- `output/dokieli.js` - dokieli application
- `output/basic.css` - dokieli typography
- `output/images/` - All images

## References

- [Bikeshed](https://tabatkins.github.io/bikeshed/)
- [Akoma Ntoso (AKN)](http://docs.oasis-open.org/legaldocml/)
- [dokieli](https://dokie.li/)
- [European Legislation Identifier (ELI)](https://op.europa.eu/en/web/eu-vocabularies/eli)

## License

CC-BY-4.0
