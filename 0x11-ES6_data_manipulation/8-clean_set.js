export default function cleanSet(set, startString) {
  let str = '';
  let len = 0;
  if (!startString.length) return '';
  set.forEach((el) => {
    if (el.startsWith(startString)) {
      str += `${el.substring(startString.length)}-`;
    }
  });
  len = str.length;
  return str.substring(0, len - 1);
}
