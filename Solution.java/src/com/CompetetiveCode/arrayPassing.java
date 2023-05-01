package com.CompetetiveCode;

public class arrayPassing {

    public static void main(String[] args) {
        int[] digits = {19, 21, 32, 40, 59};

        // Print out the array
        for (int i : digits) {
            System.out.print(i + " ");
        }
        System.out.println();

        int x = plusOne(digits);

        // Print out the resulting sum
        System.out.println("The sum is: " + x);
    }

    public static int plusOne(int[] digits) {
        int sum = 0;
        for (int i : digits) {
            sum += i;
        }
        return sum + 1;
    }
}


/* Wrong Code

public class arrayPassing {

    public static void main(String[] args) {      // main calling function
        int [] digits = {1,2,3,4,5};
        System.out.println(digits);
       int x = plusOne(digits);

    }
    public static int plusOne(Integer[] digits) {
        System.out.println("Hello");
        System.out.println(digits);
    return digits;
    }
}
 */