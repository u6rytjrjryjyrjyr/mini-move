def find_smallest_int(arr):
  min = arr[0]
  for item in arr:
    if min > item:
      min = item 
    return min


