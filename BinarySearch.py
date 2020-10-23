"""
    Time Complexity = O(log(N))
    Space Complexity = O(1) - Iterativvely
    Space Complexity = O(log(N)) - Recursively
    Algorithm Type: Divide and Conquer
"""

def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2