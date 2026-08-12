<script>
  import { documentUrl, resolveUrl, loading, resolvedRef,
           aknXmlSource, citationLang, logOp } from './stores.js';

  let urlInput = '';
  let showHelp = false;

  async function onResolve() {
    if (!urlInput.trim()) return;
    documentUrl.set(urlInput.trim());
    const result = await resolveUrl(urlInput.trim(), { fetch: true });
    if (result) {
      // If there's XML we could load, set it; otherwise put a skeleton
      if (!$aknXmlSource) {
        const ptr = result.document_pointer?.preferred_id ?? '';
        aknXmlSource.set(buildSkeletonXml(result, ptr));
      }
    }
  }

  function buildSkeletonXml(ref, ptr) {
    const work = ref.uris?.work ?? '';
    const expr = ref.uris?.expression ?? '';
    const title = ref.metadata?.title_de ?? ptr;
    return `<?xml version="1.0" encoding="UTF-8"?>
<!-- ${title} | ${ptr} -->
<!-- Work:       ${work} -->
<!-- Expression: ${expr} -->
<akomaNtoso xmlns="http://docs.oasis-open.org/legaldocml/ns/akn/3.0">
  <act>
    <meta>
      <identification source="#editor">
        <FRBRWork>
          <FRBRuri value="${work}"/>
          <FRBRdate date="${ref.parsed_url?.date ?? ''}" name="Generation"/>
          <FRBRcountry value="${ref.parsed_url?.jurisdiction ?? 'ch'}"/>
        </FRBRWork>
        <FRBRExpression>
          <FRBRuri value="${expr}"/>
          <FRBRlanguage language="${ref.parsed_url?.lang === 'de' ? 'deu' : ref.parsed_url?.lang === 'fr' ? 'fra' : 'ita'}"/>
        </FRBRExpression>
      </identification>
    </meta>
    <body>
      <!-- Document loaded — use ↗ Link in the editor to annotate cross-references -->
      <article eId="art_1" num="1">
        <paragraph eId="art_1.para_1" num="1">
          <content><p>Start typing or paste AKN XML here.</p></content>
        </paragraph>
      </article>
    </body>
  </act>
</akomaNtoso>`;
  }

  function onKeydown(e) {
    if (e.key === 'Enter') onResolve();
  }

  // Sample URLs for quick load
  const SAMPLES = [
    { label: 'BV Art. 47', url: 'https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/de', article: '47', paragraph: '2' },
    { label: 'OR', url: 'https://www.fedlex.admin.ch/eli/cc/27/317_321_377/20220101/de' },
    { label: 'DSG', url: 'https://www.fedlex.admin.ch/eli/cc/2022/491/20230901/de' },
  ];

  async function loadSample(s) {
    urlInput = s.url;
    documentUrl.set(s.url);
    await resolveUrl(s.url, { article: s.article, paragraph: s.paragraph, fetch: true });
  }
</script>

