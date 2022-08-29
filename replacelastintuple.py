l1=[1,2,5,4,5,2,1]
l2=[]



for i in l1:
    for j in range(i+1,(len(l1))):
        if l1[i]==l1[j]:
            print("repeated number is: ",l1[j])
