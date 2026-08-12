import { writable, derived } from 'svelte/store';

// XML document state
export const xmlDoc = writable(null);
export const xmlText = writable('');
export const documentUrl = writable('');
export const loading = writable(false);
export const error = writable('');

// View state
export const currentView = writable('raw'); // 'raw', 'meta', 'html'

// Filter state
export const filters = writable({
  work: true,
  expression: true,
  manifestation: true,
  showNumber: true,
  showName: true,
});

// Selection state
export const selectedElement = writable(null);
export const highlightedElements = writable([]);

// FRBR element definitions
export const FRBR_ELEMENTS = {
  work: ['FRBRthis', 'FRBRuri', 'FRBRdate', 'FRBRauthor', 'FRBRcountry', 'FRBRnumber', 'FRBRname', 'FRBRauthoritative', 'FRBRsubtype'],
  expression: ['FRBRthis', 'FRBRuri', 'FRBRdate', 'FRBRauthor', 'FRBRlanguage'],
  manifestation: ['FRBRthis', 'FRBRuri', 'FRBRdate', 'FRBRauthor', 'FRBRformat'],
};

export const FRBR_COLORS = {
  FRBRthis: '#1565c0',
  FRBRuri: '#1976d2',
  FRBRdate: '#2e7d32',
  FRBRauthor: '#7b1fa2',
  FRBRcountry: '#0288d1',
  FRBRnumber: '#e65100',
  FRBRname: '#c2185b',
  FRBRlanguage: '#00838f',
  FRBRformat: '#5d4037',
  FRBRauthoritative: '#616161',
  FRBRsubtype: '#455a64',
};

// AKN namespace
export const AKN_NS = 'http://docs.oasis-open.org/legaldocml/ns/akn/3.0';

// Helper to query with namespace
export function queryAkn(doc, xpath) {
  const nsResolver = (prefix) => prefix === 'akn' ? AKN_NS : null;
  const result = doc.evaluate(
    xpath,
    doc,
    nsResolver,
    XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
    null
  );
  const nodes = [];
  for (let i = 0; i < result.snapshotLength; i++) {
    nodes.push(result.snapshotItem(i));
  }
  return nodes;
}

// Get single element
export function queryAknSingle(doc, xpath) {
  const nodes = queryAkn(doc, xpath);
  return nodes.length > 0 ? nodes[0] : null;
}
