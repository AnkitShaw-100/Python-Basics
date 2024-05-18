# Get the source file name from the user
source_file_name = input("Enter the name of the source text file: ")

# Get the target file name from the user
target_file_name = input("Enter the name of the target text file: ")

try:
    # Open the source file in read mode ('r')
    with open(source_file_name, 'r') as source_file:
        # Read the content of the source file
        source_content = source_file.read()

    # Convert the content to lowercase
    converted_content = source_content.lower()

    # Open the target file in write mode ('w') to create it or overwrite existing content
    with open(target_file_name, 'w') as target_file:
        # Write the converted content to the target file
        target_file.write(converted_content)

    print(f"Content copied and converted to lowercase to {target_file_name}")
except FileNotFoundError:
    print("The specified file(s) do not exist.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
