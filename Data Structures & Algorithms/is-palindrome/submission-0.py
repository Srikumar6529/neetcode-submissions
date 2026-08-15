class Solution:
    def isPalindrome(self, s: str) -> bool:
        flag = True
        s = ''.join([char for char in s if char.isalnum()])
        s = s.strip(' ')
        #print(s)
        l=0
        r=len(s)-1
        while l<r:
            if s[l].lower()!=s[r].lower():
                flag=False
                break
            l+=1
            r-=1
        if flag:
            return True
        return False