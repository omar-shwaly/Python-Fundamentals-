password ="omar@1234"
tries=3


inputPassword= input("Enter Your Password  ").strip().lower()
while inputPassword !=password:
         tries-=1
         
         if tries==0 :
            
            print("Account Looked ")
    
            break
         print(f"Wrong Password , {tries} Chance Left")
         inputPassword= input("Enter Your Password  ").strip().lower()


if inputPassword==password: 
               
  print("Welcom")

