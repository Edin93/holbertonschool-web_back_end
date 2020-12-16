export default function guardrail(mathFunction) {
  const queue = [];
  let result = null;

  try {
    result = mathFunction();
  } catch (e) {
    result = e;
  }

  queue.push(result);
  queue.push('Guardrail was processed');
  return queue;
}
