# Inspired by https://leetcode.com/problems/guess-number-higher-or-lower/discuss/1259722/Python3-dollarolution-(memory-99.87)
class Solution:
    def guessNumber(self, n: int) -> int:
        l, h = 1, n+1
        while True:
            m = int((l+h)/2)
            if guess(m) == 0:
                return m
            elif guess(m) == -1:
                h = m
            else:
                l = m
