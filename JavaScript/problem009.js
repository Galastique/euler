//Variable
let answer = 0;

//Gets value of a
for(let a = 1; a < 400; a++){
    
    //Gets value of b
    for(let b = a+1; b < 400; b++){

        //Assigns value to c
        let c = 1000-a-b;

        //Checks if pythagorean triplet has been found
        if ((answer == 0) && (a < b < c) && (a + b + c == 1000) && (a*a + b*b == c*c)){

            //Assigns answer
            answer = a*b*c;
        }
    }
}

//Displays answer
console.log(answer); //Expected 31875000