def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_next_prime_palindrome(number):
    number += 1
    while True:
        if is_prime(number) and is_palindrome(number):
            return number
        number += 1
number = int(input())
next_prime_palindrome = find_next_prime_palindrome(number)
print(next_prime_palindrome)
