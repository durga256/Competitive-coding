import sys
import math

sys.stdin = open('CodeForces/input.txt', 'r')
def get_input():
    T = int(input())
    tc = []
    for i in range(T):
        line = list(map(int, input().split()))
        n = int(input())
        points = []
        for _ in range(n):
            points.append(list(map(int, input().split())))
        tc.append([line, points])
    return tc

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
        #y = ((a+p)*x + c+ r)/(b+q)
        y = a*x+c
        # print(p,b,a,q)
        # x  = ((-r*b)-(c*q))/(p*b+a*q)
        # y = (p*x+r)/q
        return [x, y]

    def findOptimumCost(self, line, n, points):
        # code here
        self.constructLine(line[0], line[1], line[2])
        res = []
        for i in points:
            res.append(self.findPointOnLine(i[0],i[1]))

        min_x = min_y = sys.maxsize
        max_x = max_y = -sys.maxsize
        #print(res)
        for i in res:
            min_x = min(min_x, i[0])
            max_x = max(max_x, i[0])
            min_y = min(min_y, i[1])
            max_y = max(max_y, i[1])

        #print(min_x, min_y, max_x, max_y)
        # WE know our answer is somewhere around mid-point. Spread to left and right from mid
        #print('mid point', (min_x+max_x)/2, (min_y+max_y)/2)
        #print('eqn satisfy',self.a*((min_x+max_x)/2)+self.b*((min_y+max_y)/2)+self.c)

        i = min_x; j = min_y
        lengths_arr = []
        min_so_far = 100000000
        while i <= max_x and j <= max_y:
            total_len = 0
            for k in points:
                temp = self.findLength2Points(i,j, k[0], k[1])
                total_len += temp
            lengths_arr.append(total_len)
            if total_len < min_so_far:
                min_so_far = total_len
                ans = [i,j]
            i += 0.1; j = (-self.c-self.a*i)/self.b
        #print(lengths_arr)
        #print(ans)
        # temp = 0
        # for k in points:
        #     temp += self.findLength2Points((min_x+max_x)/2,(min_y+max_y)/2, k[0], k[1])
        # print('Distance from mid pt', temp)
        # return temp
        print(round(min(lengths_arr),2), ans, 'mid point: ', (min_x+max_x)/2, (min_y+max_y)/2, min_x, min_y, max_x, max_y)
            
    def findLength2Points(self,x1,y1,x2,y2):
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))



n = Solution()
tc = get_input()
for i in tc:
    line = i[0]
    points = i[1]
    n.findOptimumCost(line, len(points), points)


import sys

sys.stdin = open('CodeForces/input.txt', 'r')

def get_input():
    T = int(input())
    tc = []
    for i in range(T):
        line = list(map(int, input().split()))
        n = int(input())
        points = []
        for _ in range(n):
            points.append(list(map(int, input().split())))
        tc.append([line, points])
    return tc


class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_slope(self):
        return -self.a/self.b

    def distance_two_points(self,x1,y1,x2,y2):
        return ((x2-x1)**2+(y2-y1)**2)**0.5
    
    def intersection_on_line(self,x1,y1):
        a = self.a
        b = self.b
        c = self.c
        c = -c/b; a = -a/b; b = 1

        q = 1; p = -1/a
        r = q*y1 - p*x1
        x = (c-r)/(p-a)
        y = p*x + r
        return (x,y)
    
    def find_boundaries(self, points):
        max_x = max_y = -1000000
        min_x = min_y = 1000000
        for i in points:
            x, y = self.intersection_on_line(i[0], i[1])
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        return (min_x, min_y, max_x, max_y)

tc = get_input()
for i in tc:
    L = Line(i[0][0], i[0][1], i[0][2])
    points = i[1]
    slope = L.get_slope()
    l_x, l_y, h_x, h_y = L.find_boundaries(i[1])
    ans = 100000000
    res = [0,0]
    # WE know our answer is somewhere around mid-point. Spread to left and right from mid
    mid_x = (l_x+h_x)/2; mid_y = (l_y+h_y)/2
    #spread left
    while mid_x >= l_x and mid_y >= l_y:
        total_len = 0
        for x,y in points:
            total_len += L.distance_two_points(mid_x,mid_y,x,y)
        if total_len > ans:
            break
        ans = total_len
        res = [mid_x, mid_y]
        mid_x -= 0.1; mid_y = slope*mid_x-(L.c/L.b)
    mid_x = (l_x+h_x)/2; mid_y = (l_y+h_y)/2
    #spread right
    while mid_x <= h_x and mid_y <= h_y:
        total_len = 0
        for x,y in points:
            total_len += L.distance_two_points(mid_x,mid_y,x,y)
        if total_len > ans:
            break
        ans = total_len
        res = [mid_x, mid_y]
        mid_x += 0.1; mid_y = slope*mid_x-(L.c/L.b)

    print(ans, res)