const fs = require("fs");
input=fs.readFileSync(0).toString().trim().split(" ")
let A=Number(input[0]);
let B=Number(input[1]);
console.log(A,B,A+B)