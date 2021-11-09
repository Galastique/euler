//Variables
answer = 0;
primes = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19; //Makes things faster by multiplying primes together


//Loop
for (i = primes; i < 1000000000; i += primes) {

    temp = 0;

    //Checks if numbers are divisable by numbers from 2 to 20
    for (j = 2; j < 21; j++) {
        if (i % j == 0) {
            temp += 1;

            //If number can be divided by all numbers
            if (temp == 19) {
                answer = i;

                //Displays answer
                console.log(answer); //Expected 232792560
                process.exit(1);
            }
        }
    }
}