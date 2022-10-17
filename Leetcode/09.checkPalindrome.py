# ######## isPalidrome LOGIC ########
class Solution(object):
    def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        inverse = x
        if x > 0:  # handle positive numbers  
            inverse =  int(str(x)[::-1])  
        if x <=0:  # handle negative numbers  
            inverse = -1 * int(str(x*-1)[::-1])  

        mina = -2**31  
        maxa = 2**31 - 1  
        if mina <= x <= maxa and inverse!= x:  
              print("NOT palidrome")  
        else:  
              print(str(x)+ " is a palindrome")
              
              
    isPalindrome(8878)

#===============================================================================================================
########  LeetCode Submission Fotmat ########
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        inverse = x
        if x > 0:  # handle positive numbers  
            inverse =  int(str(x)[::-1])  
        if x <=0:  # handle negative numbers  
            inverse = -1 * int(str(x*-1)[::-1])  

        mina = -2**31  
        maxa = 2**31 - 1  
        if mina <= x <= maxa and inverse!= x:  
              return 0
        elif x<0:
            return 0
        else:  
              return 1
              
              
# Runtime: 56 ms, faster than 93.09% of Python online submissions for Palindrome Number.
# Memory Usage: 13.4 MB, less than 35.32% of Python online submissions for Palindrome Number.