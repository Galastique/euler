//Variables
let longest = 0;
let number = 0;
let length = 0;
let answer = 0;

//Finds longest chain
for(let n = 1; n < 1000000; n += 2){
    length = 0;
    number = n;

    //Execute until chain length has been found
    while(number > 1){

        //if number is even
        if(number % 2 == 0){
            number = number / 2;
            length++;
        }

        //if number is odd
        else{
            number = 3 * number + 1;
            length++;
        }
        
        //Checks if new chain is bigger
        if(length > longest){
            longest = length;
            answer = n;
        }
    }
}

//Shows answers
console.log(answer); //Expected 837799