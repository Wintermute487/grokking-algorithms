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
