#define a function accept an input of integer array. process the array to return the even_count : odd_count ration
def even_odd_ratio(arr):
    even_count = 0
    odd_count = 0
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count / odd_count if odd_count != 0 else "Cannot divide by zero."

# Example usage
arr = [2, 4, 6, 3, 7, 9, 11]
print(even_odd_ratio(arr))  # Output: 0.75


