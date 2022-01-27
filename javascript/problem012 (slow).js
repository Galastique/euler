//Variables
let divisors = 0;
let number = 0;

//Finds triangular number
for(x = 1; x < 100000; x++){
    divisors = 0;
    number += x;

    //Counts divisors
    for(y = 1; y < Math.round(number/2)+1; y++){
        if(number % y == 0){
            divisors += 1;
        }
    }

    //Checks if answer has been found
    if(divisors > 500){
        //Displays answers
        console.log(number); //Expected 76576500
        process.exit(1);
    }
}
