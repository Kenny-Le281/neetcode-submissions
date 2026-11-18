class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = {}
        counter = 0
        mostFrequent = []
        
        for n in nums:
            if n in numsDict:
                numsDict[n] += 1
            else:
                numsDict[n] = 1

        while counter < k:
            highestValueKey = max(numsDict, key = numsDict.get)
            mostFrequent.append(highestValueKey)
            numsDict.pop(highestValueKey)
            counter += 1

        return mostFrequent