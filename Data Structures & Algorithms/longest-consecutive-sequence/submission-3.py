class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        lookup = set(nums)
        grps = {}
        for i in range(len(nums)):
            curr_val = nums[i]
            left = curr_val -1
            if left not in lookup:
                grps[curr_val] = 1
                looking_for = curr_val+1
                while looking_for in lookup:
                    grps[curr_val] += 1
                    looking_for = looking_for + 1
        return max(grps.values())