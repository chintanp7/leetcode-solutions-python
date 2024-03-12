from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        if len(nums) <= 1:
            return len(nums)
        for j in range (1, len(nums)):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i = i + 1
        return i

solution = Solution()
nums = [0,1,2,2,3,3,4,4]
print(solution.removeDuplicates(nums))
print(nums)
