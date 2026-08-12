<script>
  import { xmlDoc, xmlText, documentUrl, loading, error, currentView } from './lib/stores.js';
  import SideNav from './components/SideNav.svelte';
  import RawView from './components/RawView.svelte';
  import MetaView from './components/MetaView.svelte';
  import HtmlView from './components/HtmlView.svelte';

  let urlInput = '';

  async function fetchXml() {
    if (!urlInput.trim()) return;

    $loading = true;
    $error = '';

    try {
      // Use CORS proxy for cross-origin requests
      const proxyUrl = `https://corsproxy.io/?${encodeURIComponent(urlInput)}`;
      const response = await fetch(proxyUrl);

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }

      const text = await response.text();
      const parser = new DOMParser();
      const doc = parser.parseFromString(text, 'application/xml');

      const parseError = doc.querySelector('parsererror');
      if (parseError) {
        throw new Error('Invalid XML: ' + parseError.textContent);
      }

      $xmlText = text;
      $xmlDoc = doc;
      $documentUrl = urlInput;
    } catch (err) {
      $error = err.message;
    } finally {
      $loading = false;
    }
  }

  function handleFileUpload(event) {
    const file = event.target.files[0];
    if (!file) return;

    $loading = true;
    $error = '';

    const reader = new FileReader();
    reader.onload = (e) => {
      try {
        const text = e.target.result;
        const parser = new DOMParser();
        const doc = parser.parseFromString(text, 'application/xml');

        const parseError = doc.querySelector('parsererror');
        if (parseError) {
          throw new Error('Invalid XML: ' + parseError.textContent);
        }

        $xmlText = text;
        $xmlDoc = doc;
        $documentUrl = file.name;
      } catch (err) {
        $error = err.message;
      } finally {
        $loading = false;
      }
    };
    reader.onerror = () => {
      $error = 'Failed to read file';
      $loading = false;
    };
    reader.readAsText(file);
  }

  function handleKeydown(event) {
    if (event.key === 'Enter') {
      fetchXml();
    }
  }
</script>

<main>
  <header>
    <h1>AKN Annotator</h1>
    <div class="url-bar">
      <input
        type="text"
        bind:value={urlInput}
        placeholder="Enter AKN XML URL..."
        on:keydown={handleKeydown}
      />
      <button on:click={fetchXml} disabled={$loading}>
        {$loading ? 'Loading...' : 'Fetch'}
      </button>
      <label class="file-upload">
        <input type="file" accept=".xml" on:change={handleFileUpload} />
        Upload
      </label>
    </div>
    {#if $error}
      <div class="error">{$error}</div>
    {/if}
  </header>

  {#if $xmlDoc}
    <div class="container">
      <SideNav />
      <div class="content">
        <div class="view-tabs">
          <button
            class:active={$currentView === 'raw'}
            on:click={() => $currentView = 'raw'}
          >.raw</button>
          <button
            class:active={$currentView === 'meta'}
            on:click={() => $currentView = 'meta'}
          >.meta</button>
          <button
            class:active={$currentView === 'html'}
            on:click={() => $currentView = 'html'}
          >.html</button>
        </div>
        <div class="view-content">
          {#if $currentView === 'raw'}
            <RawView />
          {:else if $currentView === 'meta'}
            <MetaView />
          {:else}
            <HtmlView />
          {/if}
        </div>
      </div>
    </div>
  {:else}
    <div class="empty-state">
      <p>Enter a URL or upload an AKN XML file to get started</p>
    </div>
  {/if}
</main>

<style>
  :global(body) {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: #f5f5f5;
  }

  main {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }

  header {
    background: #1a1a2e;
    color: white;
    padding: 16px 24px;
  }

  h1 {
    margin: 0 0 16px 0;
    font-size: 1.5rem;
  }

  .url-bar {
    display: flex;
    gap: 8px;
  }

  .url-bar input[type="text"] {
    flex: 1;
    padding: 10px 14px;
    border: none;
    border-radius: 6px;
    font-size: 14px;
  }

  .url-bar button, .file-upload {
    padding: 10px 20px;
    background: #4a4a6a;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 14px;
  }

  .url-bar button:hover, .file-upload:hover {
    background: #5a5a7a;
  }

  .url-bar button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }

  .file-upload {
    display: inline-flex;
    align-items: center;
  }

  .file-upload input {
    display: none;
  }

  .error {
    margin-top: 12px;
    padding: 10px 14px;
    background: #ff5252;
    border-radius: 6px;
    font-size: 14px;
  }

  .container {
    flex: 1;
    display: flex;
    overflow: hidden;
  }

  .content {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  .view-tabs {
    display: flex;
    background: #e0e0e0;
    padding: 8px 16px 0;
    gap: 4px;
  }

  .view-tabs button {
    padding: 8px 16px;
    border: none;
    background: #d0d0d0;
    color: #666;
    border-radius: 6px 6px 0 0;
    cursor: pointer;
    font-family: monospace;
    font-size: 14px;
  }

  .view-tabs button.active {
    background: white;
    color: #333;
  }

  .view-content {
    flex: 1;
    background: white;
    overflow: auto;
    padding: 16px;
  }

  .empty-state {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #666;
  }
</style>
