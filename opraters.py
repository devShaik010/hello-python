# MINI CALCULATER using  pyhton aeithmetics opraters 
num1=int(input("ENTER FORST NUMBER   : "))
num2=int(input("ENTER SECONDE NUMBER : "))
num3=int(input("{ SALECT OPRATER } \n 1. FOR ADDITION \n 2. FOR SUBTRACTION \n 3. FOR MULTIPLICATION \n 4. FOR DIVISION \n 5. FOR MODULUS \n 6. FOR EXPONENTIATION \n 7. FOR FLOOR DEVISION \n CHOOSE THE GIVEN OPTION :  "))
if num3==1:
    print(" SUM OF TWO NUMBER IS  : ",num1+num2)
elif num3==2:
    print(" SUBTRACTION OF TWO NUMBER IS  : ",num1-num2)
elif num3==3:
    print(" MULTIPLICATION OF TWO NUMBER IS  : ",num1*num2) 
elif num3==4:
    print(" DIVISION OF TWO NUMBER IS  : ",num1/num2)    
elif num3==5:
    print(" MODULUS OF TWO NUMBER IS  : ",num1%num2)
elif num3==6:
    print(" EXPONENTIO OF TWO NUMBER IS  : ",num1**num2)        
elif num3==7:
    print(" FLORR DIVISION OF TWO NUMBER IS  : ",num1//num2)
else:
    print(" PLEAS SALECT A GIVEN OPTION ONLY ")
print("\n            creat by shaik abrar ~~~")            
    