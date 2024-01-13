arr = [1, 3, 3, 1, 2]
from collections import Counter

def f():
    def isMajority(k, n):
        d = Counter(arr)
        if d[k] > n/2:
            return True
        return False
    #Moore's works with O(1) space when you dont check if it is majority
    #That is it is O(1) SC if guaranteed majority
    count = 0
    for i in arr:
        if count == 0: candidate = i
        if i == candidate: count += 1
        else: count -= 1

    if isMajority(candidate, len(arr)): return candidate
    return -1
    

f()
