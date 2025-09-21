# pattern_drawing.py

# Step 1: Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Step 2: Use a while loop for rows
row = 0
while row < size:
    # Step 3: Use a for loop for columns
    for col in range(size):
        print("*", end="")  # Print a star without a newline
    print()  # Move to the next line after finishing one row
    row += 1
