class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def totalTime(piles, k):
            totalTime = 0
            for pile in piles:
                if pile< k:
                    totalTime += 1
                elif (pile % k) == 0:
                    totalTime += (pile//k)
                elif (pile % k) != 0 :
                    totalTime += ((pile//k) + 1)
            return totalTime
        
        left = 1
        right = max(piles)

        while left<=right:
            k = (left + right) // 2
            res = totalTime(piles, k)

            if res > h:
                left = k + 1
            else:
                right = k-1
        #print(left,right)
        return left
            