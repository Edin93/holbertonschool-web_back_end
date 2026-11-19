const express = require('express')
const port = 7865

const app = express()

app.get('/', (req, res) => {
  res.send('Welcome to the payment system')
})

app.get('/cart/:id(\\d+)', (req, res) => {
  res.status(200).send(`Payment methods for cart ${req.params.id}`)
})

app.get('/available_payments', (req, res) => {
  res.status(200).send({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  })
})

app.use(express.json())
app.post('/login', (req, res) => {
  const username = req.body.userName
  res.status(200).send(`Welcome ${username}`)
})

app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
})

module.exports = app
