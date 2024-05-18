# Get input values from the user
try:
    books = int(input("Enter the number of books: "))
    pens = int(input("Enter the number of pens: "))
    bags = int(input("Enter the number of bags: "))
    total_price = int(input("Enter the total price: "))
except ValueError:
    print("Invalid input. Please enter integers for the quantities and total price.")
    exit()

# Create a string containing the input values separated by commas
input_values = f"{books}, {pens}, {bags}, {total_price}"

# Define the filename where you want to save the data
file_name = "inventory_data.txt"

try:
    # Open the file in write mode ('w')
    with open(file_name, 'w') as file:
        # Write the input values to the file
        file.write(input_values)
    
    print(f"Input values saved to {file_name}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
