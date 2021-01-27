const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./5-payment');
const { assert, expect } = require('chai');

describe("sendPaymentRequestToApi", function() {
	let log;

	beforeEach(function () {
		log = sinon.spy(console, "log");
	});

	afterEach(function () {
		log.restore();
	});

	it("sendPaymentRequestToAPI with 100, and 20", () => {
		sendPaymentRequestToApi(100, 20);

		expect(log.calledWithExactly('The total is: 120')).to.be.true;
		expect(log.calledOnce).to.be.true;
	});

	it("sendPaymentRequestToAPI with 10, and 10", () => {
		sendPaymentRequestToApi(10, 10);

		expect(log.calledWithExactly('The total is: 20')).to.be.true;
		expect(log.calledOnce).to.be.true;
	});

});
