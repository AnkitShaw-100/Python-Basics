# Function to generate the Fibonacci sequence up to n terms
def generate_fibonacci_sequence(n):
    sequence = [1, 1]  # Initialize the sequence with the first two terms

    # Generate the Fibonacci sequence up to the nth term
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence

# Get the value of N from the user
try:
    N = int(input("Enter the value of N: "))
    if N < 1:
        raise ValueError("N must be a positive integer.")

    # Create or open the text file for writing ('w')
    with open("fibonacci_sequence.txt", 'w') as file:
        # Generate and write the Fibonacci sequences to the file
        for i in range(1, N + 1):
            sequence = generate_fibonacci_sequence(i)
            line = "-".join(map(str, sequence))  # Convert the list to a string with '-' separator
            file.write(line + "\n")  # Write the line to the file

    print(f"Fibonacci sequences up to {N} terms have been written to 'fibonacci_sequence.txt'.")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
