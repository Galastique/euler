public class problem001 {
	public static void main(String[] args) {

		//Variable
		int answer = 0;

		//Finds the multiples of 3 or 5 under 1000
		for (int i = 0; i < 1000; i++) {
			if (i % 3 == 0 || i % 5 == 0) {
				answer += i;
			}
		}

		//Displays answer
		System.out.print(answer); //Expected 233168
	}
}