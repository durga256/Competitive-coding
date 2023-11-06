class Solution:
    def check_d_empty(self, d):
        for i in d:
            if d[i] != 0:
                return False
        
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        d = {}
        for i in s1:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        window_size = len(s1)
        start = 0; end = 0
        while end < window_size:
            if s2[end] in d:
                d[s2[end]] -= 1
                if self.check_d_empty(d) and end-start+1 == window_size:
                    return True
            end += 1

        while end < len(s2):
            if s2[end] in d:
                d[s2[end]] -= 1
            if s2[start] in d:
                d[s2[start]] += 1
            if self.check_d_empty(d) and end-start == window_size:
                return True
            end += 1; start += 1

        return False