//Variables
var product = 0;
var greatest = 0;


//Checks first multiplier
for (a = 100; a <= 999; a++) {

    //Checks second multiplier
    for (b = 100; b <= 999; b++) {

        //Gets product of multipliers and converts them to string
        product = a * b;
        checkPalindrome = (product + "");

        //Check if number is palindrome
        if ((checkPalindrome.charAt(0) == checkPalindrome.charAt(checkPalindrome.length - 1)) && (checkPalindrome.charAt(1) == checkPalindrome.charAt(checkPalindrome.length - 2)) && (checkPalindrome.charAt(2) == checkPalindrome.charAt(checkPalindrome.length - 3))) {

            //Checks if product is the biggest palindrome so far
            if (product > greatest) {
                greatest = product;
            }
        }
    }
}

//Displays answer
console.log(greatest); //Expected 906609