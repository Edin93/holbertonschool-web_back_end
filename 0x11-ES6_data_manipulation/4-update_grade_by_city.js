export default function updateStudentGradeByCity(students, city, newGrades) {
  return (students.filter((student) => student.location === city)).map((student) => {
    const grade = newGrades.filter((currentStd) => currentStd.studentId === student.id);
    if (grade.length) {
      return { ...student, grade: grade[0].grade };
    }
    return { ...student, grade: 'N/A' };
  });
}
