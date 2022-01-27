//Variables
let fibonacciNumbers = [0, 1];
let answer = 0;

//Finds fibonacci numbers
for (i = 0; i < 4000000; i += 2) {

    //Finds value of next number
    let x = fibonacciNumbers[fibonacciNumbers.length - 2] + fibonacciNumbers[fibonacciNumbers.length - 1];

    //Adds number to the list
    if (x < 4000000) {
        fibonacciNumbers.push(x);

        //Gets sum of even fibonacci number
        if (x % 2 == 0) {
            answer += x;
        }
    }
}

//Displays answer
console.log(answer); //Expected 4613732