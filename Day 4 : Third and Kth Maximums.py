def thirdMaxElemnt(nums):
  #create a set to hold maximum numbers
  max_nums = set()
  #Loop through as you store maximum numbers and delete the minimum values and retain only 3 values at any time
  for item in nums:
    max_nums.add(item)
    if len(max_nums) > 3:
      max_nums.remove(min(max_nums))
      #return the minimum of the three values
  if len(max_nums) == 3:
    return min(max_nums)
    #otherwise return the maximum of the set
  return max(max_nums)
