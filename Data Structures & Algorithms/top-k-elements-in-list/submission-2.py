class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = {}
        for n in nums:
            if n in numsDict:
                numsDict[n] += 1
            else:
                numsDict[n] = 1

        res = []
        res = sorted(numsDict, key = numsDict.get, reverse = True)

        return res[:k]