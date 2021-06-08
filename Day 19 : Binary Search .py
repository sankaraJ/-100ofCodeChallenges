#Inspired by https://leetcode.com/problems/binary-search/
#Nums must strictly be increasing
def search(nums, target):
  left, right = 0, len(nums) - 1
  while left <= right:
    pivot = left + (right - left) // 2
    if nums[pivot] == target:
      return pivot
    if target < nums[pivot]:
      right = right - 1
    else:
      left = left + 1
  return -1
