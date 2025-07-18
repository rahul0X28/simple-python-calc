print("1 -Add")
print("2-subtraction")
print("3-multiplication")
print("4-division")

option=int(input("enter the option:"))
result=0

if option in[1,2,3,4]:
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    if option ==1:
        result=num1+num2
    elif(option==2):
        result=num1-num2
    elif(option==3):
        result=num1*num2
    elif(option==4):
        result=num1//num2
else:
    print("Invalid option")


print("The result of the operation is ",result)
    
            
        
        
        
           
