export default function iterateThroughObject(reportWithIterator) {
  let msg = '';

  for (let i = 0; i < reportWithIterator.length; i += 1) {
    msg += `${reportWithIterator[i]}`;
    if (i + 1 !== reportWithIterator.length) {
      msg += ' | ';
    }
  }

  return msg;
}
