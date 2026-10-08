class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first lets find the appropriate row and then find the element in that row
        def bs(row, target):
            left = 0
            right = len(row) -1
            while left<=right:
                m = (left+right) // 2
                val = row[m]

                if val == target:
                    return True
                elif val< target:
                    left = m+1
                else:
                    right = m-1
            return False
        for row in matrix:
            if target>= row[0] and target<= row[-1]:
                return bs(row, target)
        return False
        

