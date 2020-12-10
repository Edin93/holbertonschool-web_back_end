export default function createIteratorObject(report) {
  let allEmployees = [];

  for (const value of Object.values(report.allEmployees)) {
    allEmployees = [
      ...allEmployees,
      ...value,
    ];
  }

  return allEmployees;
}
