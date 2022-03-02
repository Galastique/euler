//Variables
let amicable = 0;
let a = 0;
let b = 0;

//For every number under ten thousand
for(let number = 1; number < 10000; number++){
    a = 0;
    b = 0;

    //Find proper divisors of number
    for(let divisorA = 1; divisorA < Math.round((number/2), 0) + 1; divisorA++){
        if(number % divisorA == 0){
            a += divisorA;
        }
    }

    //Find proper divisors of a
    for(let divisorB = 1; divisorB <  Math.round((a/2), 0) + 1; divisorB++){
        if(a % divisorB == 0){
            b += divisorB;
        }
    }

    //Checks if numbers are amicable
    if((b == number) && (a != b)){
        amicable += a;
    }
}

//Displays answer
console.log(amicable); //Expected 31626