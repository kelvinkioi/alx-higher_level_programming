#!/usr/bin/node

const request = require('request');
const comp = {};
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) throw err;

  JSON.parse(body).forEach(todo => {
    const id = todo.userId;
    if (!comp[id]) comp[id] = 0;
    if (todo.completed) comp[id]++;
    if (comp[id] === 0) delete comp[id];
  });
  console.log(comp);
});
