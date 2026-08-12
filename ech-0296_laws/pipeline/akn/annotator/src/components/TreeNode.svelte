<script>
  import { selectedElement } from '../lib/stores.js';
  export let node;
  export let depth = 0;

  let expanded = depth < 2;

  $: isSelected = $selectedElement === node;
  $: hasChildren = node.children && node.children.length > 0;
  $: isTextOnly = !hasChildren && node.textContent?.trim();

  function getAttributes(node) {
    const attrs = [];
    if (node.attributes) {
      for (const attr of node.attributes) {
        attrs.push({ name: attr.name, value: attr.value });
      }
    }
    return attrs;
  }

  function toggle() {
    expanded = !expanded;
  }

  function select() {
    $selectedElement = node;
  }
</script>

<div class="tree-node" class:selected={isSelected} style="--depth: {depth}">
  <div class="node-header" on:click={select}>
    {#if hasChildren}
      <button class="toggle" on:click|stopPropagation={toggle}>
        {expanded ? '▼' : '▶'}
      </button>
    {:else}
      <span class="toggle-spacer"></span>
    {/if}

    <span class="tag">&lt;{node.localName}</span>
    {#each getAttributes(node) as attr}
      <span class="attr">
        <span class="attr-name">{attr.name}</span>=<span class="attr-value">"{attr.value}"</span>
      </span>
    {/each}
    <span class="tag">&gt;</span>

    {#if isTextOnly}
      <span class="text">{node.textContent.trim().slice(0, 60)}{node.textContent.trim().length > 60 ? '...' : ''}</span>
      <span class="tag">&lt;/{node.localName}&gt;</span>
    {/if}
  </div>

  {#if expanded && hasChildren}
    <div class="children">
      {#each Array.from(node.children) as child}
        <svelte:self node={child} depth={depth + 1} />
      {/each}
    </div>
    {#if !isTextOnly}
      <div class="closing-tag">
        <span class="tag">&lt;/{node.localName}&gt;</span>
      </div>
    {/if}
  {/if}
</div>

<style>
  .tree-node {
    font-family: 'SF Mono', Monaco, 'Consolas', monospace;
    font-size: 13px;
    line-height: 1.5;
  }

  .tree-node.selected > .node-header {
    background: #fff3cd;
  }

  .node-header {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 2px;
    padding: 2px 4px;
    padding-left: calc(var(--depth) * 20px);
    cursor: pointer;
    border-radius: 3px;
  }

  .node-header:hover {
    background: #f0f0f0;
  }

  .toggle {
    width: 16px;
    height: 16px;
    border: none;
    background: none;
    cursor: pointer;
    font-size: 10px;
    color: #666;
    padding: 0;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .toggle-spacer {
    width: 16px;
    display: inline-block;
  }

  .tag {
    color: #881280;
  }

  .attr {
    margin-left: 4px;
  }

  .attr-name {
    color: #994500;
  }

  .attr-value {
    color: #1a1aa6;
  }

  .text {
    color: #333;
    margin: 0 4px;
  }

  .children {
    border-left: 1px dashed #ddd;
    margin-left: calc(var(--depth) * 20px + 8px);
  }

  .closing-tag {
    padding-left: calc(var(--depth) * 20px);
    padding: 2px 4px;
    padding-left: calc(var(--depth) * 20px);
  }
</style>
