const express = require('express');
const countStudents = require('./3-read_file_async');

const DB = process.argv[2];
const port = 1245;
const app = express();
module.exports = app;

app.get('/', (req, res) => {
  res.setHeader('content-type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.setHeader('content-type', 'text/plain');
  res.write('This is the list of our students\n');
  countStudents(DB).then((result) => {
    res.end(result.join('\n'));
  }).catch((error) => {
    res.end(`${error.message}`);
  });
});

app.listen(port);
