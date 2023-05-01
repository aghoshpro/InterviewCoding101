    package com.CompetetiveCode;

    import java.util.Arrays;
    import static java.lang.Math.pow;

    public class plusONE {
        public static void main(String[] args) {
            int[] digits = {9};
            plusOne(digits);
        }

        public static int[] plusOne(int[] digits) {
            int sum02 = 0;
            int[] arr = new int[digits.length];
            int j = digits.length - 1;
            if(digits[0] == 9){
                arr[0] = 0;
                arr[1] = 1;
            }
            else {
                    for (int k = 0; k < digits.length; k++) {
                        sum02 += digits[k] * pow(10, digits.length - k);
                    }
                    sum02 = sum02 / 10 + 1;
                    System.out.print(sum02);

                    while (sum02 > 0 & j >= 0) {
                        arr[j] = sum02 % 10;
                        sum02 = sum02 / 10;
                        j--;
                    }
            }
            // Print out the resulting sum
            System.out.println(Arrays.toString(arr));
            return arr;
        }
    }
