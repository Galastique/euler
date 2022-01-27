import java.math.BigInteger;

public class problem015 {
    public static void main(String[] args) {
        
        //Variable
        BigInteger answer = new BigInteger("0");
        BigInteger twentyFactorial = new BigInteger("1");
        BigInteger fourtyFactorial = new BigInteger("1");

        //Number of possible paths
        for (int i = 1; i <= 20; i++) {
            twentyFactorial = twentyFactorial.multiply(BigInteger.valueOf(i));
        }

        for (int j = 1; j <= 40; j++) {
            fourtyFactorial = fourtyFactorial.multiply(BigInteger.valueOf(j));
        }

        BigInteger horizontal = twentyFactorial;
        BigInteger vertical = twentyFactorial;
        BigInteger end = fourtyFactorial;

        //Counts answer (binomial coefficient)
        answer = end.divide(horizontal.multiply(vertical));

        //Displays answer
        System.out.println(answer); //Expected 137846528820
    }
}