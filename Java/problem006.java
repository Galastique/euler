public class problem006 {
    public static void main(String[] args) {
        //Variables
        int sum = 0;
        int squares = 0;

        //Finds sum and sum of squares
        for (int i = 1; i <= 100; i++) {
            sum += i;
            squares += i * i;
        }

        //Finds square of sum
        sum = sum * sum;

        //Displays answers
        System.out.println(sum - squares); //Expected 25164150
    }
}