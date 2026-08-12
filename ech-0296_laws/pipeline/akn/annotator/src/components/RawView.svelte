<script>
  import { xmlDoc } from '../lib/stores.js';
  import TreeNode from './TreeNode.svelte';

  $: rootElement = $xmlDoc?.documentElement;
</script>

<div class="raw-view">
  {#if rootElement}
    <TreeNode node={rootElement} />
  {:else}
    <p class="empty">No XML document loaded</p>
  {/if}
</div>

<style>
  .raw-view {
    font-family: 'SF Mono', Monaco, 'Consolas', monospace;
    font-size: 13px;
    line-height: 1.6;
  }

  .empty {
    color: #666;
    font-style: italic;
  }
</style>
