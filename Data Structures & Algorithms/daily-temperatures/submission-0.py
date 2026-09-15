class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        cnt = {}
        for i in range(len(temperatures)):
            val = temperatures[i]
            while stack != []:
                j = stack.pop()
                tmp = temperatures[j]
                if val > tmp:
                    cnt[j] = i - j
                else:
                    stack.append(j)
                    break
            cnt[i] = 0
            stack.append(i)
        ans = []
        #print(cnt)
        for x in cnt:
            ans.append(cnt[x])
        return ans