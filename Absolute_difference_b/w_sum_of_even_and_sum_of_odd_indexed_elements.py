def calculate_difference(integer, lst):
    odd_sum = 0
    even_sum = 0

    for index, num in enumerate(lst):
        if index % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return  even_sum - odd_sum

# Read integer and list from user
integer = int(input())
lst = list(map(int, input().split()))

# Calculate the difference
result = calculate_difference(integer, lst)

# Print the result
print(result)
