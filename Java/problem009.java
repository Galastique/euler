public class problem009 {
    public static void main(String[] args) {
        
        //Variable
        int answer = 0;

        //Gets value of a
        for(int a = 1; a < 400; a++){
            
            //Gets value of b
            for(int b = a+1; b < 400; b++){

                //Assigns value to c
                int c = 1000-a-b;

                //Checks if pythagorean triplet has been found
                if ((answer == 0) && (a < b << c) && (a + b + c == 1000) && (a*a + b*b == c*c)){

                    //Assigns answer
                    answer = a*b*c;
                }
            }
        }

        //Displays answer
        System.out.println(answer); //Expected 31875000
    }
}