//Variable
let answer = 0;

//Finds the multiples of 3 or 5 under 1000
for (x = 0; x < 1000; x++) {
    if (x % 3 == 0 || x % 5 == 0) {
        answer += x;
    }
}

//Displays answer
console.log(answer); //Expected 233168
