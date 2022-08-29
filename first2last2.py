s=input("Enter string :")
n=len(s)

if n==2:
    print(s+s)
elif n<2:
    print("Empty string")
else:
    print(s[:2]+s[n-2:])
