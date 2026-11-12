## 3. Hash Set

### Intuition

We can use a hash set to efficiently keep track of the values we have already encountered. As we iterate through the array, we check whether the current value is already present in the set. If it is, that means we've seen this value before, so a duplicate exists. Using a hash set allows constant-time lookups, making this approach much more efficient than comparing every pair.

### Algorithm

1. Initialize an empty hash set to store seen values.
2. Iterate through each number in the array.
3. For each number:
   - If it is already in the set, return `true` because a duplicate has been found.
   - Otherwise, add it to the set.
4. If the loop finishes without finding any duplicates, return `false`.

### Time & Space Complexity

- Time complexity: $O(n)$
- Space complexity: $O(n)$
