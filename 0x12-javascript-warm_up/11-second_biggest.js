#!/usr/bin/node
let args = process.argv.slice(2);
console.log(args.length <= 1 ? 0 : args.sort((a, b) => b - a)[1]);
