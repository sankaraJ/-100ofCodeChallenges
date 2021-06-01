#Rearranging elements in an Array
#Inspired by https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/

def Rearrange(a):
  #sort the array
  a=sorted(a)
  k=0
  #loop through. If the element is less than 0 and the next element is greater than or equal to zero
  #increment the counter and do nothing
  for i in range(len(a)):
    if a[i] < 0 and a[i+1] >= 0:
      k = i+1
      break
  #loop through. If the element is less than 0 and the index is not even number, swap the elements
  #increment the counter
  for i in range(len(a)):
    if a[i] < 0 and i % 2 != 0:
      a[i], a[k] = a[k], a[i]
      k += 1
  return a
