public class problem010 {
    public static void main(String[] args) {
        
        //Variable
        long sumPrimes = 2L;

        //Finds prime numbers
        for(int x = 3; x < 2000000; x += 2){
            int temp = 0;

            //Tests if each number in list is prime
            for(int i = 3; i < Math.round(Math.sqrt(x))+1; i++){
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
        System.out.println(sumPrimes); //Expected 142913828922
    }
}