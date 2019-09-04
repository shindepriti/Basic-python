n = int(input("Enter the number of rows you want to print?"))  
  
for i in range(1,n):  
    print(i)  
    for j in range(0,i+1):  
        print(j,end="") 
