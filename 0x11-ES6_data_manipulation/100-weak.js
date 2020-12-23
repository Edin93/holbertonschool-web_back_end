export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  if (weakMap.has(endpoint)) {
    const n = weakMap.get(endpoint);
    weakMap.set(endpoint, n + 1);
    if (n >= 5) {
      throw Error('Endpoint load is high');
    }
  } else {
    weakMap.set(endpoint, 1);
  }
}
