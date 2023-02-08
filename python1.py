#Given a 4-digit positive integer, determine whether this number is divisible by all its digits.
def divisible_by_all_digits(number):
    if number < 1000 or number > 9999:
        return False
    
    num_str = str(number)
    for digit_str in num_str:
        digit = int(digit_str)
        if digit == 0 or number % digit != 0:
            return False
    
    return True

result = divisible_by_all_digits(1224)
print(result)
