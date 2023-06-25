import csv
import unittest
from unittest.mock import patch
from io import StringIO
from assignment import Assignment, main

class AssignmentTestCase(unittest.TestCase):
    # def test_successful_assignment_generation(self):
    #     employee_file = 'Employee-List.csv'
    #     previous_assignments_file = 'Secret-Santa-Game-Result-2023.csv'
    #     output_file = 'secret_santa_assignments.csv'

    #     game = Assignment(employee_file, previous_assignments_file, output_file)

    #     with patch('random.sample', side_effect=[2, 1, 0]):  # Mocking random.sample to control indices
    #         game.play_game()
            
        
    #     # Verify the contents of the output file
    #     with open(output_file, 'r') as file:
    #         reader = csv.DictReader(file)
    #         assignments = list(reader)

    #     # Assert the number of assignments and their uniqueness
    #     self.assertEqual(len(assignments), 3)
    #     self.assertEqual(len(set((assignment['Employee_EmailID'], assignment['Secret_Child_EmailID']) for assignment in assignments)), 3)

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


    # def test_unique_assignments(self):
    #     employee_file = 'Employee-List.csv'
    #     previous_assignments_file = 'Secret-Santa-Game-Result-2023.csv'
    #     output_file = 'secret_santa_assignments.csv'

    #     game = Assignment(employee_file, previous_assignments_file, output_file)

    #     with patch('random.sample', side_effect=[0, 1, 2]):  # Mocking random.sample to control indices
    #         game.play_game()

    #     # Verify the contents of the output file
    #     with open(output_file, 'r') as file:
    #         reader = csv.DictReader(file)
    #         assignments = list(reader)

    
# driver code
if __name__ == '__main__':

    unittest.main()