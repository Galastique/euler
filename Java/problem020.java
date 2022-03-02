import java.math.BigInteger;

public class problem020 {
    public static void main(String[] args) {

        //Variables
        BigInteger factorial = new BigInteger("1");
        String factorialString;
        int sum = 0;

        //Finds 100 factorial
        for(int i = 100; i > 1; i--){
            factorial = factorial.multiply(BigInteger.valueOf(i));
        }

        //Converts it to string
        factorialString = factorial.toString();

        //Finds sum of all digits
        for(int digit = 0; digit < factorialString.length(); digit++){
            sum += Character.getNumericValue(factorialString.charAt(digit));
        }

        //Displays answer
        System.out.println(sum); //Expected 648
    }
}