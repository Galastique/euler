//Variables
let sum = 0;
let squares = 0;

//Finds sum and sum of squares
for (i = 1; i <= 100; i++) {
    sum += i;
    squares += i**2;
}

//Finds square of sum
sum = sum ** 2;

//Displays answers
console.log(sum - squares); //Expected 25164150