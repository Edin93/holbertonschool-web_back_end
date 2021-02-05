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
  
  it('throws the correct error message', () => {
    expect(() => countStudents('./blabl.csv')).to.throw('Cannot load the database');
  });
});