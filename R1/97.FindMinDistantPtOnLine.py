import sys
import math

class Solution:
    def constructLine(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def findPointOnLine(self, x1,y1):
        a = self.a; b = self.b; c = self.c

        a = -1*a/b; c = -1*c/b; b = 1
        new_slope = -1/a
        q = 1; p = new_slope
        r = q*y1 - p*x1
        # print(q,y1,p,x1)
        # print(r)

        x = (r-c)/(a-p)
        y = ((a+p)*x + c+ r)/(b+q)
        return [x, y]

    def findOptimumCost(self, line, n, points):
        # code here
        self.constructLine(line[0], line[1], line[2])
        res = []
        for i in points:
            res.append(self.findPointOnLine(i[0],i[1]))

        min_x = min_y = sys.maxsize
        max_x = max_y = -sys.maxsize

        for i in res:
            min_x = min(min_x, i[0])
            max_x = max(max_x, i[0])
            min_y = min(min_y, i[1])
            max_y = max(max_y, i[1])

        slope_positive_flag = False

        if -1*self.a/self.b > 0:
            slope_positive_flag = True

        if slope_positive_flag:
            i = min_x; j = min_y
        else:
            i = max_x; j = min_y
        lengths_arr = []
        while i <= max_x and j <= max_y:
            total_len = 0
            for k in points:
                temp = self.findLength2Points(i,j, k[0], k[1])
                total_len += temp
            lengths_arr.append(total_len)
            if slope_positive_flag:
                i += 1; j += 1
            else:
                i -= 1; j += 1

        return round(min(lengths_arr),2)
            
    def findLength2Points(self,x1,y1,x2,y2):
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))



n = Solution()
line = [1,-1,-3]
points = [[-3, -2], [-1, 0], 
            [-1, 2], [1, 2], [3, 4]]

# line = [2,1,4]
# points = [[-1, 2], [1, 3],[2, 4]]

line = [3,4,4]
points = [[-1, 4], [-1, 0]]

print(n.findOptimumCost(line, len(points), points))


