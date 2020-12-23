export default function cleanSet(set, startString) {
  if (typeof startString !== 'string') return '';
  if (startString.length === 0) return '';
  if (typeof set !== 'object') return '';

  const str = [];

  set.forEach((el) => {
    if (el && el.startsWith(startString)) {
      str.push(el.substr(startString.length));
    }
  });

  return str.join('-');
}
