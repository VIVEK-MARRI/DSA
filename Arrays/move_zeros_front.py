"""
Problem: Move All Zeros to Front of Array
Link: https://www.geeksforgeeks.org/move-zeroes-front-array/
Difficulty: Easy

Approach:
- Create a new array filled with zeros.
- Traverse from right to left and place non-zero elements at correct position.
- O(n) time, O(n) space.
"""

def zeros_front(arr):
    if not arr:
        return None
    n = len(arr)
    res = [0] * n
    pos = n - 1
    for i in range(n - 1, -1, -1):
        if arr[i] != 0:
            res[pos] = arr[i]
            pos -= 1
    return res


if __name__ == "__main__":
    arr = [0, 2, 0, 1, 3, 0, 4, 2]
    print("Original:", arr)
    print("After moving zeros to front:", zeros_front(arr))  
