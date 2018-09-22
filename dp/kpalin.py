def is_palin(string):
    start=0
    end = len(string)-1
    count = 0
    while start<end:
        if string[start]!=string[end]:
            return False
        start+=1
        end-=1
    return True

def is_k_palin(string, n):
    #Code here
    if n<=0:
        return is_palin(string)
    if memo.get(string)==None:
        if is_palin(string):
            memo[string]= 1
        for i in range(len(string)):
            if is_k_palin(string[:i]+string[i+1:],n-1):
                memo[string]=1
        if memo.get(string)==None:
            memo[string]=0
    return memo[string]
memo= {}
print(is_k_palin("abcbedbbbbbaaaaaabcsdkjskjbksbkdjskjbs",2))