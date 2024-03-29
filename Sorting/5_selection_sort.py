# Python program for implementation of Selection Sort

import sys
A = [64, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(A)):
  
  # Find the smallest element in remaining unsorted array
  min_idx = i
  for j in range(i+1, len(A)):
    if A[min_idx] > A[j]:
      min_idx = j
  # We found the smallest element in array at the end of the above loop    
  # Swap the found smallest element with first element
  A[i], A[min_idx] = A[min_idx], A[i]
  
  # Driver code to test above 
print ("Sorted array") 
for i in range(len(A)): 
    print("%d" %A[i])