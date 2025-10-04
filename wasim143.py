print("Enter 1 for check Odd or Even")
print("Enter 2 for check positive or non positive")
print("Enter 3 for simple Interest")
print("Enter 4 for find roots for quadratic equations")
n=int(input())
match n:
    case 1:
        a=int(input("Enter any number\n"))
        if a%2==0:
            print("Even")
        else:
            print("Odd")
    case 2:
        b=int(input("Enter any number\n"))
        if b>0:
            print("Positive")
        else:
            print("Non positive")
    case 3:
        print("Ente the value of p,r and t")
        p,r,t=int(input()),int(input()),int(input())
        print("Simple Interest is=",p*r*t/100)
    case 4:
        print("Enter the value of a,b and c")
        a,b,c=int(input()),int(input()),int(input())
        d=b**2-4*a*c
        if d>0:
            print("Real and Distict roots")
        elif d==0:
            print("Two real and equal roots")
        else:
            print("Imaginary roots")
    case _:
        print("Ivalid Input...")