<header class="toolbar">
  <!-- Logo mark -->
  <div class="toolbar__brand">
    <span class="toolbar__ch">CH</span>
    <span class="toolbar__akn">AKN</span>
  </div>

  <!-- URL input -->
  <div class="toolbar__url-group">
    <input
      class="toolbar__url"
      type="text"
      placeholder="https://www.fedlex.admin.ch/eli/cc/… or zhlex.zh.ch/Erlass…"
      bind:value={urlInput}
      on:keydown={onKeydown}
      spellcheck="false"
    />
    <button
      class="toolbar__resolve-btn"
      on:click={onResolve}
      disabled={$loading || !urlInput}
    >
      {$loading ? '…' : 'Resolve'}
    </button>
  </div>

  <!-- Samples -->
  <div class="toolbar__samples">
    {#each SAMPLES as s}
      <button class="toolbar__sample" on:click={() => loadSample(s)}>{s.label}</button>
    {/each}
  </div>

  <!-- Resolved info pill -->
  {#if $resolvedRef}
    <div class="toolbar__info">
      <span class="toolbar__ptr">{$resolvedRef.document_pointer?.preferred_id ?? ''}</span>
      {#if $resolvedRef.parsed_url?.jurisdiction !== 'ch'}
        <span class="toolbar__jid">{$resolvedRef.parsed_url?.jurisdiction}</span>
      {/if}
      {#if $resolvedRef.metadata?.sr_number}
        <span class="toolbar__sr">SR {$resolvedRef.metadata.sr_number}</span>
      {/if}
    </div>
  {/if}

  <!-- Help toggle -->
  <button class="toolbar__help" on:click={() => showHelp = !showHelp}
          class:toolbar__help--active={showHelp}
          title="Syntax reference">?</button>
</header>

<!-- Help overlay -->
{#if showHelp}
  <div class="help-overlay">
    <div class="help-overlay__inner">
      <button class="help-overlay__close" on:click={() => showHelp = false}>×</button>
      <h2>Fragment syntax reference</h2>
      <table class="help-table">
        <thead><tr><th>Input</th><th>Meaning</th><th>AKN eId</th></tr></thead>
        <tbody>
          <tr><td class="mono">#a47</td><td>Art. 47</td><td class="mono">art_47</td></tr>
          <tr><td class="mono">#a47-p2</td><td>Art. 47 Abs. 2</td><td class="mono">art_47.para_2</td></tr>
          <tr><td class="mono">#a47-p2-lit-a</td><td>Art. 47 Abs. 2 lit. a</td><td class="mono">art_47.para_2.lit_a</td></tr>
          <tr><td class="mono">#a1-p2-lit-c-sen-2</td><td>Art. 1 Abs. 2 lit. c Satz 2</td><td class="mono">art_1.para_2.lit_c.sen_2</td></tr>
          <tr><td class="mono">#a7~a18</td><td>Art. 7 – Art. 18 (range)</td><td class="mono">art_7→art_18</td></tr>
          <tr><td class="mono">#a7_p2~a8_p2</td><td>Art. 7 Abs. 2 – Art. 8 Abs. 2</td><td class="mono">portion</td></tr>
          <tr><td class="mono">#a7,a11,a28</td><td>Art. 7; Art. 11; Art. 28</td><td class="mono">multi</td></tr>
          <tr><td class="mono">#s3</td><td>Abschnitt 3</td><td class="mono">sec_3</td></tr>
          <tr><td class="mono">#chp-2</td><td>Kapitel 2</td><td class="mono">chp_2</td></tr>
          <tr><td class="mono">#anx-1</td><td>Anhang 1</td><td class="mono">anx_1</td></tr>
        </tbody>
      </table>
      <h3>Range endpoint syntax</h3>
      <p>Within a range <code>#start~end</code>, use <code>_</code> as level separator:
        <code>#a7_p2_lit-a~a28_sen-1</code></p>
      <h3>URI modes</h3>
      <ul>
        <li><code>#</code> Hash anchor — in-document navigation, browser links</li>
        <li><code>/</code> Slash path — REST resource, ELI subdivision GET</li>
        <li><code>~</code> Portion — AKN portion reference for ranges</li>
      </ul>
    </div>
  </div>
{/if}

<style>
  .toolbar {
    height: var(--toolbar-h);
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 0 14px;
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    flex-shrink: 0;
    z-index: 10;
  }

  .toolbar__brand {
    display: flex;
    flex-direction: column;
    align-items: center;
    line-height: 1;
    margin-right: 4px;
    flex-shrink: 0;
  }
  .toolbar__ch {
    font-family: var(--mono);
    font-size: 9px;
    font-weight: 600;
    letter-spacing: .1em;
    color: var(--accent);
  }
  .toolbar__akn {
    font-family: var(--mono);
    font-size: 13px;
    font-weight: 600;
    color: var(--text);
  }

  .toolbar__url-group {
    display: flex;
    align-items: center;
    gap: 6px;
    flex: 1;
    min-width: 0;
  }
  .toolbar__url {
    flex: 1;
    height: 32px;
    min-width: 0;
  }

  .toolbar__resolve-btn {
    height: 32px;
    padding: 0 16px;
    background: var(--accent);
    color: #fff;
    font-weight: 600;
    font-size: 13px;
    border-radius: var(--radius);
    transition: opacity .1s;
    flex-shrink: 0;
    font-family: var(--sans);
  }
  .toolbar__resolve-btn:hover:not(:disabled) { opacity: .88; }
  .toolbar__resolve-btn:disabled { opacity: .45; cursor: default; }

  .toolbar__samples {
    display: flex;
    gap: 4px;
    flex-shrink: 0;
  }
  .toolbar__sample {
    font-size: 11px;
    font-weight: 500;
    padding: 3px 8px;
    border: 1px solid var(--border);
    border-radius: var(--radius);
    color: var(--text-2);
    background: var(--surface-2);
    transition: all .1s;
  }
  .toolbar__sample:hover { border-color: var(--accent); color: var(--accent); }

  .toolbar__info {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 4px 10px;
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    flex-shrink: 0;
  }
  .toolbar__ptr {
    font-family: var(--mono);
    font-size: 12px;
    font-weight: 600;
    color: var(--accent);
  }
  .toolbar__jid, .toolbar__sr {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--text-3);
    background: var(--border);
    padding: 1px 5px;
    border-radius: 2px;
  }

  .toolbar__help {
    width: 28px; height: 28px;
    border-radius: 50%;
    border: 1px solid var(--border);
    font-size: 13px;
    font-weight: 600;
    color: var(--text-3);
    flex-shrink: 0;
    transition: all .1s;
  }
  .toolbar__help:hover, .toolbar__help--active {
    background: var(--accent);
    color: #fff;
    border-color: var(--accent);
  }

  /* Help overlay */
  .help-overlay {
    position: fixed;
    inset: 0;
    background: rgba(26,25,22,.6);
    z-index: 100;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .help-overlay__inner {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg, 6px);
    padding: 28px 32px;
    max-width: 600px;
    width: 90vw;
    max-height: 80vh;
    overflow-y: auto;
    position: relative;
    box-shadow: var(--shadow-lg, 0 8px 32px rgba(0,0,0,.18));
  }
  .help-overlay__close {
    position: absolute;
    top: 12px; right: 14px;
    font-size: 20px;
    color: var(--text-3);
  }
  .help-overlay__close:hover { color: var(--accent); }

  .help-overlay__inner h2 {
    font-family: var(--serif);
    font-size: 18px;
    font-weight: 400;
    margin-bottom: 16px;
    color: var(--text);
  }
  .help-overlay__inner h3 {
    font-size: 12px;
    font-weight: 600;
    letter-spacing: .05em;
    text-transform: uppercase;
    color: var(--text-3);
    margin: 16px 0 8px;
  }
  .help-overlay__inner p { font-size: 13px; color: var(--text-2); margin-bottom: 8px; }
  .help-overlay__inner ul { padding-left: 20px; }
  .help-overlay__inner li { font-size: 13px; color: var(--text-2); margin-bottom: 4px; }
  .help-overlay__inner code {
    font-family: var(--mono);
    font-size: 12px;
    background: var(--surface-2);
    padding: 1px 5px;
    border-radius: 2px;
    color: var(--accent);
  }

  .help-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 12px;
    margin-bottom: 16px;
  }
  .help-table th {
    text-align: left;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: .07em;
    text-transform: uppercase;
    color: var(--text-3);
    padding: 4px 8px;
    border-bottom: 1px solid var(--border);
  }
  .help-table td {
    padding: 5px 8px;
    border-bottom: 1px solid var(--surface-2);
    color: var(--text-2);
  }
  .help-table td.mono {
    font-family: var(--mono);
    color: var(--accent);
    font-size: 11px;
  }

  :global(.toolbar__help--active) { background: var(--accent); }
</style>
