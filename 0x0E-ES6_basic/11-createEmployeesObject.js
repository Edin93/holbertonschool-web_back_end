export default function createEmployeesObject(departmentName, employees) {
  const val = [];
  for (const i of employees) {
    val.push(i);
  }
  const obj = {
    [`${departmentName}`]: val,
  };

  return obj;
}
