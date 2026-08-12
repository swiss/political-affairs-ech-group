<script>
  import { onMount, onDestroy } from 'svelte';
  import { createEditorView, legalSchema, aknXmlToDoc } from './prosemirror.js';
  import { docJson, aknXmlSource, selectionState, resolvedRef, logOp } from './stores.js';
  import { EditorState }  from 'prosemirror-state';

  let container;
  let view;

  // Article navigation list derived from document
  let articles = [];

  onMount(() => {
    view = createEditorView(container);
    updateArticleList(view.state.doc);
  });

  onDestroy(() => {
    if (view) view.destroy();
  });

  // When aknXmlSource changes (from CodeMirror or URL load), rebuild PM doc
  let prevXml = '';
  $: if ($aknXmlSource && $aknXmlSource !== prevXml) {
    prevXml = $aknXmlSource;
    const pmDoc = aknXmlToDoc($aknXmlSource);
    if (pmDoc && view) {
      try {
        const doc = legalSchema.nodeFromJSON(pmDoc);
        const newState = EditorState.create({
          doc,
          plugins: view.state.plugins,
        });
        view.updateState(newState);
        updateArticleList(doc);
        logOp({ type: 'xml-edit', input: 'akn-xml', output: `${articles.length} articles`, status: 'ok' });
      } catch (e) {
        logOp({ type: 'xml-edit', input: 'akn-xml', status: 'error', detail: e.message });
      }
    }
  }

  function updateArticleList(doc) {
    const list = [];
    doc.forEach((node) => {
      if (node.type.name === 'article') {
        list.push({ n: node.attrs.n, eId: node.attrs.eId, title: node.attrs.title });
      }
    });
    articles = list;
  }

  // Jump to article in PM view
  function jumpToArticle(eId) {
    if (!view) return;
    let targetPos = null;
    view.state.doc.descendants((node, pos) => {
      if (node.type.name === 'article' && node.attrs.eId === eId) {
        targetPos = pos;
        return false;
      }
    });
    if (targetPos != null) {
      const tr = view.state.tr.setSelection(
        view.state.selection.constructor.near(view.state.doc.resolve(targetPos + 1))
      );
      view.dispatch(tr);
      view.focus();
    }
  }

  // Add cross-reference mark to current PM selection
  function addRefMark() {
    if (!view || !$selectionState?.compact_display) return;
    const { from, to } = view.state.selection;
    if (from === to) return;

    const mark = legalSchema.marks.ref.create({
      href:    $selectionState.hash_uri || $selectionState.compact_display,
      compact: $selectionState.compact_display,
      human:   $selectionState.human_de || '',
    });
    const tr = view.state.tr.addMark(from, to, mark);
    view.dispatch(tr);
    logOp({
      type: 'annotation',
      input: `pos ${from}-${to}`,
      output: $selectionState.compact_display,
      status: 'ok',
    });
  }

  // Remove cross-reference mark
  function removeRefMark() {
    if (!view) return;
    const { from, to } = view.state.selection;
    const tr = view.state.tr.removeMark(from, to, legalSchema.marks.ref);
    view.dispatch(tr);
  }

  // Export current PM doc as simple AKN XML skeleton
  function exportXml() {
    if (!view) return;
    const doc = view.state.doc;
    let xml = `<?xml version="1.0" encoding="UTF-8"?>\n<akomaNtoso xmlns="http://docs.oasis-open.org/legaldocml/ns/akn/3.0">\n  <act>\n    <body>\n`;
    doc.forEach(node => {
      if (node.type.name === 'article') {
        xml += `      <article eId="${node.attrs.eId}" num="${node.attrs.n}">\n`;
        node.forEach(para => {
          if (para.type.name === 'paragraph') {
            xml += `        <paragraph eId="${para.attrs.eId}" num="${para.attrs.n}">\n`;
            xml += `          <content><p>${para.textContent}</p></content>\n`;
            xml += `        </paragraph>\n`;
          }
        });
        xml += `      </article>\n`;
      }
    });
    xml += `    </body>\n  </act>\n</akomaNtoso>`;
    aknXmlSource.set(xml);
    logOp({ type: 'xml-export', input: `${articles.length} articles`, output: 'akn-xml', status: 'ok' });
  }
</script>

