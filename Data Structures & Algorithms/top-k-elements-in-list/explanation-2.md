# Sorting

## Intuition

To find the `k` most frequent numbers, we first need to know how often each number appears. A hash map is ideal for this: as we iterate through the array, we store each number as a key and its count as the value, adding 1 every time we see it again. Once we have the counts, the problem becomes ordering. We sort the numbers by their counts from highest to lowest, so the most frequent numbers end up at the front of the list. The answer is then simply the first `k` numbers. Because we sort the keys (the numbers themselves) and only use the counts to decide the order, the result contains the numbers we want to return, not their counts.

## Algorithm

1. Initialize an empty hash map to store each number and the number of times it appears.
2. Iterate through the array. For each number:
   * If it is already in the map, increase its count by 1.
   * Otherwise, add it to the map with a count of 1.
3. Sort the keys of the map by their counts in descending order.
4. Return the first `k` elements of the sorted list.

## Time & Space Complexity

* Time complexity: O(n log n)
* Space complexity: O(n)

> Counting takes O(n). Sorting the unique numbers takes O(u log u), where u is the number of unique values, which is at most O(n log n). Slicing the first `k` elements takes O(k). The map and the sorted list together use O(u) space, which is at most O(n).

## Code

```python
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
```
