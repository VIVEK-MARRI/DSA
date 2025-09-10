"""
Problem: Move All Zeros to End of Array
Link: https://leetcode.com/problems/move-zeroes/
Difficulty: Easy

Approach:
- Use two-pointer technique.
- Traverse array:
  - Place non-zero elements at the current position.
  - After traversal, fill the remaining positions with zeros.
- O(n) time, O(1) space.
"""

def zeros_end(arr):
    if not arr:
        return None
    pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1
    while pos < len(arr):
        arr[pos] = 0
        pos += 1
    return arr


if __name__ == "__main__":
    arr = [0, 2, 0, 1, 3, 0, 4, 2]
    print("Original:", arr)
    print("After moving zeros to end:", zeros_end(arr))  
