<script>
  import { xmlDoc, selectedElement, AKN_NS } from '../lib/stores.js';
  import { afterUpdate } from 'svelte';

  $: preface = $xmlDoc ? extractSection($xmlDoc, 'preface') : null;
  $: preamble = $xmlDoc ? extractSection($xmlDoc, 'preamble') : null;
  $: body = $xmlDoc ? extractBody($xmlDoc) : null;

  function extractSection(doc, name) {
    const elem = doc.getElementsByTagNameNS(AKN_NS, name)[0];
    if (!elem) return null;
    return renderElement(elem);
  }

  function extractBody(doc) {
    const bodyElem = doc.getElementsByTagNameNS(AKN_NS, 'body')[0];
    if (!bodyElem) return null;
    return renderBodyContent(bodyElem);
  }

  function renderElement(elem, depth = 0) {
    const localName = elem.localName;
    const eId = elem.getAttribute('eId') || '';
    const children = [];

    for (const child of elem.children) {
      children.push(renderElement(child, depth + 1));
    }

    let text = '';
    if (children.length === 0) {
      text = elem.textContent?.trim() || '';
    }

    return { localName, eId, text, children, element: elem };
  }

  function renderBodyContent(bodyElem) {
    const items = [];

    function traverse(elem) {
      const localName = elem.localName;
      const eId = elem.getAttribute('eId') || '';

      if (['chapter', 'section', 'article'].includes(localName)) {
        const numElem = elem.getElementsByTagNameNS(AKN_NS, 'num')[0];
        const headingElem = elem.getElementsByTagNameNS(AKN_NS, 'heading')[0];
        const contentElems = [];

        for (const child of elem.children) {
          if (!['num', 'heading'].includes(child.localName)) {
            contentElems.push(renderContentElement(child));
          }
        }

        items.push({
          type: localName,
          eId,
          num: numElem?.textContent || '',
          heading: headingElem?.textContent || '',
          content: contentElems,
          element: elem
        });
      }

      for (const child of elem.children) {
        traverse(child);
      }
    }

    traverse(bodyElem);
    return items;
  }

  function renderContentElement(elem) {
    const localName = elem.localName;
    const eId = elem.getAttribute('eId') || '';

    if (localName === 'paragraph' || localName === 'subparagraph') {
      const numElem = elem.getElementsByTagNameNS(AKN_NS, 'num')[0];
      const contentElem = elem.getElementsByTagNameNS(AKN_NS, 'content')[0];
      const introElem = elem.getElementsByTagNameNS(AKN_NS, 'intro')[0];
      const listElem = elem.getElementsByTagNameNS(AKN_NS, 'list')[0];

      let text = '';
      if (contentElem) {
        text = contentElem.textContent?.trim() || '';
      } else if (introElem) {
        text = introElem.textContent?.trim() || '';
      }

      const listItems = [];
      if (listElem) {
        for (const item of listElem.children) {
          if (item.localName === 'point' || item.localName === 'item') {
            const itemNum = item.getElementsByTagNameNS(AKN_NS, 'num')[0];
            const itemContent = item.getElementsByTagNameNS(AKN_NS, 'content')[0];
            listItems.push({
              num: itemNum?.textContent || '',
              text: itemContent?.textContent?.trim() || ''
            });
          }
        }
      }

      return {
        type: localName,
        eId,
        num: numElem?.textContent || '',
        text,
        listItems,
        element: elem
      };
    }

    return {
      type: localName,
      eId,
      text: elem.textContent?.trim() || '',
      element: elem
    };
  }

  function isSelected(elem) {
    return $selectedElement === elem;
  }

  afterUpdate(() => {
    if ($selectedElement) {
      const el = document.querySelector('.html-section.selected, .body-item.selected, .paragraph.selected');
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }
  });
</script>

