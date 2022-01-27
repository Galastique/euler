//Variables
let primeNumbers = [2];

//Finds every prime number
for (prime = 3; prime < 200000; prime += 2) {
    temp = 0;

    //Stops loop if answer has been found
    if (primeNumbers.length == 10001) {
        break;
    }

    //Tests if each number in list is prime
    for (i = 3; i < Math.round(Math.sqrt(prime))+1; i++) {
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

//Displays answer
console.log(primeNumbers[primeNumbers.length - 1]); //Expected 104743