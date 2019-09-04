num=int(input("Enter The Number"))

for i in range(2,num):
    if(num % i)==0:
        print(num,"is not prime Number")
        break
    else:
        print(num,"is prime number")
        break
