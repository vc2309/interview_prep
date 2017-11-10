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
        prods={}
        prods[n]=self.breakup(s,prods)*self.breakup(l,prods)
        # self.breakup(l,prods)
        # self.breakup(s,prods)
        
        # print(splits)
        # prod=1
        # for i in splits:
        #     if i!=None:
        #         prod=prod*i
        # prods.append(prod)
        print(prods)
        return max(prods)
    
    def breakup(self,x,prods):
        if prods.get(x)==None:
            if x<=3:
                prods[x]=x
            else:
                if x%2==0:
                    l=x/2
                else:
                    l=(x+1)/2
                s=x-l
                if s==1 or l==1:
                    return x
                else:
                    # prod=1
                    # for i in splits:
                    #     if i!=None:
                    #         prod=prod*i
                    # prods[x]=prod
                    prods[x]=(self.breakup(s,prods))*(self.breakup(l,prods))
        return prods[x]
        
def main():
    sol=Solution()
    n=int(input("put\n"))
    start=time.time()
    sol.integerBreak(n)
    end=time.time()
    print(end-start)


if __name__ == '__main__':
    main()
    