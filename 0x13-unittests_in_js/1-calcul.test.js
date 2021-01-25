const calculateNumber = require("./1-calcul");
const assert = require('assert');

describe("calculateNumber", () => {
	assert.equal(4, calculateNumber('SUM', 1, 3))
	assert.equal(5, calculateNumber('SUM', 1.8, 3));
	assert.equal(5, calculateNumber('SUM', 1.8, 3.2));
	assert.equal(4, calculateNumber('SUM', 1, 3.2));
	assert.equal(5, calculateNumber('SUM', 1, 3.7));
	assert.equal(5, calculateNumber('SUM', 1.2, 3.7));
	assert.equal(6, calculateNumber('SUM', 1.5, 3.7));

	assert.equal(2, calculateNumber('SUBTRACT', 3, 1));
	assert.equal(2, calculateNumber('SUBTRACT', 3.1, 1.2));
	assert.equal(1, calculateNumber('SUBTRACT', 3, 1.8));
	assert.equal(1, calculateNumber('SUBTRACT', 3.2, 1.8));
	assert.equal(3, calculateNumber('SUBTRACT', 3.9, 0.9));
	assert.equal(6, calculateNumber('SUBTRACT', 5.8, 0));
	assert.equal(-3, calculateNumber('SUBTRACT', 1.2, 3.7));

	assert.equal(3, calculateNumber('DIVIDE', 9, 3.2));
	assert.equal(3, calculateNumber('DIVIDE', 12, 3.8));
	assert.equal(3, calculateNumber('DIVIDE', 11.9, 3.7));
	assert.equal(4, calculateNumber('DIVIDE', 16.1, 3.6));
	assert.equal(4, calculateNumber('DIVIDE', 8.25, 2));
	assert.equal('Error', calculateNumber('DIVIDE', 9, 0.2));
});
