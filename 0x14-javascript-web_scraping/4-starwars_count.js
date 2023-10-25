#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) return;
  console.log(body.split('people/18/').length - 1);
});
