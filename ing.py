s=input("Enter string:")
n=len(s)



if n>2:
    
    if s.endswith("ing"):
        print(s[0:n-3]+"ly")
    else:
        print(s+"ing")
else:
    print(s)
