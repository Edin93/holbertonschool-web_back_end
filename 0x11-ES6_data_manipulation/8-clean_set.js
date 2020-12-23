export default function cleanSet(set, startString) {
  if (!(startString && typeof startString === 'string')) {
    return '';
  }
  let str = '';
  let i = 0;
  set.forEach((el) => {
    i += 1;
    if (el.startsWith(startString)) {
      str += `${el.substring(startString.length)}`;
      if (i !== set.size - 1) {
        str += '-';
      }
    }
  });
  return str;
}
