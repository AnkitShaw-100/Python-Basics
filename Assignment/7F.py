# Initialize an empty dictionary to store student data
student_data = {}

# Get the number of students from the user
num_students = int(input("Enter the number of students: "))

# Loop to collect data for each student
for i in range(num_students):
    print(f"Enter details for student {i + 1}:")
    student_name = input("Name: ")
    student_age = int(input("Age: "))
    student_grade = (input("Grade: "))
    
    # Create a dictionary for the student's data
    student_info = {
        "Name": student_name,
        "Age": student_age,
        "Grade": student_grade
    }
    
    # Add the student's data to the main dictionary with a unique key (e.g., student ID)
    student_data[f"Student {i + 1}"] = student_info

# Display the student data
print("\nStudent Data:")
for student_id, data in student_data.items():
    print(student_id)
    for key, value in data.items():
        print(f"{key}: {value}")
    print()
