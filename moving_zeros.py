a=[0,1,9,0,6,0,9,3,2,0,1]
zeros=[]
non_zeros=[]
result=[]
for i in a:
    if i==0:
        zeros.append(i)
    else:
        non_zeros.append(i)
result=non_zeros+zeros
print(result)