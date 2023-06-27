def calculate_sum_odd_indices(integer, lst):
    odd_sum = 0

    for index in range(1, len(lst), 2):
        odd_sum += lst[index]

    return odd_sum

# Read an integer and a list of integers from the user
integer = int(input())
lst = list(map(int, input().split()))

# Calculate the sum of elements at odd indices
result = calculate_sum_odd_indices(integer, lst)

# Print the result
print(result)
