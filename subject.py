maths=int(input("Enter Your Maths Marks:"))
sci=int(input("Enter Your science marks:"))
eng=int(input("Enter Your English marks:"))
geo=int(input("Enter Your geomentry marks:"))
hin=int(input("Enter Your hindi marks:"))

print('''enter Your choice
1:total
2:averge
3:percentage
4:grade
''')

option = 1
option = int(input("Enter your Choice"))
if option!=0:
    
    if option==1:
          total=maths+sci+eng+geo+hin
          print("total marks=",total)
    elif option==2:
           averge=maths+science+eng+geo+hin/5
           print("Averge marks=",averge)
    elif option==3:
          percentage=(maths+sci+eng+geo+hin/500)*100
          print("marks percentage=",percentage)
    elif option==4:
        avg=maths+sci+eng+geo+hin/5
        if(avg>=90):
         print("Grade:A")
        elif(avg>=80&avg<90):
         print("Grade:B")
        elif(avg>=70&avg<80):
         print("Grade:c")
        elif(avg>=60&avg<70):
         print("Grade:D")
        else:
         print("grade:F")

         

else:
      print("Do You Want To Continiue(y/n)")
      
