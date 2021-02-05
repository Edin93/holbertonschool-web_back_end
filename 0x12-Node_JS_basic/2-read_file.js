const fs = require('fs');

function countStudents(path) {
  fs.readFile(path,
    'utf-8',
    (error, results) => {
      if (error) {
        throw new Error('Cannot load the database');
      } else {
        const lines = results.split('\n');
        let i = 0;
        const fields = {};

        const getLines = () => {
          for (const line of lines) {
            if (line.trim() !== '' && i > 0) {
            const [fname, lname, age, field] = line.split(','); // eslint-disable-line
              if (!fields[field]) {
                fields[field] = {
                  count: 1,
                  students: [fname],
                };
              } else {
                const newCount = fields[field].count + 1;
                const newStudents = (fields[field].students).concat(fname);
                fields[field] = {
                  count: newCount,
                  students: newStudents,
                };
              }
            }
            i += 1;
          }
          if (i >= 1) {
            i -= 1;
          }
        };

        const display = async () => {
          getLines();
          console.log(`Number of students: ${i}`);
          for (const field of Object.keys(fields)) {
            const n = fields[field].count;
            const names = fields[field].students.join(', ');
            console.log(`Number of students in ${field}: ${n}. List: ${names}`);
          }
        };

        display();
      }
    });
}

module.exports = countStudents;
