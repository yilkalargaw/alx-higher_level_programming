#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(h) || isNaN(h)) {
      w = {};
      h = {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
