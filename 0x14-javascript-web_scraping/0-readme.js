#!/usr/bin/node

const myfile = process.argv[2];
const fs = require('fs');

fs.readFile(myfile, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
