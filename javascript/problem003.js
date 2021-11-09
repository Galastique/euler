//Variables
var factors = [];
var number = 600851475143;
var temp = 1;

//Finds prime factors of 600851475143
for (prime = 0; prime < number; prime++) {

    //Adds number to list if its prime
    if (number % prime == 0) {
        factors.push(prime);


        //Counts product of primes
        temp = temp * prime;


        //Check if all prime factors have been found
        if (temp == number) {
            console.log(prime); //Expected 6857
            break;
        }
    }
}