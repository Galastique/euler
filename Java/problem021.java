public class problem021 {
    public static void main(String[] args) {
        
        //Variables
        int amicable = 0;
        int a = 0;
        int b = 0;

        //For every number under ten thousand
        for(int number = 1; number < 10000; number++){
            a = 0;
            b = 0;

            //Find proper divisors of number
            for(int divisorA = 1; divisorA < (number/2) + 1; divisorA++){
                if(number % divisorA == 0){
                    a += divisorA;
                }
            }

            //Find proper divisors of a
            for(int divisorB = 1; divisorB <  (a/2) + 1; divisorB++){
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
        System.out.println(amicable); //Expected 31626
    }
}
