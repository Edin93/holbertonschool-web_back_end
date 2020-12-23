export default function cleanSet(set, startString) {
  let str = '';
  if (startString === '') return '';
  set.forEach((el) => {
    if (el.startsWith(startString)) {
      str += `${el.substring(startString.length)}-`;
    }
  });
  return str.substr(0, str.length - 1);
}
