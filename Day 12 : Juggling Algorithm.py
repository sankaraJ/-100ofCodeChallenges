#Implementing the Juggling algorithm
#Divide the array to be rotated into sets
#Number of sets will be determined by the GCD of n and k
#Have two loops, the outer one that will go through all the sets and an inner one that will move elements within the sets
#Outer loop i will start at 0 and stop when its less than number of sets
#Values --Elements in the inner loop represented by A[j] will be determined by A[(j+k) % n]
#% is modulo --> is an arithmetic operator that returns the reminder after dividing two numbers 
#Inner loop ends when d == i
#Increment the value of i to move on to the next set/cycle
#Inspired by https://www.youtube.com/watch?v=utE_1ppU5DY&t=5s&ab_channel=CodeWhoop
#and https://www.geeksforgeeks.org/array-rotation/
#Import a necessary library math
import math
def leftrotate(arr, d, n):
  d = d % n
  g_c_d = math.gcd(d, n)
  for i in range(g_c_d):
    temp = arr[i]
    j = i

    while(1):
      k = j + d
      if k >= n:
        k = k - n
      if k == i:
        break
      arr[j] = arr[k]
      j = k
      arr[j] = temp
#The function to return elements of the array
def printArray(arr):
  for i in range(len(arr)):
    print("% d" % arr[i], end =" ")
