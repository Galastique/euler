import java.util.*;

public class problem003 {
	public static void main(String[] args) {

		// Variables
		List<Long> factors = new ArrayList<Long>(Arrays.asList(0L, 1L));
		long number = 600851475143L;
		long temp = 1;

		for (long prime = 1L; prime < number; prime++) {

			// Adds number to list if its prime
			if ((number % prime) == 0) {
				factors.add(prime);

				// Counts product of primes
				temp = temp * prime;

				// Check if all prime factors have been found
				if (temp == number) {
					System.out.print(prime); // Expected 6857
					break;
				}
			}
		}
	}
}