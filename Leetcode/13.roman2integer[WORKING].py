class Solution(object):
    def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """


value = 0
romanAlpha= {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500, 'M':1000} 
romanNum = "MCMXCIV"
print(romanAlpha["I"])

for r in romanNum:
    for k in romanAlpha:
        if romanAlpha[str(k)] > romanAlpha[str(r)]:
           value = value + (romanAlpha[str(k)] - romanAlpha[str(r)])
           break
        else:
            print(r)
        

print(romanNum,value)