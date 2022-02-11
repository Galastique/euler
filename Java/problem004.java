public class problem004 {
    public static void main(String[] args) {

        //Variables
        int product = 0;
        int greatest = 0;
        String checkPalindrome;

        //Checks first multiplier
        for (int a = 100; a <= 999; a++) {

            //Checks second multiplier
            for (int b = 100; b <= 999; b++) {

                //Gets product of multipliers and converts them to string
                product = a * b;
                checkPalindrome = (product + "");

                //Check if number is palindrome
                if ((checkPalindrome.charAt(0) == checkPalindrome.charAt(checkPalindrome.length() - 1)) && (checkPalindrome.charAt(1) == checkPalindrome.charAt(checkPalindrome.length() - 2)) && (checkPalindrome.charAt(2) == checkPalindrome.charAt(checkPalindrome.length() - 3))) {

                    //Checks if product is the biggest palindrome so far
                    if (product > greatest) {
                        greatest = product;
                    }
                }
            }
        }

        //Displays answer
        System.out.println(greatest); //Expected 906609
    }
}