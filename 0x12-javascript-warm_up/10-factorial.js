#!/usr/bin/node
function factorial(x) {
	if (x < 0) {
		return 1;
	}
	var result = 1;
	while (x > 1) {
		result *= x;
		x--;
	}
	return result;
}

console.log(factorial(Number(process.argv[2])));
