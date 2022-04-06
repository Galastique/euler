public class problem003 {
	public static void main(String[] args) {

		//Variables
		long factors = 1L;
		long number = 600851475143L;
		long prime = 0L;

		//Finds prime factors of 600851475143
		while (factors != number) {
			prime += 1;

			//Multiplies number to total if its prime
			if (number % prime == 0L) {
				factors *= prime;
			}
		}

		//Displays answer
		System.out.print(prime); //Expected 6857
	}
}