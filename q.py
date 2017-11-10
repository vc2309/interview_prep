import time
class Solution(object):

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n%2==0:
            l=n/2
        else:
            l=(n+1)/2
        s=n-l
        splits=[]
        prods=[s*l]
        self.breakup(l,splits,prods)
        self.breakup(s,splits,prods)
        
        print(splits)
        prod=1
        for i in splits:
            if i!=None:
                prod=prod*i
        prods.append(prod)
        print(prods)
        return max(prods)
    
    def breakup(self,x,splits,prods):
        if x<=3:
            return x
        else:
            if x%2==0:
                l=x/2
            else:
                l=(x+1)/2
            s=x-l
            if s==1 or l==1:
                return x
            else:
                prod=1
                for i in splits:
                    if i!=None:
                        prod=prod*i
                prods.append(prod)
                splits.append(self.breakup(s,splits,prods))
                splits.append(self.breakup(l,splits,prods))
        
def main():
    sol=Solution()
    n=int(input("put\n"))
    start=time.time()
    sol.integerBreak(n)
    end=time.time()
    print(end-start)

if __name__ == '__main__':
    main()