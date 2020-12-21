export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    } else {
      this._name = name;
    }
  }

  set length(length) {
    if (typeof length !== 'number') {
      throw TypeError('Length must be a number');
    } else {
      this._length = length;
    }
  }

  get length() {
    return this._length;
  }

  set students(students) {
    let areValidStudents = true;
    for (let i = 0; i < students.length; i += 1) {
      if (typeof students[i] !== 'string') {
        areValidStudents = false;
        break;
      }
    }
    if (!areValidStudents) {
      throw TypeError('Students array must be a strings');
    } else {
      this._students = students;
    }
  }

  get students() {
    return this._students;
  }
}