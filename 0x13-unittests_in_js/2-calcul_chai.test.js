const calculateNumber = require("./2-calcul_chai");
const chai = require('chai');
const except = chai.expect;

describe("calculateNumber", () => {
	except(4).to.equal(calculateNumber('SUM', 1, 3));
	except(5).to.equal(calculateNumber('SUM', 1.8, 3));
	except(5).to.equal(calculateNumber('SUM', 1.8, 3.2));
	except(4).to.equal(calculateNumber('SUM', 1, 3.2));
	except(5).to.equal(calculateNumber('SUM', 1, 3.7));
	except(5).to.equal(calculateNumber('SUM', 1.2, 3.7));
	except(6).to.equal(calculateNumber('SUM', 1.5, 3.7));

	except(2).to.equal(calculateNumber('SUBTRACT', 3, 1));
	except(2).to.equal(calculateNumber('SUBTRACT', 3.1, 1.2));
	except(1).to.equal(calculateNumber('SUBTRACT', 3, 1.8));
	except(1).to.equal(calculateNumber('SUBTRACT', 3.2, 1.8));
	except(3).to.equal(calculateNumber('SUBTRACT', 3.9, 0.9));
	except(6).to.equal(calculateNumber('SUBTRACT', 5.8, 0));
	except(-3).to.equal(calculateNumber('SUBTRACT', 1.2, 3.7));

	except(3).to.equal(calculateNumber('DIVIDE', 9, 3.2));
	except(3).to.equal(calculateNumber('DIVIDE', 12, 3.8));
	except(3).to.equal(calculateNumber('DIVIDE', 11.9, 3.7));
	except(4).to.equal(calculateNumber('DIVIDE', 16.1, 3.6));
	except(4).to.equal(calculateNumber('DIVIDE', 8.25, 2));
	except('Error').to.equal(calculateNumber('DIVIDE', 9, 0.2));
});
