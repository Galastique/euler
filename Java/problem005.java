public class problem005 {
    public static void main(String[] args) {
        //Variables
        int answer = 0;
        int primes = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19; //Makes things faster by multiplying primes together
        int temp = 0;

        //Finds smallest divisible number
        while(temp != 19){
            temp = 0;
            answer += primes;

            //Checks if numbers are divisable by numbers from 2 to 20
            for (int i = 2; i < 21; i++) {
                if (answer % i == 0) {
                    temp += 1;
                }
            }
        }
        
        //Displays answer
        System.out.println(answer); //Expected 232792560
    }
}