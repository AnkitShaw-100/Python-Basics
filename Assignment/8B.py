class Car:
    # Constructor to initialize the car's acceleration
    def __init__(self):
        self.acceleration = 10.0  # Constant acceleration of 10 m/s^2
    
    # Function to calculate the final velocity
    def calculate_velocity(self, initial_velocity, time):
        final_velocity = initial_velocity + (self.acceleration * time)
        return final_velocity

# Get input from the user for initial velocity
initial_velocity = float(input("Enter the initial velocity (m/s): "))

# Create an instance of the Car class
car = Car()

# Get input from the user for the time of acceleration
time = float(input("Enter the time of acceleration (seconds): "))

# Calculate and display the final velocity of the car
final_velocity = car.calculate_velocity(initial_velocity, time)
print(f"The final velocity of the car is: {final_velocity} m/s")
