const request = require('request')
const chai = require('chai');

describe('Server Integration tests', function () {
  it('should return right string at endpoint GET /', function (done) {
    request('http://localhost:7865', (error, response, body) => {
      chai.expect(response.statusCode).to.equal(200)
      chai.expect(body).to.equal('Welcome to the payment system')
      if (error) return done(error)
      done()
    })
  })
});
