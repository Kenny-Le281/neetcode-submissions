class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        count = 0
        for num in nums:
            if target - num in numsDict:
                return [numsDict[target - num], count]
            numsDict[num] = count
            count += 1