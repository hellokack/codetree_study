const fs=require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ");
let A = Number(input[0]);
let B = Number(input[1]);
let C = Number(input[2]);
let hap = A+B+C;
console.log((hap)+"\n"+(hap/3)+"\n"+(hap-(hap/3)));