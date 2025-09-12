"""
Problem: Binary Search
Link: https://www.geeksforgeeks.org/binary-search/
Difficulty: Easy

Approach:
- Use two pointers (low = l, high = r) to define the search space.
- Find the middle element → mid = l + (r-l)//2
- Compare target with arr[mid]:
    - If arr[mid] == target → return index.
    - If arr[mid] > target → search left half (r = mid-1).
    - If arr[mid] < target → search right half (l = mid+1).
- Continue until l > r → return -1 if not found.
- Time Complexity: O(log n)
- Space Complexity: O(1)
"""

def binary_search(arr, tar):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == tar:
            return mid
        elif arr[mid] > tar:
            r = mid - 1
        else:
            l = mid + 1
    return -1


# -----------------------------
# Example Test Cases
# -----------------------------
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13]
    target = 7
    result = binary_search(arr, target)
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found")

    target2 = 6
    result2 = binary_search(arr, target2)
    if result2 != -1:
        print(f"Element {target2} found at index {result2}")
    else:
        print(f"Element {target2} not found")
