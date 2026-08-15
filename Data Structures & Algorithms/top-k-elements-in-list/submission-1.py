class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for val in nums:
            if val in count:
                count[val]+=1
            else:
                count[val] = 1
        tmp = []
        for val in count:
            #[count,num]
            tmp.append([count[val],val])
        sorted_tmp = sorted(tmp,reverse=True)
        ans = []
        tmp_ans = sorted_tmp[:k]
        for val in tmp_ans:
            ans.append(val[1])
        return ans

