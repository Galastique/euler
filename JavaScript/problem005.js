//Variables
let answer = 0;
let primes = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19; //Makes things faster by multiplying primes together
let temp = 0;

//Finds smallest divisible number
while(temp != 19){
    temp = 0;
    answer += primes;

    //Checks if numbers are divisable by numbers from 2 to 20
    for (let i = 2; i < 21; i++) {
        if (answer % i == 0) {
            temp += 1;
        }
    }
}

//Displays answer
console.log(answer); //Expected 232792560