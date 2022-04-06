//Variables
let factors = 1;
let number = 600851475143;
let prime = 0;

//Finds prime factors of 600851475143
while (factors != number) {
    prime += 1;

    //Multiplies number to total if its prime
    if (number % prime == 0) {
        factors *= prime;
    }
}

//Displays answer
console.log(prime); //Expected 6857