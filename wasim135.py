print("Enter any three numbers")
a,b,c=int(input()),int(input()),int(input())
if a>b and a>c:
    print("Greatest Number is=",a)
elif b>a and b>c:
    print("Greatest Number is=",b)
else:
    print("Greatest Number is=",c)