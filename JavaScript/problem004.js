//Variables
let product = 0;
let greatest = 0;

//Checks first multiplier
for (let a = 100; a <= 999; a++) {

    //Checks second multiplier
    for (let b = 100; b <= 999; b++) {

        //Gets product of multipliers and converts them to string
        product = a * b;
        let checkPalindrome = product + "";

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