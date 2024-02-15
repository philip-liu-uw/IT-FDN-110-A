import json # Imports built-in json module into Python session
# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: Philip Liu. 2/14.2024. Created Script. 
# ------------------------------------------------------------------------------------------ #

# Constant to show menu options to the user
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''

# Definition of Data Variables
FILE_NAME: str = "Enrollments.json" # File name
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
json_data: str = [] # Holds entry of student information that was manually entered by user.
file_obj = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
student_data: dict = [] # Data in Dictionary format.
students: list = [] # List of student data

# (1)Wrapped error handling if json file is not present. (2)Create file if not present
try:
    with open(FILE_NAME, "r") as file:
        pass  # If json file exists, program will continue
except FileNotFoundError as e:
    file = open(FILE_NAME, 'w')
    print(e,e.__doc__)
    print("Enrollments.json file not found. Created file for you")
finally:
    file.close()

# Start point of While Loop and present & process data
while True:
    # Presentation of menu choices and intro message for action from the user.
    print(MENU)
    menu_choice = input("What would you like to do?: ")

    # Menu option 1. User inputs data, a row is created reflecting user input
    if menu_choice == "1":
        try: # Error handlings wrapped to only accept alphabetic characters Ra
            student_first_name = input("Enter the student's first name: ").strip()
            if not student_first_name.isalpha():
                raise ValueError("Please enter alphabetic characters only for the first name.")

            student_last_name = input("Enter the student's last name: ").strip()
            if not student_last_name.isalpha():
                raise ValueError("Please enter alphabetic characters only for the last name.")

            course_name = input("Please enter the name of the course: ")
            registered_students_row = [student_first_name, student_last_name, course_name]
            student_data.append(registered_students_row)
        except ValueError as e:
            print("Invalid information:", e)

    # Menu option 2. Present current data to the user
    elif menu_choice == "2":
        print("\nThe current data is: ")
        for student in student_data:
            print(student)

    # Menu option 3. Save current data to JSON file
    elif menu_choice == "3":
        with open(FILE_NAME, "w") as file:
            json.dump(student_data, file)
        print("Data saved to file")

    # Menu option 4. Exit program. While Loop stop point.
    elif menu_choice == "4":
        break

    else:
        print("Please only choose options 1, 2, 3, or 4")  # Message to the user if user input is out of bounds.

# Menu option 4 with outro message.
print("Exiting Program...")
