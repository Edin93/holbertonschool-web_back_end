export default function cleanSet(set, startString) {
  if (!(startString && typeof startString === 'string')) {
    return '';
  }
  let str = '';
  let i = 0;
  for (const el of set) {
    if (el.startsWith(startString)) {
      str += `${el.substr(startString.length)}`;
      if (i !== set.size - 1) {
        str += '-';
      }
		}
		i += 1;
  }
  return str;
}
