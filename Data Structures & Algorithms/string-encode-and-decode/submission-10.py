class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        #we will use len# as delimiter
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans
    def decode(self, s: str) -> List[str]:
        print(s)
        # egample string 4#neet4#code
        res = []
        i = 0
        print(s)
        while i < len(s):
            tmp =""
            while s[i]!="#":
                tmp+=s[i]
                i+=1
            length = int(tmp)
            j = i+1
            k = i+length
            res.append(s[j:k+1])
            i = k+1
            #print(res)
        return res