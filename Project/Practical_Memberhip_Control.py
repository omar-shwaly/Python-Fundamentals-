#List Contains Admain

admins = ["Ahmed","Omar","Osama","Sammeh","Sharlok"]

name=input("Enter Your name") .strip().capitalize()




if  name in admins  :
        

   print(f"Hello {name} Welcome Back")

   option= input("Delet Or Ubdate Your Name ") .strip().capitalize()


   if option in ('Ubdate' , 'U'):
 
              New_Name= input("Enter your theNewNAame")
 
              admins[admins.index(name)]= New_Name
 
              print("Name Ubdated Successfully")
 
              print(admins)


   elif option in ('Delete','D') :

         admins.remove(name)
    
         print("Name Dleted Successfully")

         print(admins)


   else:
          print("Wrong option")
          
          
          
else:

          status= input("You Are Not Admin , Add You : Y,N ").strip().capitalize()

    
if status in ('Yes','Y'):
      
           print("Name Add Successfully")
   
           admins.append(name)


           print(admins)

else:
           print("You Are Not Added")
      