def binary_search(list, item):
  ''' a function to find a value in a list using a binary search and return index'''

  sort_list = sorted(list)  # sort the list incase it isn't already sorted

  # set low and high to keep track of where the search is

  low = 0
  high = len(list) - 1  # n - 1

  #  while the item hasn't been found
  while low <= high:
    mid = (low + high) // 2  # (0 + len(list) - 1) // 2 (round down)
    guess = sort_list[mid]  # find the middle value in the list

    if guess == item:
      return mid  # found the item
    if guess > item:
      high = mid - 1  # guess too high, item will be in the bottom half of the list
    else:
      low = mid + 1  # guess too low, item will be in the upper half of the list

  return None

my_list = [5, 7, 9, 11, 1, 3]
other_list = [1, 3, 5, 7, 9, 11, 13]

print(binary_search(my_list, 7))
print(binary_search(other_list, 5))

'''
Exercises

1.1 Suppose you have a sorted list of 128 names, and you're searching through it using binary search. What's the maximum number of steps it would take?

1) 128 / 2 = 64 
2) 64 / 2 = 32 
3) 32 / 2 = 16 
4) 16 / 2 = 8
5) 8 / 2 = 4
6) 4 / 2 = 2
7) 2 / 2 = 1

1.2 Suppose you double the size of the list. What's the maximum number of steps now?

1) 256 / 2 = 128
2) 128 / 2 = 64 
3) 64 / 2 = 32 
4) 32 / 2 = 16 
5) 16 / 2 = 8
6) 8 / 2 = 4
7) 4 / 2 = 2
8) 2 / 2 = 1

'''