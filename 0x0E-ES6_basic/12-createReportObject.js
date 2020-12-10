export default function createReportObject (employeesList) {
  const allEmployees = {};
  for (const [k, v] of Object.entries(employeesList)) {
    allEmployees[`${k}`] = v;
  }
  const result = {
    allEmployees: allEmployees,
    getNumberOfDepartments: (employeesList) => { return Object.keys(employeesList).length; }
  };

  return result;
}
