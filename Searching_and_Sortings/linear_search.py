"""
Problem: Linear Search
Link: https://www.geeksforgeeks.org/linear-search/
Difficulty: Easy

Approach:
- Traverse the array from left to right.
- Compare each element with the given key.
- If found, return its index (or message).
- Time Complexity: O(n)
- Space Complexity: O(1)
"""

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i   # return index if found
    return -1          # return -1 if not found


# -----------------------------
# Example Test Cases
# -----------------------------
if __name__ == "__main__":
    arr = [10, 11, 4, 5, 7, 77, 20, 31, 44]
    key = 20
    result = linear_search(arr, key)
    if result != -1:
        print(f"Key {key} found at index {result}")
    else:
        print(f"Key {key} not found")
