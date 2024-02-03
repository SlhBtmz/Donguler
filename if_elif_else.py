number = int(input("Please anter a number: "))
factorial = 1

if number < 0: print(f"the number you entered is negative and has no factorial.")
elif number == 0: print(f"the factorial of {number} is zero")
else: 
    for x in range(1, number+1):
        factorial = factorial * x
    print(f" the factorial of {number} is {factorial}")


    