import java.util.*;

public class problem002 {
	public static void main(String[] args) {

		//Variables
		List<Integer> fibonacciNumbers = new ArrayList<Integer>(Arrays.asList(0, 1));
		int answer = 0;

		//Finds fibonacci numbers
		for (int i = 0; i < 4000000; i += 2) {

			//Finds value of next number
			int x = fibonacciNumbers.get(fibonacciNumbers.size() - 1) + fibonacciNumbers.get(fibonacciNumbers.size() - 2);

			//Adds number to list
			if (x < 4000000) {
				fibonacciNumbers.add(x);

				//Checks if number is even
				if (x % 2 == 0) {
					answer += x;
				}
			}
		}

		//Displays answer
		System.out.print(answer); //Expected 4613732
	}
}