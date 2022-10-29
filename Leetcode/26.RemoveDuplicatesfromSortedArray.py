class Solution(object):
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        print(length)
        count = 0

        # for i in range(0,length-1):
        #     if nums[i] == nums[i+1]:
        #      print(nums)
        #     #  nums.remove(nums[i+1])
        #      nums[i+1] = '_'
        #      count = count + 1
        #     print(i)
   
        # return count

        expectedNums = list(set(nums))
        count = length - len(expectedNums)
        new_length = len(expectedNums)
        while new_length!=0:
            expectedNums.append("_")
            new_length = new_length - 1
            
        return count, expectedNums
        

    nums = [0,0,1,1,1,2,2,3,3,4]#Input array
    expectedNums = [] # The expected answer with correct length

    k, expectedNums = removeDuplicates(nums) #function calling

    print(k)
    print(expectedNums)