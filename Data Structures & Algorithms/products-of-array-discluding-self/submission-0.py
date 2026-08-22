class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        ans = []
        n = len(nums)
        for i in range(n):
            x = nums[i]
            curr_left = x * left[-1]
            left.append(curr_left)
            y = nums[n-i-1]
            curr_right = y * right[-1]
            right.append(curr_right)
        left = left[:-1]
        right = right[:-1]
        #print(left)
        #print(right)
        for i in range(n):
            ans.append(left[i]*right[-i-1])
        return ans