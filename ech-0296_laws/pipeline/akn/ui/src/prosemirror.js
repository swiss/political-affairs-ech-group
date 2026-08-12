// src/prosemirror.js
// ProseMirror schema, plugins, and selection→store bridge for AKN legal text

import { Schema }        from 'prosemirror-model';
import { EditorState }   from 'prosemirror-state';
import { EditorView }    from 'prosemirror-view';
import { Plugin }        from 'prosemirror-state';
import { keymap }        from 'prosemirror-keymap';
import { baseKeymap }    from 'prosemirror-commands';
import { selectionRaw, resolveSelection } from './stores.js';

// ── Schema ────────────────────────────────────────────────────────────────────

export const legalSchema = new Schema({
  nodes: {
    doc: { content: 'block+' },

    chapter: {
      attrs: { n: { default: '' }, eId: { default: '' } },
      content: '(section | article)+',
      group: 'block',
      toDOM: n => ['div', { class: 'akn-chp', 'data-n': n.attrs.n, 'data-eid': n.attrs.eId }, 0],
      parseDOM: [{ tag: 'div.akn-chp', getAttrs: d => ({ n: d.dataset.n, eId: d.dataset.eid }) }],
    },

    section: {
      attrs: { n: { default: '' }, eId: { default: '' } },
      content: 'article+',
      group: 'block',
      toDOM: n => ['div', { class: 'akn-sec', 'data-n': n.attrs.n, 'data-eid': n.attrs.eId }, 0],
      parseDOM: [{ tag: 'div.akn-sec', getAttrs: d => ({ n: d.dataset.n, eId: d.dataset.eid }) }],
    },

    article: {
      attrs: { n: { default: '' }, eId: { default: '' }, title: { default: '' } },
      content: 'paragraph+',
      group: 'block',
      toDOM: n => ['div', { class: 'akn-art', 'data-n': n.attrs.n, 'data-eid': n.attrs.eId }, 0],
      parseDOM: [{ tag: 'div.akn-art', getAttrs: d => ({ n: d.dataset.n, eId: d.dataset.eid }) }],
    },

    paragraph: {
      attrs: { n: { default: '' }, eId: { default: '' } },
      content: 'inline*',
      group: 'block',
      toDOM: n => ['p', { class: 'akn-para', 'data-n': n.attrs.n, 'data-eid': n.attrs.eId }, 0],
      parseDOM: [{ tag: 'p.akn-para', getAttrs: d => ({ n: d.dataset.n, eId: d.dataset.eid }) }],
    },

    number_item: {
      attrs: { n: { default: '' }, eId: { default: '' } },
      content: 'inline*',
      group: 'block',
      toDOM: n => ['div', { class: 'akn-num', 'data-n': n.attrs.n, 'data-eid': n.attrs.eId }, 0],
      parseDOM: [{ tag: 'div.akn-num', getAttrs: d => ({ n: d.dataset.n, eId: d.dataset.eid }) }],
    },

    litera_item: {
      attrs: { n: { default: '' }, eId: { default: '' } },
      content: 'inline*',
      group: 'block',
      toDOM: n => ['div', { class: 'akn-lit', 'data-n': n.attrs.n, 'data-eid': n.attrs.eId }, 0],
      parseDOM: [{ tag: 'div.akn-lit', getAttrs: d => ({ n: d.dataset.n, eId: d.dataset.eid }) }],
    },

    text: { group: 'inline' },
    hard_break: { inline: true, group: 'inline', selectable: false, toDOM: () => ['br'] },
  },

  marks: {
    /**
     * Cross-reference link (akn:ref in AKN XML).
     * Renders as underlined text with tooltip showing human citation.
     */
    ref: {
      attrs: {
        href:    { default: '' },  // full fragment URI
        compact: { default: '' },  // '#a47-p2-lit-a'
        human:   { default: '' },  // 'BV Art. 47 Abs. 2 lit. a'
      },
      inclusive: false,
      toDOM: n => ['a', {
        href:           n.attrs.href,
        'data-compact': n.attrs.compact,
        'data-human':   n.attrs.human,
        class:          'akn-ref',
        title:          n.attrs.human,
      }, 0],
      parseDOM: [{ tag: 'a.akn-ref', getAttrs: d => ({
        href:    d.getAttribute('href')    ?? '',
        compact: d.getAttribute('data-compact') ?? '',
        human:   d.getAttribute('data-human')   ?? '',
      }) }],
    },

    highlight: {
      toDOM: () => ['mark', { class: 'akn-highlight' }, 0],
      parseDOM: [{ tag: 'mark.akn-highlight' }],
    },

    selection_mark: {
      toDOM: () => ['span', { class: 'akn-sel' }, 0],
      parseDOM: [{ tag: 'span.akn-sel' }],
    },
  },
});


// ── Selection plugin ──────────────────────────────────────────────────────────

/**
 * Resolves the PM selection position to a compact fragment string.
 * Walks the document tree to find the enclosing article/paragraph eId.
 */
