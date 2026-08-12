<script>
  import { operations } from './stores.js';

  // Type labels and colors
  const TYPE_META = {
    'url-resolve':    { label: 'RESOLVE',  color: 'pending' },
    'selection':      { label: 'SELECT',   color: 'ok' },
    'fragment-parse': { label: 'FRAGMENT', color: 'ok' },
    'fetch-metadata': { label: 'FETCH',    color: 'pending' },
    'annotation':     { label: 'ANNOT',    color: 'warn' },
    'xml-export':     { label: 'EXPORT',   color: 'ok' },
    'xml-edit':       { label: 'EDIT',     color: 'ok' },
  };

  function meta(type) {
    return TYPE_META[type] ?? { label: type.toUpperCase(), color: 'ok' };
  }

  function fmtTime(iso) {
    return iso.slice(11, 19);
  }

  let collapsed = false;
</script>

<aside class="ops-log" class:ops-log--collapsed={collapsed}>
  <div class="ops-log__header">
    <span class="ops-log__title">Operations</span>
    <span class="ops-log__count">{$operations.length}</span>
    <button class="ops-log__toggle" on:click={() => collapsed = !collapsed}
            title={collapsed ? 'Expand' : 'Collapse'}>
      {collapsed ? '›' : '‹'}
    </button>
  </div>

  {#if !collapsed}
    <div class="ops-log__list">
      {#if $operations.length === 0}
        <div class="ops-log__empty">No operations yet</div>
      {/if}
      {#each $operations as op (op.id)}
        <div class="ops-log__item ops-log__item--{op.status}">
          <div class="ops-log__item-top">
            <span class="op-badge op-badge--{meta(op.type).color}">
              {meta(op.type).label}
            </span>
            <span class="ops-log__time">{fmtTime(op.ts)}</span>
            {#if op.status !== 'ok'}
              <span class="op-badge op-badge--{op.status === 'error' ? 'error' : 'warn'}">
                {op.status}
              </span>
            {/if}
          </div>
          {#if op.input}
            <div class="ops-log__io">
              <span class="ops-log__arrow">›</span>
              <span class="ops-log__val ops-log__val--in">{op.input}</span>
            </div>
          {/if}
          {#if op.output}
            <div class="ops-log__io">
              <span class="ops-log__arrow">←</span>
              <span class="ops-log__val ops-log__val--out">{op.output}</span>
            </div>
          {/if}
          {#if op.detail}
            <div class="ops-log__detail">{op.detail}</div>
          {/if}
        </div>
      {/each}
    </div>
  {/if}
</aside>

<style>
  .ops-log {
    width: 260px;
    min-width: 260px;
    border-left: 1px solid var(--border);
    background: var(--surface);
    display: flex;
    flex-direction: column;
    overflow: hidden;
    transition: width .2s, min-width .2s;
  }
  .ops-log--collapsed {
    width: 36px;
    min-width: 36px;
  }

  .ops-log__header {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 0 10px;
    height: 36px;
    border-bottom: 1px solid var(--border);
    background: var(--surface-2);
    flex-shrink: 0;
  }
  .ops-log__title {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: .07em;
    text-transform: uppercase;
    color: var(--text-3);
    white-space: nowrap;
  }
  .ops-log--collapsed .ops-log__title { display: none; }
  .ops-log__count {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--text-3);
    margin-left: auto;
  }
  .ops-log--collapsed .ops-log__count { display: none; }
  .ops-log__toggle {
    font-size: 16px;
    color: var(--text-3);
    padding: 0 2px;
    line-height: 1;
  }
  .ops-log__toggle:hover { color: var(--accent); }

  .ops-log__list {
    overflow-y: auto;
    flex: 1;
    padding: 6px 0;
  }
  .ops-log__empty {
    padding: 12px;
    font-size: 12px;
    color: var(--text-3);
    text-align: center;
  }

  .ops-log__item {
    padding: 6px 10px;
    border-bottom: 1px solid var(--surface-2);
    font-size: 11px;
  }
  .ops-log__item--error { background: var(--error-dim); }

  .ops-log__item-top {
    display: flex;
    align-items: center;
    gap: 5px;
    margin-bottom: 3px;
  }
  .ops-log__time {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--text-3);
    margin-left: auto;
  }

  .ops-log__io {
    display: flex;
    align-items: baseline;
    gap: 4px;
    overflow: hidden;
  }
  .ops-log__arrow {
    color: var(--text-3);
    flex-shrink: 0;
    font-size: 10px;
  }
  .ops-log__val {
    font-family: var(--mono);
    font-size: 10px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .ops-log__val--in  { color: var(--text-2); }
  .ops-log__val--out { color: var(--ok); }

  .ops-log__detail {
    font-size: 10px;
    color: var(--error);
    margin-top: 2px;
    word-break: break-all;
  }

  .op-badge {
    display: inline-block;
    font-family: var(--mono);
    font-size: 9px;
    padding: 1px 4px;
    border-radius: 2px;
    font-weight: 600;
    letter-spacing: .04em;
    text-transform: uppercase;
    flex-shrink: 0;
  }
  .op-badge--ok      { background: var(--ok-dim);      color: var(--ok); }
  .op-badge--error   { background: var(--error-dim);   color: var(--error); }
  .op-badge--pending { background: var(--pending-dim); color: var(--pending); }
  .op-badge--warn    { background: var(--warn-dim);    color: var(--warn); }
</style>
