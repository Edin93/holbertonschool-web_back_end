export default function guardrail(mathFunction) {
  const queue = [];
  let result = null;

  try {
    result = mathFunction();
  } catch (e) {
    result = `${e.name}: ${e.message}`;
  }

  queue.push(result);
  queue.push('Guardrail was processed');
  return queue;
}
