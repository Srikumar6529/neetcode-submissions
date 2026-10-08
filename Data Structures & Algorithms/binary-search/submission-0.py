class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            m = (left + right) // 2
            val = nums[m]

            if val == target:
                return m
            elif val < target:
                left = m+1
            else:
                right = m-1
        return -1