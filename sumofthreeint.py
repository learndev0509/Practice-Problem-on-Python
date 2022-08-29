A=int(input("Enter number:"))
B=int(input("Enter number:"))
C=int(input("Enter number:"))
sum=A+B+C
#print(sum)

if (A==B or B==C or C==A):
    print("sum=0")
else:
    print("sum=",sum)