<div class="left-panel">
  <!-- Article navigation sidebar -->
  <div class="art-nav">
    <div class="art-nav__header">
      <span class="art-nav__label">Articles</span>
      {#if articles.length > 0}
        <span class="art-nav__count">{articles.length}</span>
      {/if}
    </div>
    <div class="art-nav__list">
      {#if articles.length === 0}
        <div class="art-nav__empty">—</div>
      {/if}
      {#each articles as art}
        <button
          class="art-nav__item"
          on:click={() => jumpToArticle(art.eId)}
          title={art.eId}
        >
          <span class="art-nav__n">Art. {art.n}</span>
          {#if art.title}
            <span class="art-nav__title">{art.title}</span>
          {/if}
        </button>
      {/each}
    </div>
  </div>

  <!-- Editor area -->
  <div class="editor-area">
    <!-- Toolbar for editor actions -->
    <div class="editor-toolbar">
      <button class="editor-toolbar__btn" on:click={addRefMark}
              disabled={!$selectionState}
              title="Underline selection as cross-reference link">
        <span>↗</span> Link
      </button>
      <button class="editor-toolbar__btn" on:click={removeRefMark}
              title="Remove cross-reference mark">
        <span>×</span> Unlink
      </button>
      <div class="editor-toolbar__sep"></div>
      <button class="editor-toolbar__btn" on:click={exportXml}
              title="Export as AKN XML (updates right panel)">
        <span>⟨/⟩</span> Export XML
      </button>
      {#if $resolvedRef?.metadata?.title_de}
        <span class="editor-toolbar__doc-title">
          {$resolvedRef.document_pointer?.preferred_id ?? ''}
          — {$resolvedRef.metadata.title_de}
        </span>
      {/if}
    </div>

    <!-- ProseMirror mount point -->
    <div class="pm-container" bind:this={container}></div>
  </div>
</div>

<style>
  .left-panel {
    display: flex;
    flex: 1;
    overflow: hidden;
    border-right: 1px solid var(--border);
  }

  /* Article navigation sidebar */
  .art-nav {
    width: 80px;
    min-width: 80px;
    border-right: 1px solid var(--border);
    background: var(--surface-2);
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }
  .art-nav__header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 8px 8px 4px;
    border-bottom: 1px solid var(--border);
  }
  .art-nav__label {
    font-size: 10px;
    font-weight: 600;
    letter-spacing: .07em;
    text-transform: uppercase;
    color: var(--text-3);
  }
  .art-nav__count {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--text-3);
  }
  .art-nav__list {
    overflow-y: auto;
    flex: 1;
    padding: 4px 0;
  }
  .art-nav__empty {
    text-align: center;
    color: var(--text-3);
    font-size: 11px;
    padding: 12px 0;
  }
  .art-nav__item {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 100%;
    padding: 4px 8px;
    text-align: left;
    transition: background .1s;
  }
  .art-nav__item:hover { background: var(--border); }
  .art-nav__n {
    font-family: var(--mono);
    font-size: 10px;
    font-weight: 500;
    color: var(--text-2);
    white-space: nowrap;
  }
  .art-nav__title {
    font-size: 9px;
    color: var(--text-3);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 64px;
  }

  /* Editor area */
  .editor-area {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  .editor-toolbar {
    height: 34px;
    display: flex;
    align-items: center;
    gap: 2px;
    padding: 0 10px;
    border-bottom: 1px solid var(--border);
    background: var(--surface-2);
    flex-shrink: 0;
  }
  .editor-toolbar__btn {
    display: flex;
    align-items: center;
    gap: 4px;
    padding: 3px 8px;
    border-radius: var(--radius);
    font-size: 12px;
    color: var(--text-2);
    transition: all .1s;
  }
  .editor-toolbar__btn:hover:not(:disabled) {
    background: var(--surface);
    color: var(--accent);
  }
  .editor-toolbar__btn:disabled { opacity: .4; cursor: default; }
  .editor-toolbar__sep {
    width: 1px;
    height: 18px;
    background: var(--border);
    margin: 0 4px;
  }
  .editor-toolbar__doc-title {
    margin-left: auto;
    font-size: 11px;
    color: var(--text-3);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 280px;
    font-family: var(--serif);
    font-style: italic;
  }

  .pm-container {
    flex: 1;
    overflow-y: auto;
    background: var(--surface);
  }
  .pm-container :global(.ProseMirror) {
    min-height: 100%;
  }
</style>
