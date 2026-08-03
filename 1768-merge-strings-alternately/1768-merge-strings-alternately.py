from itertools import zip_longest
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for a, b in zip_longest(word1, word2, fillvalue=""):
            if a == "":
                res.append(b)
            elif b == "":
                res.append(a)
            else:
                res.append(a)
                res.append(b)

        return "".join(res)        
                