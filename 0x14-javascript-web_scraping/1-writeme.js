#!/usr/bin/node

const myfile = process.argv[2];
const text = process.argv[3];
const fs = require('fs');

fs.writeFile(myfile, text, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
