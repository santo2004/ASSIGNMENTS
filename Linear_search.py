def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return "not found"

print(linear_search([10, 15, 20, 30], 25))  