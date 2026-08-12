// src/stores.js
// tags: svelte, state, akn
//
// Central state management for the AKN-CH pipeline editor.
// All stores are writable or derived — no global mutable objects.
//
// Store hierarchy:
//   documentUrl      → triggers API call → resolvedRef
//   selectionRaw     → triggers API call → selectionState
//   resolvedRef + selectionState → currentDisplayUri (derived)
//   operations       → append-only log of backend interactions

import { writable, derived, get } from 'svelte/store';

// ── Document ──────────────────────────────────────────────────────────────────

/** The raw URL pasted into the toolbar */
export const documentUrl = writable('');

/** Resolved FRBR reference from /resolve API */
export const resolvedRef = writable(null);

/** Page metadata from /resolve?fetch=true */
export const fetchedMeta = writable(null);

/** Whether the API is loading */
export const loading = writable(false);

/** API base URL — configurable for local dev vs Docker */
export const API_BASE = writable('http://localhost:8787');

// ── Editor ────────────────────────────────────────────────────────────────────

/** ProseMirror doc as JSON (serialised, not the EditorState object) */
export const docJson = writable(null);

/** CodeMirror AKN XML source */
export const aknXmlSource = writable('');

/** Active language for human citations */
export const citationLang = writable('de');

/** URI display mode: 'hash' | 'slash' | 'portion' */
export const uriMode = writable('hash');

// ── Selection ─────────────────────────────────────────────────────────────────

/**
 * Raw selection string as set by the ProseMirror plugin.
 * Formats:
 *   single:  '#a47-p2-lit-a'
 *   range:   '#a7~a18'
 *   multi:   '#a7,a11,a28'
 *   empty:   ''
 */
export const selectionRaw = writable('');

/**
 * Resolved SelectionState from /selection API.
 * { compact_display, human_de, human_fr, hash_uri, slash_uri, ... }
 */
export const selectionState = writable(null);

/**
 * The "current URL" field — the primary live display in the UI.
 * Shows: pointer#compact  e.g.  bv#a47-p2-lit-a
 */
export const currentDisplayUri = derived(
  [resolvedRef, selectionState, uriMode],
  ([$ref, $sel, $mode]) => {
    if (!$ref) return '';
    const ptr = $ref.document_pointer?.akn_pointer ?? '';

    if ($sel?.compact_display) {
      const compact = $sel.compact_display;  // '#a47-p2-lit-a'
      if ($mode === 'slash' && $sel.slash_uri) return $sel.slash_uri;
      return `${ptr}${compact}`;
    }
    return $ref.uris?.display_uri ?? ptr;
  }
);

/** Full fragment URI (AKN expression + fragment) */
export const currentFragmentUri = derived(
  [resolvedRef, selectionState, uriMode],
  ([$ref, $sel, $mode]) => {
    if (!$ref) return '';
    if ($sel) {
      if ($mode === 'slash') return $sel.slash_uri ?? '';
      return $sel.hash_uri ?? '';
    }
    return $ref.uris?.fragment_uri ?? $ref.uris?.expression ?? '';
  }
);

/** Human-readable citation in active language */
export const currentHumanCitation = derived(
  [resolvedRef, selectionState, citationLang],
  ([$ref, $sel, $lang]) => {
    if ($sel?.human_de && $lang === 'de') return $sel.human_de;
    if ($sel?.human_fr && $lang === 'fr') return $sel.human_fr;
    if ($ref) {
      const ptr = $ref.document_pointer?.preferred_id ?? '';
      const frag = $lang === 'fr'
        ? $ref.fragment?.human_fr
        : $ref.fragment?.human_de;
      return frag ? `${ptr} ${frag}` : ptr;
    }
    return '';
  }
);

// ── Operations log ────────────────────────────────────────────────────────────

/**
 * Append-only log of backend operations.
 * Each entry: { id, ts, type, status, input, output, detail? }
 */
export const operations = writable([]);

export function logOp(op) {
  operations.update(ops => [
    {
      id: Math.random().toString(36).slice(2),
      ts: new Date().toISOString(),
      status: 'ok',
      output: '',
      ...op,
    },
    ...ops,
  ].slice(0, 200));
}

// ── API helpers ───────────────────────────────────────────────────────────────

/**
 * Resolve a Fedlex/ZH-Lex URL via the /resolve API.
 * Updates resolvedRef, fetchedMeta, and the operations log.
 */
export async function resolveUrl(url, opts = {}) {
  const base = get(API_BASE);
  loading.set(true);
  logOp({ type: 'url-resolve', input: url, status: 'pending' });
  try {
    const params = new URLSearchParams({ url, lang: get(citationLang), ...opts });
    const res = await fetch(`${base}/resolve?${params}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    resolvedRef.set(data);
    if (data.metadata) fetchedMeta.set(data.metadata);
    logOp({
      type: 'url-resolve',
      input: url,
      output: data.uris?.display_uri ?? '',
      status: 'ok',
    });
    return data;
  } catch (e) {
    logOp({ type: 'url-resolve', input: url, status: 'error', detail: e.message });
    return null;
  } finally {
    loading.set(false);
  }
}

/**
 * Resolve a selection string via /selection API.
 * Updates selectionState and the operations log.
 */
export async function resolveSelection(raw) {
  if (!raw) { selectionState.set(null); return; }
  const base = get(API_BASE);
  const $ref  = get(resolvedRef);
  try {
    const res = await fetch(`${base}/selection`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        raw,
        base_expression_uri: $ref?.uris?.expression ?? '',
        document_pointer:    $ref?.document_pointer?.preferred_id ?? '',
        lang:                get(citationLang),
      }),
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    selectionState.set(data);
    logOp({
      type: 'selection',
      input: raw,
      output: data.compact_display,
      status: data.errors?.length ? 'error' : 'ok',
    });
    return data;
  } catch (e) {
    logOp({ type: 'selection', input: raw, status: 'error', detail: e.message });
    return null;
  }
}

/**
 * Parse a fragment string via /fragment/parse API.
 * Used when user types directly into the compact field.
 */
export async function parseFragment(q) {
  const base = get(API_BASE);
  try {
    const res = await fetch(`${base}/fragment/parse?q=${encodeURIComponent(q)}`);
    if (!res.ok) return null;
    const data = await res.json();
    logOp({ type: 'fragment-parse', input: q, output: data.eid, status: 'ok' });
    return data;
  } catch (e) {
    logOp({ type: 'fragment-parse', input: q, status: 'error', detail: e.message });
    return null;
  }
}
