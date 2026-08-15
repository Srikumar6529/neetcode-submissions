class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        ans = []
        for i in range(len(nums)):
            val = nums[i]
            diff = target - val
            if diff in hashmap:
                ans = [hashmap[diff],i]
                break
            hashmap[val] = i
        print(hashmap)
        return ans
