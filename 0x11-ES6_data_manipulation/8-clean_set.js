export default function cleanSet(set, startString) {
  if (!startString) return '';
  if (typeof startString !== 'string') return '';
  const str = [];
  set.forEach((el) => {
    if (el.startsWith(startString)) {
      str.push(el.substr(startString.length));
    }
  });
  return str.join('-');
}
