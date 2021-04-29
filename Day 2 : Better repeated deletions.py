def movezeroesToTheEnd(nums):
  length_ = nums.count(0)
  for item in range(length_):
    nums.remove(0)
    nums.append(0)
  return nums


def sortArrayByParity(nums):
  nums.sort(key = lambda x: x%2 )
  return nums

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
