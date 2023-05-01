package com.CompetetiveCode;

import java.util.Arrays;
import static java.lang.Math.pow;

public class digitSumEvenLOGIC2148 {

    public static void main(String[] args) {
        int[] digits = {1, 2, 3};
        int[] arr = new int[digits.length];
        int j = digits.length - 1;
        // Print out the array
        for (int i : digits) {
            System.out.print(i + " ");
        }
        System.out.println();

        int x = plusOne(digits);
        while(x>0){
            arr[j] = x%10;
            x = x/10;
            j--;
        }
        // Print out the resulting sum
        System.out.println("The sum is: " + Arrays.toString(arr));
    }

    public static int plusOne(int[] digits) {
        int sum02 = 0;
        for(int k=0; k<digits.length; k++) {
            sum02 += digits[k] * pow(10,digits.length - k);
        }
        sum02 = sum02/10 + 1;
        return sum02;
    }
}


/* Wrong Code

public class digitSumEvenLOGIC2148 {

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