const calculateNumber = require("./0-calcul");
const assert = require('assert');

describe("calculateNumber", () => {
	assert.equal(4, calculateNumber(1, 3))
	assert.equal(5, calculateNumber(1.8, 3));
	assert.equal(5, calculateNumber(1.8, 3.2));
	assert.equal(4, calculateNumber(1, 3.2));
	assert.equal(5, calculateNumber(1, 3.7));
	assert.equal(5, calculateNumber(1.2, 3.7));
	assert.equal(6, calculateNumber(1.5, 3.7));
});
