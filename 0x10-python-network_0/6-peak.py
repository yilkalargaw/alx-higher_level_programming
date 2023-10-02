#!/usr/bin/python3
"""Find peak in list_of_integers using linear search algorithm"""

def find_peak(lst):
  low = 0
  high = len(lst) - 1
  while low <= high:
    mid = (low + high) // 2
    if ((mid == 0 or lst[mid] >= lst[mid - 1]) and
        (mid == len(lst) - 1 or
         lst[mid] >= lst[mid + 1])):
      return lst[mid]
    elif lst[mid] < lst[mid - 1]:
      high = mid - 1
    else:
      low = mid + 1
  return None

# print(find_peak([1, 2, 4, 6, 3]))
# print(find_peak([4, 2, 1, 2, 3, 1]))
# print(find_peak([2, 2, 2]))
# print(find_peak([]))
# print(find_peak([-2, -4, 2, 1]))
# print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
