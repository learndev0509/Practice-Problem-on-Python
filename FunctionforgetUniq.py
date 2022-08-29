
l1=[1,2,5,1,8,5,2]
l2=[]

def unique():
    for i in l1:
        if i not in l2:
            l2.append(i)
    print(l2)

unique()
