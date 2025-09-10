"""
Problem: Reverse an Array
Link: https://www.geeksforgeeks.org/dsa/program-to-reverse-an-array/
Difficulty: Easy

Approach:
- Use two-pointer technique (start and end).
- Swap elements until pointers meet in the middle.
- This reverses the array in-place with O(n) time and O(1) extra space.
"""

def reverse_array(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


if __name__ == "__main__":
    arr1 = [10, 20, 30, 40, 50, 60, 70]
    print("Original:", arr1)
    print("Reversed:", reverse_array(arr1))  

    arr2 = [1, 2, 3, 4, 5]
    print("Original:", arr2)
    print("Reversed:", reverse_array(arr2))  
