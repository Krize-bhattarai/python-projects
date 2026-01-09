# lambda Function Example

numbers = [1, 2, 3, 4, 5]          # List of numbers

squared = list(                   # Convert result to a list
    map(                           # Apply function to each item
        lambda x: x * x,           # Take x and return x squared
        numbers                    # Loop through this list
    )
)

print(squared)                    

# Output: [1, 4, 9, 16, 25]