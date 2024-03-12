from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ans = []
        i = 0
        j = 0
        for k in range(0, m + n):
            if i < m and j < n:
                if nums1[i] <= nums2[j]:
                    ans.append(nums1[i])
                    i = i + 1
                else:
                    ans.append(nums2[j])
                    j = j + 1
            elif i < m:
                ans.append(nums1[i])
                i = i + 1
            else:
                ans.append(nums2[j])
                j = j + 1

        for k in range(0, m + n):
            nums1[k] = ans[k]

        for k in ans:
            print(k)


solution = Solution()
solution.merge([1, 2, 4, 0, 0, 0], 3, [2, 5, 6], 3)