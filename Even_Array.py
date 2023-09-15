def is_strictly_even_array(arr):
    for num in arr:
        if num % 2 != 0:
            return False
    return True

# Example usage:
n=int(input())
arr1 =list(map(int,input().split()))

if is_strictly_even_array(arr1):
    print("True")
else:
    print("False")
