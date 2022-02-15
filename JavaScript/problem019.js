//Variable
let sundays = 0;

//For every year
for(let year = 1901; year < 2001; year++){

    //For every month
    for(let month = 0; month < 12; month++){

        //Get weekday of first day of the month
        let weekday = new Date(year, month, 1).getDay();

        //If day 1 = sunday count it
        if(weekday == 6){
            sundays += 1;
        }
    }
}

//Displays answers
console.log(sundays); //Expected 171