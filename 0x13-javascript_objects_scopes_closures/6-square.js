#!/usr/bin/node
const Sq = require('./5-square');

module.exports = class Square extends Sq {
  charPrint (c) {
    if (!c) c = 'X';
    for (let i = 0; i < this.width; i++) {
      for (let n = 0; n < this.height; n++) {
        process.stdout.write(c);
      }
      console.log();
    }
  }
};
