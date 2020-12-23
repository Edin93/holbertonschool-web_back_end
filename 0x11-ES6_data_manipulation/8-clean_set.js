export default function cleanSet(set, startString) {
	if (typeof startString !== 'string') return '';
	if (startString.length === 0) return '';
  if (!(set instanceof Set)) return '';
  const str = [];
  set.forEach((el) => {
    if (el.startsWith(startString)) {
      str.push(el.substr(startString.length));
    }
  });
  return str.join('-');
}
