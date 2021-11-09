public class problem001 {
	public static void main(String[] args) {

		// Variable
		int answer = 0;

		// Executes for every number under 1000
		for (int i = 0; i < 1000; i++) {

			// Checks if number is divisible by 3 or 5
			if (i % 3 == 0 || i % 5 == 0) {

				// Adds answer to total
				answer += i;
			}
		}

		// Displays answer
		System.out.print(answer); // Expected 233168
	}
}