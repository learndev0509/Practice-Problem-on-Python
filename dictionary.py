t1=[("dev",10),("devansh",40),("man",20),("arjun",30)]
d1=dict(t1)
print("converted dictionary is :")
print(d1)
print("*"*50)
d2=sorted(d1.values())
print("sorted dictionary is :")
print(d2)
print("*"*50)
d3={"john":60,"ana":50}
d4={"smith":70,"david":80,"smith":70}
d5={}

for i in (d1,d3,d4):
    d5.update(i)
print("new Dictionary is :")
print(d5)
print("*"*50)
def check_key(i):
    
        if i in d5:
            print("given key is present")
            
        else:
            print("given key is not present")


check_key("john")

print("*"*50)
d6={}
for i in range(1,16):
    d6[i]=i**2
print("numbers as a key:")
print(d6)
print("*"*50)

d7={'dev': 10, 'devansh': 40, 'man': 20, 'arjun': 10, 'john': 60, 'ana': 50, 'smith': 10, 'david': 80}
x=list(d7.values())
print("values of dictionary :")
print(x)
l1=[]
for i in x:
    if i not in l1:
        l1.append(i)
print("unique values in dictionary :")
print(l1)
print("*"*50)


print("sorted list :")
s=sorted(l1)
print(s)
n=len(l1)
print("Highest 3 values :")
print(l1[n-3:])
print("*"*50)


