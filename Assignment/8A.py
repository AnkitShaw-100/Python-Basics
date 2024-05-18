class Box:
    # Constructor to initialize the dimensions of the box
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
    
    # Function to calculate the volume of the box
    def calculate_volume(self):
        volume = self.length * self.width * self.height
        return volume

# Get input from the user for the dimensions of the box
length = float(input("Enter the length of the box: "))
width = float(input("Enter the width of the box: "))
height = float(input("Enter the height of the box: "))

# Create an instance of the Box class with user-provided dimensions
box1 = Box(length, width, height)

# Calculate and display the volume of the box
volume = box1.calculate_volume()
print(f"The volume of the box is: {volume} cubic units")
