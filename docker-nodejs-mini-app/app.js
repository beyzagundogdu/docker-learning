const express = require('express');
const app = express();

app.get('/hello', (req, res) => {
  res.send('Merhaba, Node.js!');
});

app.listen(3000, () => {
  console.log('Uygulama 3000 portunda calisiyor.');
});
