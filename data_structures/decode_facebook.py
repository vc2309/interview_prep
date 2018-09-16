#code

def isInt(a):
    try:
        a=int(a)
        return True
    except ValueError:
        return False

def digits(a):
    # print(a,"digits")
    i=0
    while a>0:
        a=int(a/10)
        i+=1
    return i

def decode(mystr):
    mystr=list(mystr)
    parenth = []
    i=0
    while i<len(mystr):
        # print(mystr)
        if mystr[i]=="[":
            ctr=i-1
            while isInt(mystr[ctr]) and ctr>=0:
                ctr-=1
            # print(mystr)
            print(ctr,i)
            num=int(("").join(mystr[ctr+1:i]))
            parenth.append((ctr+1,num))
            print(parenth)
        elif mystr[i]=="]":
            prev = parenth.pop()
            num = prev[1]
            start = prev[0]
            
            
            numdigits = digits(num)
            substr = mystr[start+numdigits+1:i]*num
            ctr=0
            print(start,numdigits)
            for j in range(numdigits+1):
                print(start+j,mystr[start+j])
                mystr[start+j]="*"
                ctr=j

            mystr[start+ctr+1]="*"
            mystr[i]="*"
            lhs = mystr[:start+2]
            (lhs.extend(substr))
            lhs.extend(mystr[i:])
            print(lhs)
            # print((lhs.extend(substr)))
            mystr=lhs
        i+=1
    mynewstr = ""
    print(mystr)
    for i in mystr:
        if i!="*":
            mynewstr+=i
    print(mynewstr)
# mystr = input()
decode("a1[b]")