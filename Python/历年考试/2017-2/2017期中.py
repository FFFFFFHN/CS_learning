def GetIntNumers(s):
    a=s.split()
    # b=map(int,a)
    # c=list(b)
    # res=[int(str(c[2*i])+str(c[2*i+1])) for i in range(len(c)//2)]
    # return res
    return [int(a[2*i]+a[2*i+1]) for i in range(len(a)//2)]

def DeleteRepeatedNumbers(a):
    return list(set(a))
    # a=a[::]
    # for i in range(len(a)-1,0,-1):
    #     if a.count(a[i])>1:
    #         a.pop(i)
    # return a

def MySort(a):
    a.sort(key=lambda x:int(str(x)[-1])+int(str(x)[-2]),reverse=True)
    return a

def Display(a,width=10, cols=2, direct=1):
    if direct==1:   #右对齐
        ft="%"+str(width)+"d"
    else:
        ft="%-"+str(width)+"d"
    for i in range(len(a)):
        print(ft%a[i],end='')
        if (i+1)%cols==0:
            print()
    if len(a)%cols!=0:
        print()

def GetMaxMinAver(a):
    a=a[::]

    res=[]
    res.append(max(a))
    res.append(min(a))
    res.append(sum(a)/len(a))
    return res