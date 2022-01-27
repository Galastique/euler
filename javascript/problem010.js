//Variable
let sumPrimes = 2;

//Finds prime numbers
for(x = 3; x < 2000000; x += 2){
    let temp = 0;

    //Tests if each number in list is prime
    for(i = 3; i < Math.round(Math.sqrt(x))+1; i++){
        if(x % i == 0){
            temp = 1;
            break;
        }
    }
    //Adds prime number to list
    if(temp == 0){
        sumPrimes += x;
    }
}

//Displays answer
console.log(sumPrimes); //Expected 142913828922