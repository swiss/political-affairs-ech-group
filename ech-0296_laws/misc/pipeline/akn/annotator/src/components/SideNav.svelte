<script>
  import { xmlDoc, filters, currentView, selectedElement, FRBR_ELEMENTS, FRBR_COLORS, AKN_NS } from '../lib/stores.js';

  $: frbrData = $xmlDoc ? extractFrbrData($xmlDoc) : null;
  $: preambleData = $xmlDoc ? extractPreambleData($xmlDoc) : null;
  $: bodyData = $xmlDoc ? extractBodyData($xmlDoc) : null;

  function extractFrbrData(doc) {
    const data = { work: [], expression: [], manifestation: [] };

    for (const level of ['work', 'expression', 'manifestation']) {
      const levelElem = doc.getElementsByTagNameNS(AKN_NS, 'FRBR' + level.charAt(0).toUpperCase() + level.slice(1))[0];
      if (!levelElem) continue;

      for (const elemName of FRBR_ELEMENTS[level]) {
        const elems = levelElem.getElementsByTagNameNS(AKN_NS, elemName);
        for (const elem of elems) {
          const value = elem.getAttribute('value') || elem.getAttribute('name') || elem.getAttribute('href') || elem.textContent;
          data[level].push({ name: elemName, value, element: elem });
        }
      }
    }
    return data;
  }

  function extractPreambleData(doc) {
    const items = [];
    const preamble = doc.getElementsByTagNameNS(AKN_NS, 'preamble')[0];
    const preface = doc.getElementsByTagNameNS(AKN_NS, 'preface')[0];

    function extractChildren(parent, depth = 0) {
      if (!parent) return;
      for (const child of parent.children) {
        const localName = child.localName;
        if (localName) {
          const eId = child.getAttribute('eId') || '';
          const text = child.textContent?.trim().slice(0, 50) || '';
          items.push({ name: localName, eId, text, depth, element: child });
          if (child.children.length > 0 && depth < 2) {
            extractChildren(child, depth + 1);
          }
        }
      }
    }

    if (preface) {
      items.push({ name: 'preface', eId: preface.getAttribute('eId') || '', text: '', depth: 0, element: preface });
      extractChildren(preface, 1);
    }
    if (preamble) {
      items.push({ name: 'preamble', eId: preamble.getAttribute('eId') || '', text: '', depth: 0, element: preamble });
      extractChildren(preamble, 1);
    }

    return items;
  }

  function extractBodyData(doc) {
    const items = [];
    const body = doc.getElementsByTagNameNS(AKN_NS, 'body')[0];
    if (!body) return items;

    function traverse(elem, depth = 0) {
      const localName = elem.localName;
      if (['chapter', 'section', 'article', 'paragraph', 'subparagraph', 'point', 'indent', 'list', 'item'].includes(localName)) {
        const eId = elem.getAttribute('eId') || '';
        const numElem = elem.getElementsByTagNameNS(AKN_NS, 'num')[0];
        const headingElem = elem.getElementsByTagNameNS(AKN_NS, 'heading')[0];
        const num = numElem?.textContent || '';
        const heading = headingElem?.textContent || '';
        items.push({ name: localName, eId, num, heading, depth, element: elem });
      }
      for (const child of elem.children) {
        traverse(child, depth + (localName === 'body' ? 0 : 1));
      }
    }

    traverse(body);
    return items;
  }

  function toggleFilter(key) {
    $filters = { ...$filters, [key]: !$filters[key] };
  }

  function selectElement(elem, view) {
    $selectedElement = elem;
    $currentView = view;
  }

  function getColor(name) {
    return FRBR_COLORS[name] || '#666';
  }
</script>

