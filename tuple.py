t1=(2,5,9,3,7,4)
t2=t1[::-1]
print("Reversed Tuple=",t2)

n=int(input("Enter tuple member:"))

for i in t1:
    if n==i:
        print("Element is present")
        break
else:
    print("Element is not present")

#convert list into tuple
l1=[2,5,9,8,4,6,1,7]
print(tuple(l1))

#Remove empty list from list of tuple
l2=[(5,9,3,7),(),(5,6,8,7)]
for i in l2:
    if i==():
        l2.remove(())
        print(l2)


