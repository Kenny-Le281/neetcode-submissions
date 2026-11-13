class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sDict = {}
        tDict = {}

        for ch in s:
            sDict[ch] = sDict.get(ch, 0) + 1

        for ch in t:
            tDict[ch] = tDict.get(ch, 0) + 1

        if sDict == tDict:
            return True
        else:
            return False
