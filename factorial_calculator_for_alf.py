# ========== PSEUDO CODE ==========
# - Printing 'FACTORIAL CALCULATOR FOR ALF'
print("FACTORIAL CALCULATOR FOR ALF")


# - Ask user to input a non-negative number
ask_user_a_number = int(input("Input a non-negative number:"))


# - Calculate the factorial of the user-defined integer using a loop.
def factorial(n):
    if n < 0:
        return "Invalid. Please enter a non-negative number."
    else:
        factorial = 1 
        for i in range(n):
            factorial *= i+1
        return factorial


# - Display the factorial result
result = factorial(ask_user_a_number)
print("The factorial of", ask_user_a_number, "is", result)
