export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  if (weakMap.has(endpoint)) {
    const n = weakMap.get(endpoint);
    if (n >= 5) {
      throw new Error('Endpoint load is high');
    } else {
      weakMap.set(endpoint, n + 1);
    }
  } else {
    weakMap.set(endpoint, 1);
  }
}
