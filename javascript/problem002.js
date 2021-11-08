//Variables
var fibonacciNumbers = [0, 1];
var answer = 0;

//Loop
for (i = 0; i < 4000000; i += 2) {

    //Finds value of next number
    var x = fibonacciNumbers[fibonacciNumbers.length -2] + fibonacciNumbers[fibonacciNumbers.length -1];

    //Adds number to the list
    if (x < 4000000) {
        fibonacciNumbers.push(x);

        //Adds even fibonacci number
        if (x % 2 == 0) {
            answer += x;
        }
    }
}
//Displays answer
console.log(answer); //Expected 4613732