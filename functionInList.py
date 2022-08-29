l=[45,83,94,35,86]

def Larger():
    l.sort()
    l1=l[-1]
    print("Max Number is :",l1)

def Smaller():
    l.sort()
    l1=l[-5]
    print("Min Number is :",l1)

def Summation():
    
    s=sum(l)
    print("Total sum is :",s)

Larger()
Smaller()
Summation()
