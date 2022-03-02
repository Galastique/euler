//Variables
factorial = BigInt(1);
let sum = 0;

//Finds 100 factorial
for(let i = 100; i > 1; i--){
    factorial *= BigInt(i);
}

//Converts it to string
factorial = factorial + "";

//Finds sum of all digits
for(let digit = 0; digit < factorial.length; digit++){
    sum += parseInt(factorial[digit]);
}

//Displays answer
console.log(sum); //Expected 648