n=int(input("Enter the year\n"))
if n%400==0:
    print("Leap Year")
elif n%4==0 and n%100!=0:
    print("Leap Year")
else:
    print("Not Leap Year")