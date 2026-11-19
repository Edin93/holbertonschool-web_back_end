const getPaymentTokenFromAPI = require('./6-payment_token');
const chai = require('chai');

describe('getPaymentTokenFromAPI', function () {
  it('tests getPaymentTokenFromAPI(true)', function (done) {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        chai.expect(response).to.deep.equal({ data: 'Successful response from the API' });
        done();
      })
      .catch((error) => done(error));
  })
})