function posToCompact(state, pos) {
  const $pos = state.doc.resolve(pos);
  const levels = {};

  for (let d = $pos.depth; d >= 0; d--) {
    const node = $pos.node(d);
    if (!node.attrs?.eId) continue;
    const eId = node.attrs.eId;  // e.g. 'art_47', 'art_47.para_2'

    if (node.type.name === 'article')     levels.article   = eId.match(/art_(\S+)/)?.[1];
    if (node.type.name === 'paragraph')   levels.paragraph = eId.match(/para_(\S+)/)?.[1];
    if (node.type.name === 'number_item') levels.number    = eId.match(/num_(\S+)/)?.[1];
    if (node.type.name === 'litera_item') levels.litera    = eId.match(/lit_(\S+)/)?.[1];
  }

  if (!levels.article) return '';

  let compact = `a${levels.article}`;
  if (levels.paragraph) compact += `_p${levels.paragraph}`;
  if (levels.number)    compact += `_num-${levels.number}`;
  if (levels.litera)    compact += `_lit-${levels.litera}`;
  return compact;
}

let debounce = null;

export const selectionPlugin = new Plugin({
  view(view) {
    return {
      update(view, prevState) {
        if (view.state.selection.eq(prevState.selection)) return;

        const { from, to, empty } = view.state.selection;
        let raw = '';

        if (empty) {
          raw = posToCompact(view.state, from);
        } else {
          const startCompact = posToCompact(view.state, from);
          const endCompact   = posToCompact(view.state, to);
          if (startCompact && endCompact && startCompact !== endCompact) {
            raw = `${startCompact}~${endCompact}`;
          } else {
            raw = startCompact;
          }
        }

        if (raw) {
          clearTimeout(debounce);
          debounce = setTimeout(() => {
            selectionRaw.set(raw);
            resolveSelection(raw);
          }, 80);
        }
      }
    };
  }
});


// ── Editor factory ────────────────────────────────────────────────────────────

/**
 * Create a ProseMirror EditorView with the legal schema and plugins.
 *
 * @param {HTMLElement} dom   — mount target
 * @param {Object}      doc   — initial PM document (JSON or null for empty)
 */
export function createEditorView(dom, doc = null) {
  const initDoc = doc
    ? legalSchema.nodeFromJSON(doc)
    : legalSchema.node('doc', {}, [
        legalSchema.node('article', { n: '1', eId: 'art_1', title: '' }, [
          legalSchema.node('paragraph', { n: '1', eId: 'art_1.para_1' }, [
            legalSchema.text('Paste a Fedlex or ZH-Lex URL above to load a document, or start typing here.'),
          ]),
        ]),
      ]);

  const state = EditorState.create({
    doc: initDoc,
    plugins: [
      selectionPlugin,
      keymap(baseKeymap),
    ],
  });

  return new EditorView(dom, { state });
}


// ── AKN XML → ProseMirror document ───────────────────────────────────────────

/**
 * Lightweight AKN XML parser — converts a subset of AKN XML to PM doc JSON.
 * Full AKN processing would use the backend; this handles preview/annotation.
 *
 * @param {string} xmlStr
 * @returns {Object} PM document JSON
 */
export function aknXmlToDoc(xmlStr) {
  const parser = new DOMParser();
  const xmlDoc = parser.parseFromString(xmlStr, 'application/xml');
  const body   = xmlDoc.querySelector('body, act > body');
  if (!body) return null;

  function convertNode(el) {
    const tag = el.tagName?.toLowerCase();
    const eId = el.getAttribute('eId') ?? '';

    if (tag === 'chapter') {
      return { type: 'chapter', attrs: { n: el.getAttribute('num') ?? '', eId }, content: convertChildren(el) };
    }
    if (tag === 'section') {
      return { type: 'section', attrs: { n: el.getAttribute('num') ?? '', eId }, content: convertChildren(el) };
    }
    if (tag === 'article') {
      return { type: 'article', attrs: { n: el.getAttribute('num') ?? '', eId, title: '' }, content: convertChildren(el) };
    }
    if (tag === 'paragraph') {
      return { type: 'paragraph', attrs: { n: el.getAttribute('num') ?? '', eId }, content: convertInline(el) };
    }
    if (tag === 'listintroduction' || tag === 'intro') {
      return { type: 'paragraph', attrs: { n: '', eId }, content: convertInline(el) };
    }
    if (tag === 'point') {
      return { type: 'litera_item', attrs: { n: el.getAttribute('num') ?? '', eId }, content: convertInline(el) };
    }
    return null;
  }

  function convertChildren(el) {
    return Array.from(el.children).map(convertNode).filter(Boolean);
  }

  function convertInline(el) {
    const text = el.textContent ?? '';
    if (!text.trim()) return [{ type: 'text', text: ' ' }];
    return [{ type: 'text', text }];
  }

  const content = convertChildren(body);
  if (!content.length) return null;
  return { type: 'doc', content };
}
