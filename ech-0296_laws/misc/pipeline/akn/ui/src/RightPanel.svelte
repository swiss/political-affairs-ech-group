<script>
  import { onMount, onDestroy } from 'svelte';
  import { EditorView, basicSetup } from 'codemirror';
  import { xml } from '@codemirror/lang-xml';
  import { EditorState as CMState } from '@codemirror/state';
  import { aknXmlSource, selectionState, logOp } from './stores.js';

  let container;
  let cmView;
  let internalUpdate = false;
  let collapsed = false;

  // Custom AKN-aware theme
  import { EditorView as CMEditorView } from '@codemirror/view';

  const aknTheme = CMEditorView.theme({
    '&': {
      height: '100%',
      fontFamily: "'IBM Plex Mono', monospace",
      fontSize: '12px',
      background: '#1c1b18',
    },
    '.cm-content': { caretColor: '#c8001e', padding: '16px 8px' },
    '.cm-line': { lineHeight: '1.65' },
    '.cm-cursor': { borderLeftColor: '#c8001e' },
    '.cm-selectionBackground': { background: 'rgba(200,0,30,.25)' },
    '.cm-gutters': { background: '#161512', borderRight: '1px solid #2a2925', color: '#5a574f' },
    '&.cm-focused .cm-selectionBackground': { background: 'rgba(200,0,30,.3)' },
  });

  // Highlight AKN-specific eId attributes
  const AKN_HIGHLIGHT = CMEditorView.baseTheme({
    '.cm-akn-eid': { color: '#c8001e', fontWeight: '500' },
  });

  onMount(() => {
    cmView = new EditorView({
      state: CMState.create({
        doc: $aknXmlSource || sampleXml(),
        extensions: [
          basicSetup,
          xml(),
          aknTheme,
          AKN_HIGHLIGHT,
          CMEditorView.updateListener.of(update => {
            if (update.docChanged && !internalUpdate) {
              const src = update.state.doc.toString();
              internalUpdate = true;
              aknXmlSource.set(src);
              internalUpdate = false;
            }
          }),
        ],
      }),
      parent: container,
    });
  });

  onDestroy(() => cmView?.destroy());

  // Sync store → CodeMirror (when XML is set from URL load or export)
  $: if (cmView && $aknXmlSource !== undefined && !internalUpdate) {
    const current = cmView.state.doc.toString();
    if (current !== $aknXmlSource) {
      internalUpdate = true;
      cmView.dispatch({
        changes: { from: 0, to: current.length, insert: $aknXmlSource }
      });
      internalUpdate = false;
    }
  }

  // Highlight the eId matching current selection in CM
  $: if (cmView && $selectionState?.compact_display) {
    // Convert compact to eId for search
    // e.g. '#a47-p2-lit-a' → 'art_47.para_2.lit_a'
    // We just highlight the raw compact for now — full eId lookup would need API
    highlightInSource($selectionState.compact_display);
  }

  function highlightInSource(compact) {
    if (!cmView || !compact) return;
    const src = cmView.state.doc.toString();
    // Look for eId attribute containing the article number
    const artMatch = compact.match(/^#?a(\d+)/);
    if (!artMatch) return;
    const artNum = artMatch[1];
    const searchStr = `eId="art_${artNum}`;
    const idx = src.indexOf(searchStr);
    if (idx >= 0) {
      cmView.dispatch({
        selection: { anchor: idx, head: idx + searchStr.length },
        scrollIntoView: true,
      });
    }
  }

  function sampleXml() {
    return `<?xml version="1.0" encoding="UTF-8"?>
<!-- AKN-CH Sample — paste a Fedlex URL in the toolbar above -->
<akomaNtoso xmlns="http://docs.oasis-open.org/legaldocml/ns/akn/3.0">
  <act>
    <meta>
      <identification source="#editor">
        <FRBRWork>
          <FRBRuri value="/akn/ch/lei/1999-01-01/404"/>
          <FRBRdate date="1999-01-01" name="Generation"/>
          <FRBRauthor href="#bundesrat"/>
          <FRBRcountry value="ch"/>
        </FRBRWork>
        <FRBRExpression>
          <FRBRuri value="/akn/ch/lei/1999-01-01/404/deu@2021-03-07"/>
          <FRBRdate date="2021-03-07" name="Generation"/>
          <FRBRlanguage language="deu"/>
        </FRBRExpression>
      </identification>
    </meta>
    <body>
      <article eId="art_47" num="47">
        <num>Art. 47</num>
        <paragraph eId="art_47.para_1" num="1">
          <content><p>Der Bund wahrt die Eigenständigkeit der Kantone.</p></content>
        </paragraph>
        <paragraph eId="art_47.para_2" num="2">
          <content><p>Er belässt den Kantonen genügend eigene Aufgaben und beachtet
            ihre Organisationsautonomie.</p></content>
        </paragraph>
      </article>
    </body>
  </act>
</akomaNtoso>`;
  }

  // Panel sections
  let showMeta = false;
  let showAnnotations = true;

  $: annotations = [];  // TODO: extract from PM doc marks
</script>

<div class="right-panel" class:right-panel--collapsed={collapsed}>
  <div class="right-panel__header">
    <span class="right-panel__title">AKN Source</span>
    <div class="right-panel__tabs">
      <button class="rp-tab" class:rp-tab--active={showAnnotations}
              on:click={() => showAnnotations = !showAnnotations}
              title="Toggle annotation panel">
        Annotations
      </button>
    </div>
    <button class="right-panel__toggle" on:click={() => collapsed = !collapsed}
            title={collapsed ? 'Expand' : 'Collapse'}>
      {collapsed ? '‹' : '›'}
    </button>
  </div>

  {#if !collapsed}
    <div class="right-panel__body">
      <!-- CodeMirror -->
      <div class="cm-wrap" bind:this={container}></div>

      <!-- Annotations panel -->
      {#if showAnnotations && $selectionState}
        <div class="annot-panel">
          <div class="annot-panel__row">
            <span class="annot-panel__key">Type</span>
            <span class="annot-panel__val annot-panel__val--badge
              annot-panel__val--{$selectionState.selection_type}">
              {$selectionState.selection_type}
            </span>
          </div>
          <div class="annot-panel__row">
            <span class="annot-panel__key">Compact</span>
            <span class="annot-panel__val mono">{$selectionState.compact_display}</span>
          </div>
          <div class="annot-panel__row">
            <span class="annot-panel__key">DE</span>
            <span class="annot-panel__val serif">{$selectionState.human_de}</span>
          </div>
          <div class="annot-panel__row">
            <span class="annot-panel__key">FR</span>
            <span class="annot-panel__val serif">{$selectionState.human_fr}</span>
          </div>
          {#if $selectionState.hash_uri}
            <div class="annot-panel__row">
              <span class="annot-panel__key">Hash URI</span>
              <span class="annot-panel__val mono annot-panel__val--uri">
                {$selectionState.hash_uri}
              </span>
            </div>
          {/if}
          {#if $selectionState.slash_uri}
            <div class="annot-panel__row">
              <span class="annot-panel__key">Slash URI</span>
              <span class="annot-panel__val mono annot-panel__val--uri">
                {$selectionState.slash_uri}
              </span>
            </div>
          {/if}
          {#if $selectionState.errors?.length}
            <div class="annot-panel__row annot-panel__row--error">
              {$selectionState.errors.join('; ')}
            </div>
          {/if}
        </div>
      {/if}
    </div>
  {/if}
</div>

<style>
  .right-panel {
    width: 420px;
    min-width: 420px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    transition: width .2s, min-width .2s;
    background: #1c1b18;
  }
  .right-panel--collapsed { width: 32px; min-width: 32px; }

  .right-panel__header {
    height: 34px;
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 0 10px;
    background: #161512;
    border-bottom: 1px solid #2a2925;
    flex-shrink: 0;
  }
  .right-panel__title {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: .07em;
    text-transform: uppercase;
    color: #5a574f;
    white-space: nowrap;
  }
  .right-panel--collapsed .right-panel__title { display: none; }
  .right-panel--collapsed .right-panel__tabs  { display: none; }

  .right-panel__tabs { display: flex; gap: 2px; }
  .rp-tab {
    font-size: 11px;
    padding: 2px 8px;
    border-radius: var(--radius);
    color: #5a574f;
    transition: all .1s;
  }
  .rp-tab:hover { color: #b8b4aa; background: #2a2925; }
  .rp-tab--active { background: #2a2925; color: #d4d0c8; }

  .right-panel__toggle {
    margin-left: auto;
    font-size: 16px;
    color: #5a574f;
    padding: 0 2px;
    line-height: 1;
  }
  .right-panel__toggle:hover { color: #c8001e; }

  .right-panel__body {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  .cm-wrap {
    flex: 1;
    overflow: hidden;
    min-height: 0;
  }
  .cm-wrap :global(.cm-editor) { height: 100%; }
  .cm-wrap :global(.cm-scroller) { overflow: auto; }

  /* Annotation panel */
  .annot-panel {
    border-top: 1px solid #2a2925;
    background: #161512;
    padding: 8px 12px;
    flex-shrink: 0;
    max-height: 180px;
    overflow-y: auto;
  }
  .annot-panel__row {
    display: flex;
    align-items: baseline;
    gap: 10px;
    padding: 3px 0;
    border-bottom: 1px solid #1c1b18;
    font-size: 11px;
  }
  .annot-panel__row:last-child { border-bottom: none; }
  .annot-panel__row--error { color: #c8001e; font-family: var(--mono); }

  .annot-panel__key {
    font-size: 9px;
    font-weight: 600;
    letter-spacing: .06em;
    text-transform: uppercase;
    color: #5a574f;
    min-width: 56px;
    flex-shrink: 0;
  }
  .annot-panel__val {
    color: #d4d0c8;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .annot-panel__val.mono  { font-family: var(--mono); font-size: 11px; }
  .annot-panel__val.serif { font-family: var(--serif); }
  .annot-panel__val--uri  { color: #c8001e; font-size: 10px; }

  .annot-panel__val--badge {
    font-family: var(--mono);
    font-size: 9px;
    font-weight: 600;
    padding: 1px 5px;
    border-radius: 2px;
    text-transform: uppercase;
  }
  .annot-panel__val--single  { background: #1a4a2e; color: #6abf8a; }
  .annot-panel__val--range   { background: #1a2a4a; color: #6a90cf; }
  .annot-panel__val--multi   { background: #4a3a10; color: #c8a040; }
</style>
