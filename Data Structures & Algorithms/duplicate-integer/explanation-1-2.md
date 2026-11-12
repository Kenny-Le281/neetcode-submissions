## 4. Hash Set Length

### Intuition

This approach uses the same idea as the previous hash set method: a set only stores unique values, so duplicates are automatically removed. Instead of checking each element manually, we simply compare the length of the set to the length of the original array. If duplicates exist, the set will contain fewer elements. The logic is identical to the earlier approach — this version is just a shorter and more concise implementation of it.

### Algorithm

1. Convert the array into a hash set, which removes duplicates.
2. Compare the size of the set with the size of the original array.
3. If the set is smaller, return `true` because duplicates must have been removed.
4. Otherwise, return `false`.

### Time & Space Complexity

- Time complexity: $O(n)$
- Space complexity: $O(n)$
