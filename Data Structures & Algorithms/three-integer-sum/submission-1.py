class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def twosum(arr,target):
            seen = set()
            ans = []
            for x in arr:
                diff = target - x
                if diff in seen:
                    ans.append([x,diff])
                seen.add(x)
            return ans
        for i in range(len(nums)):
            target = -nums[i]
            arr = nums[:i] + nums[i+1:]
            twins = twosum(arr,target)
            if twins != []:
                for twin in twins:
                    triplets = sorted(twin + [nums[i]])
                    if triplets not in ans:
                        ans.append(triplets)
        return ans