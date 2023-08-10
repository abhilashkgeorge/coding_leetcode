class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        new_map = {}
        expected = 0

        #target = 6
        # nums = [3,2,4]

        #i = 0,1,2
        #value = 3,2,4
        #expected = 3,4,2
        #new_map = {0:3,}. {0: 3, 1: 2}



        for (i,value) in enumerate(nums):
            expected = abs(value - target)
            print(f'Expected = ', expected)
            print(new_map)
            if expected in new_map.keys():
                value = new_map[expected]
                return [value, i]
            else:
                new_map[value] = i
       # return [new_map[value],i ]


solution = Solution()
nums = [3,2,4]
target = 6
solution.twoSum(nums, target)
print(solution)