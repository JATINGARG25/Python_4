a = int(input("Enter the number:\n"))
prime = True
for i in range(2,a):
    if(a%i==0):
        prime = False
        break

if prime:
    print("The number is prime")
else:
    print("The number is not prime")