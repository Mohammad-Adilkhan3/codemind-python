def find_last_even_index(arr):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] % 2 != 0:
            return i
    # If no even element is found, you can return -1 or raise an exception.
    return -1

# Example usage:
n=int(input())
l=list(map(int,input().split()))
last_even_index = find_last_even_index(l)

if last_even_index != -1:
    print(last_even_index)
else:
    print("No even element found in the list.")
