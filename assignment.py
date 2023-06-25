import csv
import random

class Assignment:
    def __init__(self, employee_file, previous_assignments_file, output_file):
        self.employee_file = employee_file
        self.previous_assignments_file = previous_assignments_file
        self.output_file = output_file

    def custom_shuffle(self,lst):
        n = len(lst)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            lst[i], lst[j] = lst[j], lst[i]
        return lst

    def get_random_index(self,length, current_index):
        if length <= 1:
            raise IndexError("List length is insufficient to generate a different index.")
        
        index_list = list(range(length))
        index_list.remove(current_index)
        
        if len(index_list) == 0:
            raise IndexError("No available indices to select from.")
        
        random_index = random.sample(index_list, 1)[0]
        return random_index
    
    def load_employee_info(self):
        employee_info = []
        try:
            with open(self.employee_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    employee_info.append(row)
            return employee_info
        except FileNotFoundError:
            self.fail("File not found containing the employee details/ previous secret children assignment")
        except PermissionError:
            self.fail("Access denied to file containing the employee details/ previous secret children assignment")
        

    def load_previous_assignments(self):
        try:
            previous_assignments = []
            with open(self.previous_assignments_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    previous_assignments.append(row)
            return previous_assignments
        except FileNotFoundError:
            self.fail("File not found containing the employee details/ previous secret children assignment")
        except PermissionError:
            self.fail("Access denied to file containing the employee details/ previous secret children assignment")
        

    def assign_secret_children(self, employee_info, previous_assignments):
        employees = employee_info.copy()
        self.custom_shuffle(employees)  # Shuffle the list of employees

        assignments = []
        for i in range(len(employees)):
            employee = employees[i]
            secret_child = employees[self.get_random_index(len(employees),i)]  # Assign next employee as secret child

            # Check if employee and secret child are the same or were paired in previous year
            while (employee['Employee_EmailID'] == secret_child['Employee_EmailID'] or
                   any((pa['Employee_EmailID'] == employee['Employee_EmailID'] and
                        pa['Secret_Child_EmailID'] == secret_child['Employee_EmailID']) or
                       (pa['Employee_EmailID'] == secret_child['Employee_EmailID'] and
                        pa['Secret_Child_EmailID'] == employee['Employee_EmailID'])
                       for pa in previous_assignments)):
                self.custom_shuffle(employees)  # Reshuffle the list of employees
                secret_child = employees[self.get_random_index(len(employees),i)]  # Assign next employee as secret child

            assignment = {
                'Employee_Name': employee['Employee_Name'],
                'Employee_EmailID': employee['Employee_EmailID'],
                'Secret_Child_Name': secret_child['Employee_Name'],
                'Secret_Child_EmailID': secret_child['Employee_EmailID']
            }
            assignments.append(assignment)

        return assignments

    def save_assignments(self, assignments):
        fieldnames = ['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID']
        with open(self.output_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(assignments)

    def play_game(self):
        employee_info = self.load_employee_info()
        previous_assignments = self.load_previous_assignments()
        assignments = self.assign_secret_children(employee_info, previous_assignments)
        self.save_assignments(assignments)
        print("Secret Santa assignments have been generated successfully.")

# Usage example
def main():
    employee_file = 'Employee-List.csv'
    previous_assignments_file = 'Secret-Santa-Game-Result-2023.csv'
    output_file = 'secret_santa_assignments.csv'

    game = Assignment(employee_file, previous_assignments_file, output_file)
    game.play_game()

if __name__ == '__main__':
    main()
