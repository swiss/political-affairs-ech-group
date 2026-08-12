<script>
  import './app.css';
  import Toolbar       from './Toolbar.svelte';
  import LeftPanel     from './LeftPanel.svelte';
  import RightPanel    from './RightPanel.svelte';
  import ReferenceBar  from './ReferenceBar.svelte';
  import OperationsLog from './OperationsLog.svelte';
</script>

<div id="app">
  <Toolbar />
  <div class="main-row">
    <LeftPanel />
    <RightPanel />
    <OperationsLog />
  </div>
  <ReferenceBar />
</div>

<style>
  :global(#app) {
    height: 100vh;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }
  .main-row {
    flex: 1;
    display: flex;
    overflow: hidden;
    min-height: 0;
  }
</style>
