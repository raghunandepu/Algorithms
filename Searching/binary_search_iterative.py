# Python Program for iterative binary search. 
  
# Returns index of x in arr if present, else -1 
import math
def binarySearch_iterative(arr, l, r, x):
  
  while (l <= r):
    
    mid = math.floor((l+r)/2)
    
    # If element is present at the middle itself 
    if arr[mid] == x:
      return mid
    
    # If element is smaller than mid, then it  
    # can only be present in left subarray
    if arr[mid] > x:
      r = mid-1
    
    # Else the element can only be present  
    # in right sub array
    else: 
      l = mid + 1
      
  # If we reach here, then the element 
  # was not present 
  return -1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 40
  
# Function call 
result = binarySearch_iterative(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print (f"Element is present at index {result}" )
else: 
    print ("Element is not present in array")  