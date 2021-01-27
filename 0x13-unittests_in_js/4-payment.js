const Utils = require('./utils');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
	let sum = Utils.calculateNumber('SUM', totalAmount, totalShipping);
	console.log(`The total is: ${sum}`);
}

module.exports = sendPaymentRequestToApi;
