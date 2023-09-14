#!/usr/bin/node

function dsort (dict) {
  const tmp = {};
  for (const key in dict) {
    if (tmp[dict[key]] === undefined) {
      tmp[dict[key]] = [key];
    } else {
      tmp[dict[key]].push(key);
    }
  }
  return (tmp);
}

const dict = require('./101-data.js').dict;

console.log(dsort(dict));
