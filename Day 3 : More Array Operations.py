def HeightChecker(nums):
  #define a counter and a second array which is a sorted version of the first one
  sec_nums = sorted(nums)
  count = 0
#loop through the second array as you count the values that are not matching between the two array
  for item in range(len(sec_nums)):
    if nums[item] != sec_nums[item]:
      #increment the counter
      count+=1
  return count


def findMaxConsecutiveOnes(nums):
  #hold values in the following variables
  longest_sequence, left, right, count_zeroes = 0, 0, 0, 0
  while right < len(nums):       #The span of iteration
    if nums[right] == 0:
      count_zeroes+=1            #Count appearance of zeroes           

    while count_zeroes ==2:      #When you hit two zeroes, the span is invalid, move the pointers and start again
      if nums[left] == 0:
        count_zeroes-=1
      left+=1
    longest_sequence = max(longest_sequence, right - left + 1)      #return the longest span of ones
    right+=1
  return longest_sequence
