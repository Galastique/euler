import java.util.*;

public class problem007 {
    public static void main(String[] args) {
        // Variables
        List<Integer> primeNumbers = new ArrayList<Integer>();
        int answer = 0;

        // Loop
        for (int prime = 2; prime < 200000; prime++) {
            int temp = 0;

            // Stops loop if list has 10001 items
            if (primeNumbers.size() == 10001) {
                break;
            }

            // Tests if each number in list is prime
            for (int i = 2; i <= primeNumbers.size(); i++) {
                if (prime % i == 0) {
                    temp = 1;
                    break;
                }
            }

            // Adds prime number to list
            if (temp == 0) {
                primeNumbers.add(prime);
            }
        }

        // Gets answer
        answer = primeNumbers.get(primeNumbers.size() - 1);

        // Displays answer
        System.out.println(answer); // Expected 104743
    }
}