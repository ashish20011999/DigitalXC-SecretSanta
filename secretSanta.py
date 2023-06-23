import csv
import random

# Function to load employee information from CSV file
def load_employee_info(file_name):
    employee_info = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employee_info.append(row)
    return employee_info

# Function to load previous year's Secret Santa assignments from CSV file
def load_previous_assignments(file_name):
    previous_assignments = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            previous_assignments.append(row)
    return previous_assignments

# Function to assign secret children to employees
def assign_secret_children(employee_info, previous_assignments):
    employees = employee_info.copy()
    random.shuffle(employees)  # Shuffle the list of employees

    assignments = []
    for i in range(len(employees)):
        employee = employees[i]
        secret_child = employees[(i+1) % len(employees)]  # Assign next employee as secret child

        # Check if employee and secret child are the same or were paired in previous year
        while (employee['Employee_EmailID'] == secret_child['Employee_EmailID'] or
               any((pa['Employee_EmailID'] == employee['Employee_EmailID'] and
                    pa['Secret_Child_EmailID'] == secret_child['Employee_EmailID']) or
                   (pa['Employee_EmailID'] == secret_child['Employee_EmailID'] and
                    pa['Secret_Child_EmailID'] == employee['Employee_EmailID'])
                   for pa in previous_assignments)):
            random.shuffle(employees)  # Reshuffle the list of employees
            secret_child = employees[(i+1) % len(employees)]  # Assign next employee as secret child

        assignment = {
            'Employee_Name': employee['Employee_Name'],
            'Employee_EmailID': employee['Employee_EmailID'],
            'Secret_Child_Name': secret_child['Employee_Name'],
            'Secret_Child_EmailID': secret_child['Employee_EmailID']
        }
        assignments.append(assignment)

    return assignments

# Function to save assignments to CSV file
def save_assignments(assignments, file_name):
    fieldnames = ['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID']
    with open(file_name, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(assignments)

# Main function
def main():
    # File paths
    employee_file = 'employee_info.csv'
    previous_assignments_file = 'previous_assignments.csv'
    output_file = 'secret_santa_assignments.csv'

    # Load employee information and previous assignments
    employee_info = load_employee_info(employee_file)
    previous_assignments = load_previous_assignments(previous_assignments_file)

    # Assign secret children to employees
    assignments = assign_secret_children(employee_info, previous_assignments)

    # Save assignments to output file
    save_assignments(assignments, output_file)

    print("Secret Santa assignments have been generated successfully.")

# Run the program
if __name__ == '__main__':
    main()
