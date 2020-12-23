export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  let count = weakMap.get(endpoint);

  if (count) {
    weakMap.set(endpoint, weakMap.get(endpoint) + 1);
  } else {
    weakMap.set(endpoint, 1);
  }

  count = weakMap.get(endpoint);

  if (count >= 5) {
    throw Error('Endpoint load is high');
  }
}
