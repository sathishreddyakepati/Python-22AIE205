# Q3. Remove Duplicate Data

# Accept n integers from the user.

# Store them in a list.
# Remove duplicates using a set.
# Display the unique values.
# Display the number of unique values.

n = int(input("Enter no.of integers: "))
numbers = []
for i in range(0,n):
    num = int(input(f"Enter Integer{i+1}: "))
    numbers.insert(i,num)

unique = set(numbers)

Nunique = len(unique)

print(f"Unique values: {unique}")
print(f"No.of unique numbers: {Nunique}")
