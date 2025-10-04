print("The value of a,b and c")
a,b,c=int(input()),int(input()),int(input());
d=b*b-4*a*c
if d>0:
    print("Real and distinct roots")
elif d==0:
    print("Two real and equal roots")
else:
    print("Imaginary roots")