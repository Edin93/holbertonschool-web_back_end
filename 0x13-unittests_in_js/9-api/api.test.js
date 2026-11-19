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

  it('should work as expected for endpoint GET /cart/:id with ID as number', function (done) {
    const numberId = 10;

    request(`http://localhost:7865/cart/${numberId}`, (error, response, body) => {
      chai.expect(response.statusCode).to.equal(200)
      chai.expect(body).to.equal(`Payment methods for cart ${numberId}`)
      if (error) return done(error)
      done()
    })
  })

  it('should work as expected for endpoint GET /cart/:id with non valid ID number', function (done) {
    const notNumberId = 'Hello'

    request(`http://localhost:7865/cart/${notNumberId}`, (error, response, body) => {
      chai.expect(response.statusCode).to.equal(404)
      if (error) return done(error)
      done()
    })
  })
})
