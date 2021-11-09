public class problem006 {
    public static void main(String[] args) {
        // Variables
        int sum = 0;
        int squares = 0;
        int answer;

        // Adds numbers from 1 to 100 together
        for (int i = 1; i <= 100; i++) {
            sum += i;// Adds numbers together
            squares += i * i; // Adds square of numbers together
        }

        // Finds square of sum
        sum = sum * sum;

        // Gets final answer
        answer = sum - squares;

        // Displays answers
        System.out.println(answer); // Expected 25164150
    }
}