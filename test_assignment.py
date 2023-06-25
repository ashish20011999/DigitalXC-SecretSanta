import csv
import unittest
from unittest.mock import patch
from io import StringIO
from assignment import Assignment, main

class AssignmentTestCase(unittest.TestCase):
 

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
