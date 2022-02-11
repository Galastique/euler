//Variables
let bigNumber = BigInt(2**1000) + "";
let sum = 0;

//Adds every digit of number to sum
for(let x = 0; x < bigNumber.length; x++){
    sum += parseInt(bigNumber.charAt(x));
}

//Displays answer
console.log(sum); //Expected 1366