from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] == val:
                if nums[j] != val:
                    nums[i] = nums[j]
                    nums[j] = val
                    count = count + 1
                    i = i + 1
                    j = j - 1
                else:
                    j = j - 1
            else:
                i = i + 1
                count = count + 1
        return count

solution = Solution()
nums = [0,1,2,2,3,0,4,2]
print(solution.removeElement(nums, 2))
print(nums)
