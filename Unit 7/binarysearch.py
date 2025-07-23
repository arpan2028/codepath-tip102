def binary_search(arr, l, r, target):
    if l >= r:
        return -1
    mid = (r + l)// 2
    if arr[mid] == target:
        return mid
    elif target > arr[mid]:
        binary_search(arr, mid + 1, t, target)
    else:
        binary_search(arr, l, mid - 1, target)
        
nums = [1, 3, 5, 7, 9, 11, 12]
print(binary_search(nums, 0, ))
