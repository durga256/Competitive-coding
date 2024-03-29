class Solution:
    res = []
    def solve(self,s,i,j,level,temp):
        if i == j+1 and level == 5:
            self.res.append(temp[1:])

        k = i
        #0-255 has less than 3 digits
        while k < i + 3 and k <= j:
            ad = s[i:k+1]

            if ((s[i]==0 and len(ad) > 1) or int(ad) > 255 or (ad[0] == '0' and len(ad) > 1)):
                return
            
            self.solve(s,k+1,j,level + 1, temp+'.'+ad)

            k += 1
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []
        self.solve(s,0,len(s)-1,1,"")
        return self.res