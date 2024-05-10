number = int(input("Enter the Number "))
c=0
for i in range(2,number):
    if number%i==0:    
        c=c+1
        break
    else:
        c=0
if(c==0):
    print(number,"is prime")
else:
    print(number,"is not prime")