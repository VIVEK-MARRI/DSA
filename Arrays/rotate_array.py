"""
Problem: Rotate Array (Left and Right by K elements)
Link: https://leetcode.com/problems/rotate-array/
Difficulty: Medium

Approach:
- Use reversal algorithm:
  - Left Rotation:
    1. Reverse first k elements
    2. Reverse remaining elements
    3. Reverse whole array
  - Right Rotation: Similar but start from the end.
- O(n) time, O(1) extra space.
"""

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_left(arr, k):
    n = len(arr)
    if n == 0:
        return None
    k = k % n
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)
    return arr

def rotate_right(arr, k):
    n = len(arr)
    if n == 0:
        return None
    k = k % n
    reverse(arr, n - k, n - 1)
    reverse(arr, 0, n - k - 1)
    reverse(arr, 0, n - 1)
    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Rotate Left by 3:", rotate_left(arr[:], 3))  
    print("Rotate Right by 3:", rotate_right(arr[:], 3))  
