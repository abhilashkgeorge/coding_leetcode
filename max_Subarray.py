class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = 0
        maxArray = []

        if len(nums) == 0:
            maxArray.append(0) 
            print(maxArray[0])
            return maxArray[0]
        if len(nums) == 1: 
            maxArray.append(nums[0])
            print(maxArray[0])
            return maxArray[0]
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                current_sum = current_sum + nums[j]
                maxArray.append(current_sum)
            current_sum = 0
        print(max(maxArray))

class Optimised:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        current_sum = 0

        for num in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += num
            max_sum = max(max_sum, current_sum) 
        print(max_sum)
        return max_sum


nums = [-5,-4,-1,-7,-8]
sol = Optimised()
sol.maxSubArray(nums=nums)