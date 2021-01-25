const assert = require("assert");
const calculateNumber = require("./1-calcul.js");

describe('calculateNumber', () => {
  describe('when type is SUBTRACT', () => {
    it('it round the first argument', () => {
        assert.equal(calculateNumber('SUBTRACT', 1.0, 0), 1);
        assert.equal(calculateNumber('SUBTRACT', 1.3, 0), 1);
        assert.equal(calculateNumber('SUBTRACT', 1.7, 0), 2);
    });
    
    it('it round the second argument', () => {
        assert.equal(calculateNumber('SUBTRACT', 0, 1.0), -1);
        assert.equal(calculateNumber('SUBTRACT', 0, 1.3), -1);
        assert.equal(calculateNumber('SUBTRACT', 0, 1.7), -2);
    });
    
    it('it should return the right number', () => {
        assert.equal(calculateNumber('SUBTRACT', 1.3, 0), 1);
        assert.equal(calculateNumber('SUBTRACT', 0, 1.2), -1);
        assert.equal(calculateNumber('SUBTRACT', 1.3, 1.3), 0);
        assert.equal(calculateNumber('SUBTRACT', 1.7, 1.2), 1);
        assert.equal(calculateNumber('SUBTRACT', 1.3, 1.8), -1);
        assert.equal(calculateNumber('SUBTRACT', 1.6, 1.8), 0);
    });
  });
});