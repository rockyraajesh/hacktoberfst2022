lis=[10, 8, 6, 11, 24]
def insertion_sort(lis):
    screen=1
    N=len(lis)
    while(screen<N):
        safe=lis[screen]
        for i in range(screen-1,0,-1):
            if(safe>lis[i]):
                break
            else:
                lis[i+1]=lis[i]
    screen=screen+1
    lis[screen]=safe
insertion_sort(lis)
print(lis)

# some problem