<nav class="side-nav">
  <section class="filters">
    <h3>Filters</h3>
    <div class="filter-toggles">
      <label class:dimmed={!$filters.work}>
        <input type="checkbox" bind:checked={$filters.work} />
        Work
      </label>
      <label class:dimmed={!$filters.expression}>
        <input type="checkbox" bind:checked={$filters.expression} />
        Expression
      </label>
      <label class:dimmed={!$filters.manifestation}>
        <input type="checkbox" bind:checked={$filters.manifestation} />
        Manifestation
      </label>
    </div>
    <div class="filter-toggles sub">
      <label class:dimmed={!$filters.showNumber}>
        <input type="checkbox" bind:checked={$filters.showNumber} />
        FRBRnumber
      </label>
      <label class:dimmed={!$filters.showName}>
        <input type="checkbox" bind:checked={$filters.showName} />
        FRBRname
      </label>
    </div>
  </section>

  {#if frbrData}
    <section class="frbr-elements">
      <h3>FRBR Elements</h3>
      {#each ['work', 'expression', 'manifestation'] as level}
        {#if $filters[level]}
          <div class="level-section">
            <h4>{level.charAt(0).toUpperCase() + level.slice(1)}</h4>
            {#each frbrData[level] as item}
              {#if (item.name !== 'FRBRnumber' || $filters.showNumber) && (item.name !== 'FRBRname' || $filters.showName)}
                <button
                  class="frbr-item"
                  style="--color: {getColor(item.name)}"
                  on:click={() => selectElement(item.element, 'meta')}
                >
                  <span class="tag">&lt;{item.name}&gt;</span>
                  <span class="value">{item.value?.slice(0, 40)}{item.value?.length > 40 ? '...' : ''}</span>
                </button>
              {/if}
            {/each}
          </div>
        {/if}
      {/each}
    </section>
  {/if}

  {#if preambleData && preambleData.length > 0}
    <section class="preamble-section">
      <h3>Preface / Preamble</h3>
      {#each preambleData as item}
        <button
          class="preamble-item"
          style="padding-left: {12 + item.depth * 16}px"
          on:click={() => selectElement(item.element, 'html')}
        >
          <span class="tag">&lt;{item.name}&gt;</span>
          {#if item.text}
            <span class="preview">{item.text}</span>
          {/if}
        </button>
      {/each}
    </section>
  {/if}

  {#if bodyData && bodyData.length > 0}
    <section class="body-section">
      <h3>Body Structure</h3>
      {#each bodyData as item}
        <button
          class="body-item"
          style="padding-left: {12 + Math.min(item.depth, 4) * 12}px"
          on:click={() => selectElement(item.element, 'html')}
        >
          <span class="type">{item.name}</span>
          {#if item.num}
            <span class="num">{item.num}</span>
          {/if}
          {#if item.heading}
            <span class="heading">{item.heading.slice(0, 30)}{item.heading.length > 30 ? '...' : ''}</span>
          {/if}
          {#if item.eId}
            <span class="eid">{item.eId}</span>
          {/if}
        </button>
      {/each}
    </section>
  {/if}
</nav>

<style>
  .side-nav {
    width: 320px;
    background: #fafafa;
    border-right: 1px solid #e0e0e0;
    overflow-y: auto;
    padding: 16px;
  }

  section {
    margin-bottom: 24px;
  }

  h3 {
    margin: 0 0 12px 0;
    font-size: 13px;
    font-weight: 600;
    color: #333;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  h4 {
    margin: 8px 0 4px 0;
    font-size: 12px;
    color: #666;
    font-weight: 500;
  }

  .filter-toggles {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .filter-toggles.sub {
    margin-top: 12px;
    padding-top: 12px;
    border-top: 1px solid #e0e0e0;
  }

  .filter-toggles label {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
    cursor: pointer;
  }

  .filter-toggles label.dimmed {
    color: #999;
  }

  .frbr-item, .preamble-item, .body-item {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 6px;
    width: 100%;
    padding: 6px 12px;
    border: none;
    background: none;
    text-align: left;
    cursor: pointer;
    font-size: 12px;
    border-radius: 4px;
  }

  .frbr-item:hover, .preamble-item:hover, .body-item:hover {
    background: #e8e8e8;
  }

  .frbr-item .tag {
    color: var(--color);
    font-family: monospace;
    font-weight: 500;
  }

  .frbr-item .value {
    color: #666;
    font-size: 11px;
  }

  .preamble-item .tag {
    color: #1565c0;
    font-family: monospace;
    font-size: 11px;
  }

  .preamble-item .preview {
    color: #888;
    font-size: 11px;
    font-style: italic;
  }

  .body-item .type {
    color: #7b1fa2;
    font-weight: 500;
  }

  .body-item .num {
    color: #333;
    font-weight: 600;
  }

  .body-item .heading {
    color: #666;
    font-size: 11px;
  }

  .body-item .eid {
    color: #999;
    font-family: monospace;
    font-size: 10px;
  }
</style>
