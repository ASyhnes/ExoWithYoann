def binary_search(arr, x):
  low = 0
  high = len(arr) - 1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == x:
      return mid
    elif arr[mid] < x:
      low = mid + 1
    else:
      high = mid - 1
  return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 5
result = binary_search(arr, x)

if result != -1:
  print("Element is present at index", str(result))
else:
  print("Element is not present in array")