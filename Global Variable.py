def addition (a,b):
    global result
    result=a+b
    return result


result=0
Number1=int(input("Please enter the first number: "))
Number2= int(input("Please enter the econd number: "))
Outcome=addition(Number1,Number2)
print("Total Outcome: ", Outcome)   
