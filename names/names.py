import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# QUESTION ONE: what is the runtime complexity or original function?

# for name_1 in names_1:  runs O(n) times (linear - directly proportional to number of names in list)
#    for name_2 in names_2:  runs O(n) times
#        if name_1 == name_2:  constant time O(1) 
#            duplicates.append(name_1)  constant time O(1) 

# runtime complexity = O(n) * O(n) 
#                    = O(n^2) - Quadratic - directly proportional to square of n     


# QUESTION TWO: Replace the nested for loops below with your improvements

# <------ OPTION ONE: create binary search tree out of names_1 ------>
# for every name in names_2, call contains method on bst passing name
# if contains returns True, append name to duplicates array
# runtime: 0.20003294944763184 seconds

# (copied and pasted same Binary Search Tree class I worked on on Wednesday into bst file)
from bst import BinarySearchTree

# pass in the first name in names_1 as initial root node of BST
names_1_bst = BinarySearchTree(names_1[0])
# insert new node into BST for every name in names_1 except the first (already passed this in as the root node)
for name in names_1[1:]: 
    names_1_bst.insert(name)

# for every name in names_2, call contains method on bst passing in the name
for name in names_2:
    # if bst contains it, append it to duplicates array
    if names_1_bst.contains(name): duplicates.append(name)



#  <------ OPTION TWO: Use regular binary search to compare every name in names_1 with every name in names_2 ------>
# names_2 must be sorted alphabetically first because binary search will need perform comparison on every iteration to see if name at 
# current index is alphabetically higher or lower 
# runtime = 0.14918088912963867 seconds


def recursive_binary_search(array, left, right, name):
  while right >= left:
    mid = round(left + (right - left)/2)
    # if name at middle index == name we are looking for, 
    if array[mid] == name:
      # append the name to duplicates array
      duplicates.append(name) 
    # if name at current index is alphabetically lower than the name we're looking for,
    # eliminate LHS of array -> if it exists it must be on the RHS
    elif array[mid] < name:
      return recursive_binary_search(array, mid + 1, right, name)
    # if name at current index is alphabetically higher than the name we're looking for,
    # eliminate RHS of array -> if it exists it must be on the LHS
    elif array[mid] > name:
      return recursive_binary_search(array, left, mid - 1, name)
    # else name is not duplicate -> return False
    return False

# sort names_2 alphabetically
names_2 = sorted(names_2)

# for every name in names_1
for name in names_1: 
    # perform binary search, passing in alphabetically ordered names_2 as array to check against and current name as the target
    recursive_binary_search(names_2, 0, len(names_2)- 1, name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
