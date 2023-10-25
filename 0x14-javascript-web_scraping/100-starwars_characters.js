#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, (err, res, body) => {
  if (err) return;

  JSON.parse(body).characters.forEach(character => {
    request(character, (err, res, body) => {
      if (!err) console.log(JSON.parse(body).name);
    });
  });
});
