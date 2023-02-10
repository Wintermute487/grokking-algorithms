def binary_search(list, item) :
'''A function for finding an item in a sorted list using a binary search'''
  low = 0 #the lower half of the list
  high = len(list) - 1 #the upper half of the list
  
  while low <= high :
    mid = (low + high) / 2 #the first guess will split the list in half, each subsequent run will half the resulting list until the item is found 
    guess = list(mid)
    if guess == item :
      return mid #search stops if correct
    if guess > item :
      high = mid - 1 #if guess is too high, mid value - 1, high becomes mid - 1, is added to low, new value then divided by 2, equals new mid
    else :
      low = mid + 1 #if guess is too low, mid value + 1, low becomes mid + 1, is added to high, new value then divided by 2, equals new mid
  return None

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
