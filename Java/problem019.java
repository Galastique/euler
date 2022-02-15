import java.util.Calendar;

public class problem019 {
    public static void main(String[] args) {

        //Variable
        int sundays = 0;
        Calendar calendar = Calendar.getInstance();

        //For every year
        for(int year = 1901; year < 2001; year++){

            //For every month
            for(int month = 0; month < 12; month++){

                //Get weekday of first day of the month
                calendar.set(Calendar.YEAR, year);
                calendar.set(Calendar.MONTH, month);
                calendar.set(Calendar.DAY_OF_MONTH, 0);
                int weekday = calendar.get(Calendar.DAY_OF_WEEK);

                //If day 1 = sunday count it
                if(weekday == 6){
                    sundays += 1;
                }
            }
        }

        //Displays answers
        System.out.println(sundays); //Expected 171
    }
}