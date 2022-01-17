//Variables
let sum = 0;
let squares = 0;
let answer;

//Adds numbers from 1 to 100 together
for (i = 1; i <= 100; i++) {
    sum += i;//Adds numbers together
    squares += i ** 2; //Adds square of numbers together
}

//Finds square of sum
sum = sum ** 2;

//Gets final answer
answer = sum - squares;

//Displays answers
console.log(answer); //Expected 25164150