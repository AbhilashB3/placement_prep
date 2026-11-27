a=[2,7,5,4,9,1,0,7,6]
target=7
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==target:
            print("index: ",a[i],a[j])