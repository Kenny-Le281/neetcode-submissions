## 2. Hash Map

### Intuition

If two strings are anagrams, they must use the same characters with the same frequencies. Instead of sorting, we can count how many times each character appears in both strings. By using two hash maps (or dictionaries), we track the frequency of every character in each string. If both frequency maps match exactly, then the strings contain the same characters with the same frequencies, meaning they are anagrams.

### Algorithm

1. If the two strings have different lengths, return `false` immediately.
2. Create two hash maps to store character frequencies for each string.
3. Iterate through the first string, increasing the count of each character in the first map.
4. Iterate through the second string, increasing the count of each character in the second map.
5. Compare the two maps:
   - If they are equal, return `true`.
   - Otherwise, return `false`.

### Time & Space Complexity

- Time complexity: $O(n + m)$
- Space complexity: $O(1)$
