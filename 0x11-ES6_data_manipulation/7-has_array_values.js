export default function hasValuesFromArray(set, arr) {
  for (let i = 0; i < arr.length; i += 1) {
    if (!set.has(arr[i])) {
      return false;
    }
  }
  return true;
}
