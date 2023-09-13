#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let n = 0; n < this.width; n++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }

  rotate () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
    temp = 0;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
