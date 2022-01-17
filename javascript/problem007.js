//Variables
let primeNumbers = [];
let answer = 0;

//Loop
for (prime = 2; prime < 200000; prime++) {
    temp = 0;

    //Stops loop if list has 10001 items
    if (primeNumbers.length == 10001) {
        break;
    }

    //Tests if each number in list is prime
    for (i = 2; i <= primeNumbers.length; i++) {
        if (prime % i == 0) {
            temp = 1;
            break;
        }
    }

    //Adds prime number to list
    if (temp == 0) {
        primeNumbers.push(prime);
    }
}

//Gets answer
answer = primeNumbers[primeNumbers.length - 1];

//Displays answer
console.log(answer); //Expected 104743