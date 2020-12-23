export default function cleanSet(set, startString) {
  if (!(startString && typeof startString === 'string')) {
    return '';
  }
  const str = [];
  for (const el of set) {
    if (el.startsWith(startString)) {
      str.push(el.substr(startString.length));
    }
  }
  return str.join('-');
}