<div class="html-view">
  {#if preface}
    <section class="html-section preface" class:selected={isSelected(preface.element)}>
      <h2>Preface</h2>
      <div class="section-content">
        {#each preface.children as child}
          <div class="preface-element" class:selected={isSelected(child.element)}>
            {#if child.localName === 'longTitle'}
              <h3 class="long-title">{child.text || ''}</h3>
            {:else if child.text}
              <p class="{child.localName}">{child.text}</p>
            {/if}
          </div>
        {/each}
      </div>
    </section>
  {/if}

  {#if preamble}
    <section class="html-section preamble" class:selected={isSelected(preamble.element)}>
      <h2>Preamble</h2>
      <div class="section-content">
        {#each preamble.children as child}
          <div class="preamble-element" class:selected={isSelected(child.element)}>
            {#if child.text}
              <p class="{child.localName}">{child.text}</p>
            {/if}
            {#each child.children as subchild}
              {#if subchild.text}
                <p class="{subchild.localName}">{subchild.text}</p>
              {/if}
            {/each}
          </div>
        {/each}
      </div>
    </section>
  {/if}

  {#if body && body.length > 0}
    <section class="html-section body">
      <h2>Body</h2>
      {#each body as item}
        <div class="body-item {item.type}" class:selected={isSelected(item.element)}>
          <div class="item-header">
            {#if item.type === 'chapter'}
              <h3>{item.num} {item.heading}</h3>
            {:else if item.type === 'section'}
              <h4>{item.num} {item.heading}</h4>
            {:else if item.type === 'article'}
              <h5>
                <span class="art-num">{item.num}</span>
                {#if item.heading}
                  <span class="art-heading">{item.heading}</span>
                {/if}
              </h5>
            {/if}
          </div>

          {#each item.content as para}
            <div class="paragraph {para.type}" class:selected={isSelected(para.element)}>
              {#if para.num}
                <span class="para-num">{para.num}</span>
              {/if}
              <div class="para-content">
                {#if para.text}
                  <p>{para.text}</p>
                {/if}
                {#if para.listItems && para.listItems.length > 0}
                  <ul class="list-items">
                    {#each para.listItems as li}
                      <li><span class="li-num">{li.num}</span> {li.text}</li>
                    {/each}
                  </ul>
                {/if}
              </div>
            </div>
          {/each}
        </div>
      {/each}
    </section>
  {/if}

  {#if !preface && !preamble && (!body || body.length === 0)}
    <p class="empty">No content to display</p>
  {/if}
</div>

<style>
  .html-view {
    max-width: 800px;
    line-height: 1.6;
  }

  .html-section {
    margin-bottom: 32px;
    padding: 20px;
    background: #fafafa;
    border-radius: 8px;
  }

  .html-section.selected {
    background: #fff3cd;
  }

  h2 {
    margin: 0 0 16px 0;
    font-size: 16px;
    color: #666;
    text-transform: uppercase;
    letter-spacing: 1px;
  }

  .preface h3.long-title {
    font-size: 20px;
    color: #1a1a2e;
    margin: 0 0 12px 0;
  }

  .preamble-element, .preface-element {
    margin-bottom: 8px;
  }

  .preamble-element.selected, .preface-element.selected {
    background: #fff3cd;
    padding: 4px 8px;
    border-radius: 4px;
  }

  .body-item {
    margin-bottom: 24px;
    padding: 16px;
    background: white;
    border-radius: 6px;
    border-left: 3px solid #e0e0e0;
  }

  .body-item.selected {
    background: #fff3cd;
  }

  .body-item.chapter {
    border-left-color: #1565c0;
  }

  .body-item.section {
    border-left-color: #7b1fa2;
  }

  .body-item.article {
    border-left-color: #2e7d32;
  }

  .item-header h3 {
    margin: 0;
    font-size: 18px;
    color: #1565c0;
  }

  .item-header h4 {
    margin: 0;
    font-size: 16px;
    color: #7b1fa2;
  }

  .item-header h5 {
    margin: 0;
    font-size: 14px;
    display: flex;
    gap: 8px;
  }

  .art-num {
    color: #2e7d32;
    font-weight: 600;
  }

  .art-heading {
    color: #333;
    font-weight: 500;
  }

  .paragraph {
    display: flex;
    gap: 12px;
    margin-top: 12px;
    padding: 8px;
    border-radius: 4px;
  }

  .paragraph.selected {
    background: #fff3cd;
  }

  .para-num {
    font-weight: 600;
    color: #666;
    min-width: 24px;
  }

  .para-content {
    flex: 1;
  }

  .para-content p {
    margin: 0;
  }

  .list-items {
    margin: 8px 0 0 0;
    padding-left: 0;
    list-style: none;
  }

  .list-items li {
    margin: 4px 0;
  }

  .li-num {
    font-weight: 500;
    color: #666;
    margin-right: 4px;
  }

  .empty {
    color: #666;
    font-style: italic;
  }
</style>
