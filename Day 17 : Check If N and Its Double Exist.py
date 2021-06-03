#Inspired by https://atharayil.medium.com/check-if-n-and-its-double-exist-day-54-python-2ca9007d132d

import collections

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dict_number = collections.defaultdict(int)
        for i in range(len(arr)):
            if 2 * arr[i] in  dict_number or arr[i] / 2 in dict_number:
                return True
            else:
                dict_number[arr[i]] = i
        return False
