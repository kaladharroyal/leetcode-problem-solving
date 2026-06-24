class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        for ch in s:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch]+=1
        for char in t:
            if char not in freq:
                return False
            freq[char] -= 1
            if freq[char]<0:
                return False
        return True                    
       