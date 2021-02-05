const chai = require('chai');
const chaiHttp = require('chai-http');

process.argv[2] = './blabla.csv';
const app = require('./5-http');

chai.use(chaiHttp);
chai.should();

describe('More complex HTTP server using node', () => {
  describe('When the database is not available', () => {
    before(() => {
      process.argv[2] = './blabla.csv';
    })
    it('Returns the right error message', (done) => {
      chai.request(app)
        .get('/students')
        .end((error, response) => {
          chai.expect(response.text).to.equal(`This is the list of our students
Cannot load the database`);
          done();
        });
    });
  });
});
