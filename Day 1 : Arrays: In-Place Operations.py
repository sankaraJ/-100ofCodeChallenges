def replaceElementwithGreatestontheright(nums):
  if len(nums) == 1:
    return [-1]
  greatest_ = nums[-1]
  for item in range(len(nums)-2, -1, -1):
    now_ = nums[item]
    nums[item] = greatest_
    if now_ > greatest_:
      greatest_ = now_
  nums[-1] = -1
  return nums
