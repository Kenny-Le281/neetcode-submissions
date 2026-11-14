## 1. Sorting

### Intuition

Anagrams become identical when their characters are sorted. For example, `"eat"`, `"tea"`, and `"ate"` all become `"aet"` after sorting. By using the sorted version of each string as a key, we can group all anagrams together. Strings that share the same sorted form must be anagrams, so placing them in the same group is both natural and efficient.

### Algorithm

1. Create a hash map where each key is the sorted version of a string, and the value is a list of strings belonging to that anagram group.
2. Iterate through each string in the input list:
   - Sort the characters of the string to form a key.
   - Append the original string to the list corresponding to this key.
3. After processing all strings, return all values from the hash map, which represent the grouped anagrams.

### Time & Space Complexity

- Time complexity: $O(m \cdot n \log n)$
- Space complexity: $O(m \cdot n)$
