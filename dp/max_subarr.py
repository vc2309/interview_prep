class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp=[[-1 for i in B] for j in A]
        mx=0
        m=len(A)-1
        n=len(B)-1
        dp[m][n]=self.check(A,B,dp,mx)
        print(dp)
        for i in dp:
            for j in i:
                if mx<j:
                    mx=j
        return mx
    def check(self,A,B,dp,mx):
        m=len(A)-1
        n=len(B)-1
        if m<0 or n<0:
            return -1
        elif m==0 or n==0:
            if A[m]==B[n]:
                dp[m][n]=1
            else:
                dp[m][n]=0
        else:
            if dp[m][n]==-1:
                if A[m]==B[n]:
                    dp[m][n]=1+self.check(A[:m],B[:n],dp,m)
                    dp[m-1][n]=self.check(A[:m],B,dp,m)
                    dp[m][n-1]=self.check(A,B[:n],dp,m)
                    
                else:
                    dp[m][n]=0
                    dp[m-1][n]=self.check(A[:m],B,dp,m)
                    dp[m][n-1]=self.check(A,B[:n],dp,m)
        return dp[m][n]


def main():
	s=Solution()
	A=[0,0,0,0,0,0,0,1,0,0]
	B=[0,0,0,0,0,0,1,0,0,0]
	s.findLength(A,B)

if __name__=='__main__':
	main()
