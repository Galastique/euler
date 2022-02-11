import java.math.BigInteger;

public class problem016 {
    public static void main(String[] args) {
        
        //Variables
        BigInteger bigNumber = new BigInteger("2").pow(1000);
        String numbers = bigNumber.toString();
        int sum = 0;
        
        //Adds every digit of number to sum
        for(int x = 0; x < numbers.length(); x++){
            sum += Character.getNumericValue(numbers.charAt(x));
        }

        //Displays answer
        System.out.println(sum); //Expected 1366
    }
}