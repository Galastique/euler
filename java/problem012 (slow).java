public class problem012 {
    public static void main(String[] args) {
        
        //Variables
        int divisors = 0;
        int number = 0;

        //Finds triangular number
        for(int x = 1; x < 100000; x++){
            divisors = 0;
            number += x;

            //Counts divisors
            for(int y = 1; y < Math.round(number/2)+1; y++){
                if(number % y == 0){
                    divisors += 1;
                }
            }

            //Checks if answer has been found
            if(divisors > 500){
                //Displays answers
                System.out.println(number); //Expected 76576500
                System.exit(1);
            }
        }
    }
}
