#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const myfile = process.argv[3];

request(url, (err, res, body) => {
  if (err) throw err;

  fs.writeFile(myfile, body, 'utf8', (err) => {
    if (err) throw err;
  });
});
