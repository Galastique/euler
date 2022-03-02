public class problem003 {
	public static void main(String[] args) {

		//Variables
		long factors = 1L;
		long number = 600851475143L;

		//Finds prime factors of 600851475143
		for (long prime = 1L; prime < Math.floor(number/2); prime++) {

			//Multiplies number to total if its prime
			if (number % prime == 0L) {
				factors *= prime;

				//Check if all prime factors have been found
				if (factors == number) {
					System.out.print(prime); //Expected 6857
					break;
				}
			}
		}
	}
}