def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0

    upper_bound = None

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        iterations += 1

        if guess == target:
            return iterations, guess
        elif guess < target:
            low = mid + 1
        else:
            upper_bound = guess
            high = mid - 1

    return iterations, upper_bound

# Example usage:
arr = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
target = 1.2
iterations, upper_bound = binary_search(arr, target)
print("Iterations:", iterations)
print("Upper bound:", upper_bound)
