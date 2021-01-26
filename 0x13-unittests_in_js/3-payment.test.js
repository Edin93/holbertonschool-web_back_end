const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');
const { assert } = require('chai');

describe("sendPaymentRequestToApi", function() {
	// assert.equal(5, Utils.calculateNumber('SUM', 3.1, 1.9));

	sinon.spy(Utils, "calculateNumber");
	Utils.calculateNumber('SUM', 100, 20);

	let spyCall = Utils.calculateNumber.getCall(0);
	assert.equal(spyCall.returnValue, sendPaymentRequestToApi(100, 20));
});
