#!/usr/bin/node

const ID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + ID;
const request = require('request');

request(url, (err, res, body) => {
  if (err) throw err;
  console.log(JSON.parse(body).title);
});
