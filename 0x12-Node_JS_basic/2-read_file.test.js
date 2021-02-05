const { ShouldThrow, expect } = require('chai');
const sinon = require('sinon');

const countStudents = require('./2-read_file.js');

describe('countStudents', () => {
  let consoleSpy;

  beforeEach(() => {
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    consoleSpy.restore();
  });

  it('logs to the console the right messages', () => {
    countStudents('./database.csv');

    expect(consoleSpy.calledWith('Number of students: 10')).to.be.true;
    expect(consoleSpy.calledWith('Number of students in CS: 6. List: Johenn, Arielle, Jonathen, Emmenuel, Guillaume, Katie')).to.be.true;
    expect(consoleSpy.calledWith('Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy')).to.be.true;
  });
});
