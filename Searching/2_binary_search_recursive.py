# Python Program for recursive binary search. 
  
# Returns index of x in arr if present, else -1 
import math
def binarySearch_recursive(arr, l, r, x):
  
  #check base case
  if l > r:
    return -1 # Element is not found in array
  
  else:
    mid = math.floor((l+r)/2)
    
    # If element is present at the middle itself 
    if arr[mid] == x:
      return mid
    
    # If element is smaller than mid, then it  
    # can only be present in left subarray
    if arr[mid] > x:
      return binarySearch_recursive(arr, l, mid-1, x)
    
    # Else the element can only be present  
    # in right subarray
    else: 
      return binarySearch_recursive(arr, mid+1, r, x)

    
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 40
  
# Function call 
result = binarySearch_recursive(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result )
else: 
    print ("Element is not present in array")  