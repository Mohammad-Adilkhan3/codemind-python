def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_mega_prime(num):
    if not is_prime(num):
        return False
    for digit in str(num):
        if not is_prime(int(digit)):
            return False
    return True
number = int(input())
if is_mega_prime(number):
    print("Mega Prime")
else:
    print("Not Mega Prime")
