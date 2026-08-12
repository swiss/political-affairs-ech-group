<script>
  import { xmlDoc, filters, selectedElement, FRBR_ELEMENTS, FRBR_COLORS, AKN_NS } from '../lib/stores.js';
  import { onMount, afterUpdate } from 'svelte';

  $: identification = $xmlDoc ? extractIdentification($xmlDoc) : null;
  $: references = $xmlDoc ? extractReferences($xmlDoc) : [];

  function extractIdentification(doc) {
    const data = { work: [], expression: [], manifestation: [] };

    for (const level of ['work', 'expression', 'manifestation']) {
      const levelElem = doc.getElementsByTagNameNS(AKN_NS, 'FRBR' + level.charAt(0).toUpperCase() + level.slice(1))[0];
      if (!levelElem) continue;

      const seen = new Set();
      for (const elemName of FRBR_ELEMENTS[level]) {
        const elems = levelElem.getElementsByTagNameNS(AKN_NS, elemName);
        for (const elem of elems) {
          const value = elem.getAttribute('value') || elem.getAttribute('name') || elem.getAttribute('href') || elem.textContent;
          const key = `${elemName}:${value}`;
          if (!seen.has(key)) {
            seen.add(key);
            data[level].push({
              name: elemName,
              value,
              date: elem.getAttribute('date') || '',
              element: elem
            });
          }
        }
      }
    }
    return data;
  }

  function extractReferences(doc) {
    const refs = [];
    const references = doc.getElementsByTagNameNS(AKN_NS, 'references')[0];
    if (!references) return refs;

    for (const child of references.children) {
      refs.push({
        type: child.localName,
        eId: child.getAttribute('eId') || '',
        href: child.getAttribute('href') || '',
        showAs: child.getAttribute('showAs') || '',
        element: child
      });
    }
    return refs;
  }

  function getColor(name) {
    return FRBR_COLORS[name] || '#666';
  }

  function isSelected(elem) {
    return $selectedElement === elem;
  }

  afterUpdate(() => {
    if ($selectedElement) {
      const el = document.querySelector('.meta-row.selected');
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }
  });
</script>

<div class="meta-view">
  {#if identification}
    <section class="identification">
      <h2>Identification</h2>

      {#each ['work', 'expression', 'manifestation'] as level}
        <div class="level-table" class:dimmed={!$filters[level]}>
          <h3>{level.charAt(0).toUpperCase() + level.slice(1)}</h3>
          <table>
            <tbody>
              {#each identification[level] as item}
                {#if (item.name !== 'FRBRnumber' || $filters.showNumber) && (item.name !== 'FRBRname' || $filters.showName)}
                  <tr class="meta-row" class:selected={isSelected(item.element)}>
                    <td class="element-name" style="color: {getColor(item.name)}">&lt;{item.name}&gt;</td>
                    <td class="element-value">
                      {item.value}
                      {#if item.date}
                        <span class="date">({item.date})</span>
                      {/if}
                    </td>
                  </tr>
                {/if}
              {/each}
            </tbody>
          </table>
        </div>
      {/each}
    </section>

    {#if references.length > 0}
      <section class="references dimmed">
        <h2>References</h2>
        <table>
          <thead>
            <tr>
              <th>Type</th>
              <th>eId</th>
              <th>showAs</th>
              <th>href</th>
            </tr>
          </thead>
          <tbody>
            {#each references as ref}
              <tr class="meta-row" class:selected={isSelected(ref.element)}>
                <td class="ref-type">{ref.type}</td>
                <td class="ref-eid">{ref.eId}</td>
                <td class="ref-showas">{ref.showAs}</td>
                <td class="ref-href">{ref.href}</td>
              </tr>
            {/each}
          </tbody>
        </table>
      </section>
    {/if}
  {:else}
    <p class="empty">No metadata available</p>
  {/if}
</div>

<style>
  .meta-view {
    max-width: 900px;
  }

  section {
    margin-bottom: 32px;
  }

  h2 {
    margin: 0 0 16px 0;
    font-size: 18px;
    color: #333;
    border-bottom: 2px solid #1a1a2e;
    padding-bottom: 8px;
  }

  h3 {
    margin: 16px 0 8px 0;
    font-size: 14px;
    color: #666;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .level-table {
    margin-bottom: 16px;
  }

  .level-table.dimmed {
    opacity: 0.4;
  }

  table {
    width: 100%;
    border-collapse: collapse;
  }

  th, td {
    padding: 8px 12px;
    text-align: left;
    border-bottom: 1px solid #e0e0e0;
  }

  th {
    background: #f5f5f5;
    font-weight: 500;
    font-size: 12px;
    color: #666;
    text-transform: uppercase;
  }

  .meta-row.selected {
    background: #fff3cd;
  }

  .element-name {
    font-family: monospace;
    font-size: 13px;
    font-weight: 500;
    white-space: nowrap;
  }

  .element-value {
    font-size: 13px;
    color: #333;
    word-break: break-all;
  }

  .date {
    color: #666;
    font-size: 12px;
    margin-left: 8px;
  }

  .references {
    opacity: 0.6;
  }

  .references.dimmed {
    opacity: 0.4;
  }

  .ref-type {
    font-family: monospace;
    color: #7b1fa2;
  }

  .ref-eid {
    font-family: monospace;
    font-size: 12px;
  }

  .ref-showas {
    color: #333;
  }

  .ref-href {
    font-size: 11px;
    color: #666;
    word-break: break-all;
  }

  .empty {
    color: #666;
    font-style: italic;
  }
</style>
