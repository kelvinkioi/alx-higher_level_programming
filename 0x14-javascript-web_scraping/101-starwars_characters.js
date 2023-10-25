#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
request(url, function (err, response, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    printChar(characters, 0);
  }
});

function printChar (characters, index) {
  request(characters[index], function (err, response, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printChar(characters, index + 1);
      }
    }
  });
}
