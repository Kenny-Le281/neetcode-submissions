# Top K Frequent Elements: Solution Explained

## The problem

Given a list of integers `nums` and an integer `k`, return the `k` numbers that appear most often. The answer can be in any order.

Example: `nums = [1, 1, 1, 2, 2, 3]`, `k = 2` returns `[1, 2]`.

## The solution

```python
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
```

## The idea

1. Count how many times each number appears, using a dictionary.
2. Repeat `k` times: find the number with the highest count, save it, and remove it from the dictionary so it isn't picked again.
3. Return the saved numbers.

## Step by step

### Setup

```python
numsDict = {}
counter = 0
mostFrequent = []
```

- `numsDict` maps each number to how many times it appears (key = number, value = count).
- `counter` tracks how many numbers have been picked so far.
- `mostFrequent` collects the answer.

### Step 1: count the numbers

```python
for n in nums:
    if n in numsDict:
        numsDict[n] += 1
    else:
        numsDict[n] = 1
```

For each number `n`, if it's already a key, add 1 to its count. Otherwise add it with a count of 1. The `if` check is needed because `numsDict[n] += 1` raises a `KeyError` on a key that doesn't exist yet.

For `nums = [1, 1, 1, 2, 2, 3]`, this produces:

```python
numsDict = {1: 3, 2: 2, 3: 1}
```

### Step 2: pick the top k

```python
while counter < k:
    highestValueKey = max(numsDict, key = numsDict.get)
    mostFrequent.append(highestValueKey)
    numsDict.pop(highestValueKey)
    counter += 1
```

Each pass of the loop does four things:

- **`max(numsDict, key = numsDict.get)`** finds the key with the highest value.
  - Passing the dictionary means `max` looks at its **keys**.
  - `key = numsDict.get` tells `max` to score each key by its value (its count). The method is passed without parentheses, because `max` calls it for you.
  - The result is the key, not the count.
- **`mostFrequent.append(...)`** saves that key in the answer.
- **`numsDict.pop(...)`** removes it, so the next pass finds the next highest.
- **`counter += 1`** counts the pick. When `counter` reaches `k`, the loop stops.

Trace with `k = 2`:

| Pass | numsDict before | Highest key | mostFrequent after |
|------|-----------------|-------------|--------------------|
| 1 | `{1: 3, 2: 2, 3: 1}` | 1 | `[1]` |
| 2 | `{2: 2, 3: 1}` | 2 | `[1, 2]` |

### Step 3: return

```python
return mostFrequent
```

The function must **return** the list. Printing it isn't enough, because the grader reads the return value. A function with no `return` gives back `None`.

## Complexity

- **Counting** takes O(n), where n is the length of `nums`.
- **Each `max`** scans the whole dictionary, so it costs O(u), where u is the number of unique values.
- The loop runs `k` times, so picking costs O(u × k).
- **Total time:** O(n + u × k). In the worst case (k close to u) that is roughly O(n²).
- **Space:** O(u) for the dictionary.

## Which approach is this?

It is none of NeetCode's three listed approaches (sorting, heap, bucket sort). It is a repeated max selection loop. It does the same job as a heap, "take the largest, remove it, repeat", but it finds the largest with a full scan each time, so it is slower.

## Faster alternatives

### Sorting: O(n log n)

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = {}
        for n in nums:
            numsDict[n] = numsDict.get(n, 0) + 1

        sortedKeys = sorted(numsDict, key=numsDict.get, reverse=True)
        return sortedKeys[:k]
```

- `sorted(numsDict, ...)` loops over the **keys** and returns a **list** of them.
- `key=numsDict.get` orders the keys by their counts. The counts only decide the order and are not in the output.
- `reverse=True` puts the highest counts first. The default is ascending (smallest to largest).
- `[:k]` takes the first `k` items.

### Heap: O(n log k)

Keep a min-heap of size `k` holding `(count, number)` pairs. Push each pair, and whenever the heap grows past `k`, pop the smallest. What remains are the `k` most frequent numbers.

### Bucket sort: O(n)

Make a list where index `i` holds the numbers that appeared exactly `i` times. Read it from the highest index down until you have `k` numbers.

## Small cleanups

- `for _ in range(k):` is tidier than managing `counter` by hand.
- `numsDict[n] = numsDict.get(n, 0) + 1` replaces the `if/else` in the counting step.
- `collections.Counter(nums).most_common(k)` does the counting and the top-k in one call.
