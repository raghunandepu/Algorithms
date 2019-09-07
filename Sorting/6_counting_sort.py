# Python program for counting sort
# Source: https://www.interviewcake.com/concept/python3/counting-sort

# The main function that sort the given string arr[] in  
# alphabetical order 

def counting_sort(the_list, max_value):

  # Count the number of times each value appears.
  # counts[0] stores the number of 0's in the input
  # counts[4] stores the number of 4's in the input
  # etc.
  counts = [0] * (max_value + 1)
  for item in the_list:
      counts[item] += 1

  # Overwrite counts to hold the next index an item with
  # a given value goes. So, counts[4] will now store the index
  # where the next 4 goes, not the number of 4's our
  # list has.
  num_items_before = 0
  for i, count in enumerate(counts):
      counts[i] = num_items_before
      num_items_before += count

  # Output list to be filled in
  sorted_list = [None] * len(the_list)

  # Run through the input list
  for item in the_list:

      # Place the item in the sorted list
      sorted_list[ counts[item] ] = item

      # And, make sure the next item we see with the same value
      # goes after the one we just placed
      counts[item] += 1

  return sorted_list

the_list = [3, 2, 4, 7, 1, 3, 8]
print(counting_sort(the_list, 9))
  