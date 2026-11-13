## Hash Map (One Pass)
 
### Intuition
 
For each number, the value we need to complete the pair is `target - num`. Instead of comparing every pair of numbers, we can use a hash map to remember the numbers we have already seen along with their indices. As we iterate through the array, we check whether the number we need is already in the map. If it is, we have found the pair. Otherwise, we store the current number and its index and move on. Because we only look at numbers we have already seen, a number can never be paired with itself, and duplicates are handled naturally.
 
### Algorithm
 
1. Initialize an empty hash map to store each number's value and its index.
2. Iterate through the array, keeping track of the current index.
3. For each number:
   - Compute the value needed to reach the target: `target - num`.
   - If that value is already in the map, return its stored index and the current index.
   - Otherwise, store the current number and its index in the map.
### Time & Space Complexity
 
- Time complexity: $O(n)$
- Space complexity: $O(n)$
