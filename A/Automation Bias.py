def calculate_average(numbers):
    if len(numbers) == 0:
        return 0  # Handle the case of an empty list
    else:
        return sum(numbers) / len(numbers)

# Example data
data = [10, 15, 20, 25, 30]

# Calculate the average using the function
average = calculate_average(data)

# Assume we trust the function implicitly and don't verify its result
if average > 20:
    print("The average is greater than 20.")
else:
    print("The average is not greater than 20.")
