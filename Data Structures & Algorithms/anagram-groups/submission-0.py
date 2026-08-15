class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s,t):
            return sorted(list(s)) == sorted(list(t))
        hashmap = {}
        keys = set()
        for ele in strs:
            val = "".join(sorted(list(ele)))
            keys.add(val)
            if val in hashmap:
                hashmap[val].append(ele)
            else:
                hashmap[val] = [ele]
        ans = []
        for val in keys:
            ans.append(hashmap[val])
        return ans


