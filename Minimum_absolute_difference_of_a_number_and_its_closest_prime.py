def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_closest_prime(num):
    if is_prime(num):
        return num
    lower = upper = num
    while True:
        lower -= 1
        if is_prime(lower):
            return lower
        upper += 1
        if is_prime(upper):
            return upper

def min_absolute_difference(num):
    closest_prime = find_closest_prime(num)
    difference = abs(num - closest_prime)
    return difference


number = int(input())
minimum_difference = min_absolute_difference(number)
print(minimum_difference)
