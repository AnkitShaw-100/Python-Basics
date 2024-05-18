# Get the filename from the user
file_name = input("Enter the name of the text file (include the '.txt' extension): ")

# Get the text input from the user
text_to_write = input("Enter the text you want to add to the file: ")

# Open the file in write mode ('w') to create it or overwrite existing content
try:
    with open(file_name, 'w') as file:
        # Write the user's input to the file
        file.write(text_to_write)
    print(f"Text successfully written to {file_name}")
except FileNotFoundError:
    print("The specified directory does not exist.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
