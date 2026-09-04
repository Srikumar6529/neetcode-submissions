class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans1 = ""
        ans2 = ""
        for c in s:
            if not (c.isalpha() or c.isdigit()):
                continue
            
            ans1 = c.lower() + ans1
            ans2+=c.lower()
        #print(ans1,ans2)
        return ans1==ans2