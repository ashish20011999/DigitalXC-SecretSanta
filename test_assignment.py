import csv
import unittest
from unittest.mock import patch
from io import StringIO
from assignment import Assignment, main


class AssignmentTestCase(unittest.TestCase):

    def test_same_employee_has_same_child(self):
        employee_file = 'Employee-List.csv'
        previous_assignments_file = 'Secret-Santa-Game-Result-2023.csv'
        output_file = 'secret_santa_assignments.csv'

        # Load previous year's assignments
        previous_assignments = []
        try:
            with open(previous_assignments_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    previous_assignments.append(row)
        except FileNotFoundError:
            self.fail("Previous assignments file not found")

        # Load current employee information
        employee_info = []
        try:
            with open(employee_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    employee_info.append(row)
        except FileNotFoundError:
            self.fail("Employee information file not found")

        # Generate current assignments
        current_assignments = Assignment(employee_file, previous_assignments_file, output_file).assign_secret_children(employee_info, previous_assignments)

        # Check if any employee has the same secret child as the previous year's assignment
        for assignment in current_assignments:
            employee_email = assignment['Employee_EmailID']
            secret_child_email = assignment['Secret_Child_EmailID']
            for prev_assignment in previous_assignments:
                if (prev_assignment['Employee_EmailID'] == employee_email and
                        prev_assignment['Secret_Child_EmailID'] == secret_child_email):
                    self.fail("Same employee has the same secret child as previous year's assignment")
                    

    def test_file_not_found_error(self):
        employee_file = 'Employee-List.csv'
        previous_assignments_file = 'Secret-Santa-Game-Result-2023.csv'
        output_file = 'secret_santa_assignments.csv'

        game = Assignment(employee_file, previous_assignments_file, output_file)

        try:
            game.load_previous_assignments()
            game.load_previous_assignments()
        except FileNotFoundError:
            self.fail("File not found containing the employee details/ previous secret children assignment")

    def test_permission_denied_error(self):
        employee_file = 'Employee-List.csv'
        previous_assignments_file = 'Secret-Santa-Game-Result-2023.csv'
        output_file = 'secret_santa_assignments.csv'

        game = Assignment(employee_file, previous_assignments_file, output_file)

        try:
            game.load_previous_assignments()
            game.load_previous_assignments()
        except PermissionError:
            self.fail("Access denied to file containing the employee details/ previous secret children assignment")

    def test_insufficient_employee_details(self):
        employee_file = 'Employee-List.csv'
        previous_assignments_file = 'Secret-Santa-Game-Result-2023.csv'
        output_file = 'secret_santa_assignments.csv'

        game = Assignment(employee_file, previous_assignments_file, output_file)

        try:
            game.play_game()
        except IndexError:
            self.fail("List length is insufficient to generate a different index.")

    def test_no_available_indices(self):
        employee_file = 'Employee-List.csv'
        previous_assignments_file = 'Secret-Santa-Game-Result-2023.csv'
        output_file = 'secret_santa_assignments.csv'

        game = Assignment(employee_file, previous_assignments_file, output_file)

        try:
            game.play_game()
        except IndexError:
            self.fail("List length is insufficient to generate a different index.")


    
# driver code
if __name__ == '__main__':

    unittest.main()
