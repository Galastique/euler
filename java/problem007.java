import java.util.*;

public class problem007 {
    public static void main(String[] args) {
        //Variables
        List<Integer> primeNumbers = new ArrayList<Integer>(2);

        //Finds every prime number
        for (int prime = 3; prime < 200000; prime += 2) {
            int temp = 0;

            //Stops loop if answer has been found
            if (primeNumbers.size() == 10001) {
                break;
            }

            //Tests if each number in list is prime
            for (int i = 3; i < Math.round(Math.sqrt(prime))+1; i++) {
                if (prime % i == 0) {
                    temp = 1;
                    break;
                }
            }

            //Adds prime number to list
            if (temp == 0) {
                primeNumbers.add(prime);
            }
        }

        //Displays answer
        System.out.println(primeNumbers.get(primeNumbers.size() - 1)); //Expected 104743
    }
}