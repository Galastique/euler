//Variables
let factors = 1;
let number = 600851475143;

//Finds prime factors of 600851475143
for (let prime = 1; prime < number; prime++) {

    //Multiplies number to total if its prime
    if (number % prime == 0) {
        factors *= prime;

        //Check if all prime factors have been found
        if (factors == number) {
            console.log(prime); //Expected 6857
            break;
        }
    }
}