export default function cleanSet(set, startString) {
	if (!(startString && typeof startString === 'string')) {
		return '';
	}
  let str = '';
  let len = 0;
  set.forEach((el) => {
    if (el.startsWith(startString)) {
      str += `${el.substring(startString.length)}-`;
    }
  });
  len = str.length;
  return str.substring(0, len - 1);
}
