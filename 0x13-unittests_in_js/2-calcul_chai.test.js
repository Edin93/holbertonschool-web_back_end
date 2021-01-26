const calculateNumber = require("./2-calcul_chai");
let chai = require('chai');
let expect = chai.expect;

describe("calculateNumber", () => {
	expect(4).to.equal(calculateNumber('SUM', 1, 3));
	expect(5).to.equal(calculateNumber('SUM', 1.8, 3));
	expect(5).to.equal(calculateNumber('SUM', 1.8, 3.2));
	expect(4).to.equal(calculateNumber('SUM', 1, 3.2));
	expect(5).to.equal(calculateNumber('SUM', 1, 3.7));
	expect(5).to.equal(calculateNumber('SUM', 1.2, 3.7));
	expect(6).to.equal(calculateNumber('SUM', 1.5, 3.7));

	expect(2).to.equal(calculateNumber('SUBTRACT', 3, 1));
	expect(2).to.equal(calculateNumber('SUBTRACT', 3.1, 1.2));
	expect(1).to.equal(calculateNumber('SUBTRACT', 3, 1.8));
	expect(1).to.equal(calculateNumber('SUBTRACT', 3.2, 1.8));
	expect(3).to.equal(calculateNumber('SUBTRACT', 3.9, 0.9));
	expect(6).to.equal(calculateNumber('SUBTRACT', 5.8, 0));
	expect(-3).to.equal(calculateNumber('SUBTRACT', 1.2, 3.7));

	expect(3).to.equal(calculateNumber('DIVIDE', 9, 3.2));
	expect(3).to.equal(calculateNumber('DIVIDE', 12, 3.8));
	expect(3).to.equal(calculateNumber('DIVIDE', 11.9, 3.7));
	expect(4).to.equal(calculateNumber('DIVIDE', 16.1, 3.6));
	expect(4).to.equal(calculateNumber('DIVIDE', 8.25, 2));
	expect('Error').to.equal(calculateNumber('DIVIDE', 9, 0.2));
});
