export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    }
    if (typeof length !== 'number') {
      throw TypeError('Length must be a number');
    }
    students.forEach((student) => {
      if (typeof student !== 'string') {
        throw TypeError('Students must be an array of strings');
      }
    });
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
    students.forEach((student) => {
      if (typeof student !== 'string') {
        throw TypeError('Students must be an array of strings');
      }
    });
    this._students = students;
  }

  get students() {
    return this._students;
  }
}
