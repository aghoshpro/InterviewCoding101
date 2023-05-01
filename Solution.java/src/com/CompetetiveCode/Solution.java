package com.CompetetiveCode;

public class Solution {
    public static void main(String[] args) {
        int k = countEven(13);
        System.out.println("Number of eve numbers = " + k);
    }
    public static int sumOfDigit(int number){
        int digit , sum = 0;
        while(number > 0)
        {
            digit = number % 10;
            sum = sum + digit;
            number = number / 10;
        }
        return sum;
    }
    public static int countEven(int num) {
        int count = 0;
        for (int i = 1; i <=num; i++) {
            if(sumOfDigit(i)%2==0){
                System.out.println(i);
                count++;
            }
        }
        return count;
    }

}
