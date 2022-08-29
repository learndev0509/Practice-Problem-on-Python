s=input("Enter string:")

p=s.find("poor")
n=s.find("not")
#print(p)
if int(n>p):
    print(s.replace("not","good").replace("poor","good"))
