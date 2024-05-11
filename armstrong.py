number=int(input("enter number "))
n=number
sum=0
while n>0:
    r=n%10
    sum+=r**3
    n//=10

#print(sum)
if number==sum:
    print(number,"is armstrong number")
else:
    print(number,"is not armstrong number")


