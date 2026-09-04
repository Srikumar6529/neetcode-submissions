class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index = {}
        for i in range(len(numbers)):
            val = numbers[i]
            diff = target - val
            if diff in index:
                return [index[diff]+1,i+1]
            index[val] = i
        return []