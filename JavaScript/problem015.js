//Variable
let answer = 0;
let twentyFactorial = 1;
let fourtyFactorial = 1;

//Number of possible paths
for (let i = 1; i <= 20; i++) {
    twentyFactorial *= i;
}

for (let j = 1; j <= 40; j++) {
    fourtyFactorial *= j;
}

let horizontal = twentyFactorial;
let vertical = twentyFactorial;
let end = fourtyFactorial;

//Counts answer (binomial coefficient)
answer = end / (horizontal * vertical);

//Displays answer
console.log(answer); //Expected 137846528820