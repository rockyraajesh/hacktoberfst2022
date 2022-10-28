lis=[10, 78, 94, 45, 64]
def BubbleSort(N):
    N=len(lis)
    i,j,k,flag=0,1,0,True
    while(k<N and flag==True):
        i,j,flag=0,1,False
        while(j<N-k):
            if(lis[i]>lis[j]):
                lis[i],lis[j]=lis[j],lis[i]
                flag=True
            i=i+1
            j=j+1
        k=k+1
BubbleSort(lis)
print(lis)