# ========== PSEUDO CODE ==========
# - Printing 'PERFECT NUMBER DETERMINATOR FOR ALF'
print("PERFECT NUMBER DETERMINATOR FOR ALF")

# - Ask user for non-negative number
ask_user = int(input("Enter a non-negative number:"))

# - Checking if the entered integer is a Perfect Number using a loop
def is_perfect_number(value):
    if value <= 0:
        return False
    
    
    divisors_sum = 0 
    for i in range(1, value):
        if value % i == 0:
            divisors_sum += i

    return divisors_sum == value


result = is_perfect_number(ask_user)

if result:
    print(f"{ask_user} is a perfect number.")
else:
    print(f"{ask_user} is not a perfect number.")


# NOTE : You can use if-else statement or ternary operator to display the result.