<script>
  import { currentDisplayUri, currentFragmentUri, currentHumanCitation,
           selectionState, resolvedRef, uriMode, citationLang,
           selectionRaw, resolveSelection } from './stores.js';

  let compactInput = '';
  let copied = false;
  let typingTimer;

  // Sync compact input from store (but don't overwrite while typing)
  let userTyping = false;
  $: if (!userTyping) {
    compactInput = $selectionState?.compact_display
      ?? $resolvedRef?.fragment?.compact
      ?? '';
  }

  function onCompactInput(e) {
    compactInput = e.target.value;
    userTyping = true;
    clearTimeout(typingTimer);
    typingTimer = setTimeout(async () => {
      if (compactInput.trim()) {
        selectionRaw.set(compactInput);
        await resolveSelection(compactInput);
      }
      userTyping = false;
    }, 300);
  }

  async function copyUri() {
    if (!$currentFragmentUri) return;
    await navigator.clipboard.writeText($currentFragmentUri);
    copied = true;
    setTimeout(() => copied = false, 1400);
  }

  const MODES = ['hash', 'slash', 'portion'];
  const MODE_LABELS = { hash: '#', slash: '/', portion: '~' };
</script>

<div class="refbar">
  <!-- Compact field -->
  <div class="refbar__group refbar__group--compact">
    <label class="refbar__label">Fragment</label>
    <input
      class="refbar__input refbar__input--compact"
      type="text"
      placeholder="#a47-p2-lit-a"
      value={compactInput}
      on:input={onCompactInput}
      spellcheck="false"
      title="Compact fragment — type or select in editor"
    />
  </div>

  <!-- Human citation -->
  <div class="refbar__group refbar__group--human">
    <label class="refbar__label">Citation</label>
    <span class="refbar__human" title={$currentHumanCitation}>
      {$currentHumanCitation || '—'}
    </span>
  </div>

  <!-- URI mode toggle -->
  <div class="refbar__group refbar__group--mode">
    {#each MODES as m}
      <button
        class="refbar__mode-btn"
        class:refbar__mode-btn--active={$uriMode === m}
        on:click={() => uriMode.set(m)}
        title={{ hash: 'Hash anchor (#)', slash: 'Slash path (/)', portion: 'AKN portion (~)' }[m]}
      >
        {MODE_LABELS[m]}
      </button>
    {/each}
  </div>

  <!-- Current URI field -->
  <div class="refbar__group refbar__group--uri">
    <label class="refbar__label">Current URL</label>
    <input
      class="refbar__input refbar__input--uri"
      type="text"
      readonly
      value={$currentDisplayUri}
      title={$currentFragmentUri}
      spellcheck="false"
    />
    <button
      class="refbar__copy"
      class:refbar__copy--done={copied}
      on:click={copyUri}
      title="Copy full URI"
    >
      {copied ? '✓' : '⎘'}
    </button>
  </div>

  <!-- Language toggle -->
  <div class="refbar__group refbar__group--lang">
    {#each ['de','fr','it'] as l}
      <button
        class="refbar__lang-btn"
        class:refbar__lang-btn--active={$citationLang === l}
        on:click={() => citationLang.set(l)}
      >{l.toUpperCase()}</button>
    {/each}
  </div>

  <!-- Selection type badge -->
  {#if $selectionState}
    <div class="refbar__badge refbar__badge--{$selectionState.selection_type}">
      {$selectionState.selection_type}
    </div>
  {/if}
</div>

<style>
  .refbar {
    height: var(--refbar-h);
    display: flex;
    align-items: center;
    gap: 1px;
    background: var(--surface);
    border-top: 1px solid var(--border);
    padding: 0 12px;
    flex-shrink: 0;
  }

  .refbar__group {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 0 10px;
    border-right: 1px solid var(--border);
    height: 100%;
  }
  .refbar__group:last-child { border-right: none; }

  .refbar__label {
    font-size: 10px;
    font-weight: 600;
    letter-spacing: .06em;
    text-transform: uppercase;
    color: var(--text-3);
    white-space: nowrap;
    user-select: none;
  }

  .refbar__input {
    height: 28px;
    background: var(--surface-2);
    border-color: var(--border);
  }
  .refbar__input--compact { width: 160px; }
  .refbar__input--uri     { width: 300px; color: var(--accent); cursor: default; }
  .refbar__input--uri:focus { border-color: var(--border); }

  .refbar__human {
    font-family: var(--serif);
    font-size: 14px;
    color: var(--text-2);
    max-width: 220px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .refbar__copy {
    font-size: 15px;
    padding: 0 4px;
    color: var(--text-3);
    transition: color .1s;
  }
  .refbar__copy:hover { color: var(--accent); }
  .refbar__copy--done { color: var(--ok) !important; }

  .refbar__mode-btn {
    font-family: var(--mono);
    font-size: 14px;
    font-weight: 600;
    padding: 2px 7px;
    border-radius: var(--radius);
    color: var(--text-3);
    transition: all .1s;
  }
  .refbar__mode-btn:hover { color: var(--text); background: var(--surface-2); }
  .refbar__mode-btn--active { background: var(--accent); color: #fff; }

  .refbar__lang-btn {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: .04em;
    padding: 2px 6px;
    border-radius: var(--radius);
    color: var(--text-3);
    transition: all .1s;
  }
  .refbar__lang-btn:hover { color: var(--text); background: var(--surface-2); }
  .refbar__lang-btn--active { background: var(--accent); color: #fff; }

  .refbar__badge {
    font-family: var(--mono);
    font-size: 10px;
    font-weight: 600;
    letter-spacing: .04em;
    text-transform: uppercase;
    padding: 2px 7px;
    border-radius: 2px;
    margin-left: 6px;
  }
  .refbar__badge--single  { background: var(--ok-dim);      color: var(--ok); }
  .refbar__badge--range   { background: var(--pending-dim); color: var(--pending); }
  .refbar__badge--multi   { background: var(--warn-dim);    color: var(--warn); }

  .refbar__group--mode,
  .refbar__group--lang { gap: 2px; }
</style>
