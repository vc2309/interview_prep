def reverse(string):
    print(string)
    if not len(string):
         return string
    i=0
    j=len(string)-1
    while i<j:
        string[i],string[j]=string[j],string[i]
        i+=1
        j-=1
    return string

def main():
    mystr=input("enter")
    print(reverse(list(mystr)))

if __name__ == '__main__':
    main()
