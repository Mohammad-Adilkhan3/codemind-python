def is_disarium(number):
    num_str = str(number)
    n = len(num_str)
    sum_digits = 0
    
    for i in range(n):
        sum_digits += int(num_str[i]) ** (i + 1)
    
    return sum_digits == number

number = int(input())
if is_disarium(number):
    print("True")
else:
    print("False")
