class Solution(object):
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        print(length)
        count = 0

        for i in range(len(nums)):
         if nums[i] == nums[i+1] and i != length:
            print(nums)
            # nums.remove(nums[i+1])
            # count = count + 1
            # print(i)
   
        return count


    nums = [0,0,1,1,1,2,2,3,3,4]#Input array
    expectedNums = [] # The expected answer with correct length

    k = removeDuplicates(nums) #Calls your implementation

    print(k)
    # assert k == expectedNums.length;
    # for (int i = 0; i < k; i++) {
    #     assert nums[i] == expectedNums[i];
    # }