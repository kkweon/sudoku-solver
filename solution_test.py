import solution
import unittest

from utils import *


class TestCreatePuzzle(unittest.TestCase):
    def test_values_to_grid(self):
        values = {"A1": "1234", "A2":"1"}
        self.assertEqual(values_to_grid(values), ".1" + "."*(72+7))

        values = {"A1": "4", "A2":"1"}
        self.assertEqual(values_to_grid(values), "41" + "."*(72+7))

    def test_can_create_puzzle_return_string(self):
        self.assertEqual(type(create_puzzle(12)), str)

    def test_can_create_puzzle_create_81_units(self):
        self.assertEqual(len(create_puzzle(12)), 81)

    def test_can_create_puzzle(self):
        puzzle = create_puzzle(12)
        values = solution.solve(puzzle)
        self.assertTrue(all([len(values[box]) == 1 for box in values]))
        for unit in solution.square_units:
            value_list = set([values[box] for box in unit])
            self.assertEqual(value_list, set("123456789"))


class TestNakedTwins(unittest.TestCase):
    before_naked_twins_1 = {'I6': '4', 'H9': '3', 'I2': '6', 'E8': '1', 'H3': '5', 'H7': '8', 'I7': '1', 'I4': '8',
                            'H5': '6', 'F9': '7', 'G7': '6', 'G6': '3', 'G5': '2', 'E1': '8', 'G3': '1', 'G2': '8',
                            'G1': '7', 'I1': '23', 'C8': '5', 'I3': '23', 'E5': '347', 'I5': '5', 'C9': '1', 'G9': '5',
                            'G8': '4', 'A1': '1', 'A3': '4', 'A2': '237', 'A5': '9', 'A4': '2357', 'A7': '27',
                            'A6': '257', 'C3': '8', 'C2': '237', 'C1': '23', 'E6': '579', 'C7': '9', 'C6': '6',
                            'C5': '37', 'C4': '4', 'I9': '9', 'D8': '8', 'I8': '7', 'E4': '6', 'D9': '6', 'H8': '2',
                            'F6': '125', 'A9': '8', 'G4': '9', 'A8': '6', 'E7': '345', 'E3': '379', 'F1': '6',
                            'F2': '4', 'F3': '23', 'F4': '1235', 'F5': '8', 'E2': '37', 'F7': '35', 'F8': '9',
                            'D2': '1', 'H1': '4', 'H6': '17', 'H2': '9', 'H4': '17', 'D3': '2379', 'B4': '27',
                            'B5': '1', 'B6': '8', 'B7': '27', 'E9': '2', 'B1': '9', 'B2': '5', 'B3': '6', 'D6': '279',
                            'D7': '34', 'D4': '237', 'D5': '347', 'B8': '3', 'B9': '4', 'D1': '5'}
    possible_solutions_1 = [
        {'G7': '6', 'G6': '3', 'G5': '2', 'G4': '9', 'G3': '1', 'G2': '8', 'G1': '7', 'G9': '5', 'G8': '4', 'C9': '1',
         'C8': '5', 'C3': '8', 'C2': '237', 'C1': '23', 'C7': '9', 'C6': '6', 'C5': '37', 'A4': '2357', 'A9': '8',
         'A8': '6', 'F1': '6', 'F2': '4', 'F3': '23', 'F4': '1235', 'F5': '8', 'F6': '125', 'F7': '35', 'F8': '9',
         'F9': '7', 'B4': '27', 'B5': '1', 'B6': '8', 'B7': '27', 'E9': '2', 'B1': '9', 'B2': '5', 'B3': '6', 'C4': '4',
         'B8': '3', 'B9': '4', 'I9': '9', 'I8': '7', 'I1': '23', 'I3': '23', 'I2': '6', 'I5': '5', 'I4': '8', 'I7': '1',
         'I6': '4', 'A1': '1', 'A3': '4', 'A2': '237', 'A5': '9', 'E8': '1', 'A7': '27', 'A6': '257', 'E5': '347',
         'E4': '6', 'E7': '345', 'E6': '579', 'E1': '8', 'E3': '79', 'E2': '37', 'H8': '2', 'H9': '3', 'H2': '9',
         'H3': '5', 'H1': '4', 'H6': '17', 'H7': '8', 'H4': '17', 'H5': '6', 'D8': '8', 'D9': '6', 'D6': '279',
         'D7': '34', 'D4': '237', 'D5': '347', 'D2': '1', 'D3': '79', 'D1': '5'},
        {'I6': '4', 'H9': '3', 'I2': '6', 'E8': '1', 'H3': '5', 'H7': '8', 'I7': '1', 'I4': '8', 'H5': '6', 'F9': '7',
         'G7': '6', 'G6': '3', 'G5': '2', 'E1': '8', 'G3': '1', 'G2': '8', 'G1': '7', 'I1': '23', 'C8': '5', 'I3': '23',
         'E5': '347', 'I5': '5', 'C9': '1', 'G9': '5', 'G8': '4', 'A1': '1', 'A3': '4', 'A2': '237', 'A5': '9',
         'A4': '2357', 'A7': '27', 'A6': '257', 'C3': '8', 'C2': '237', 'C1': '23', 'E6': '579', 'C7': '9', 'C6': '6',
         'C5': '37', 'C4': '4', 'I9': '9', 'D8': '8', 'I8': '7', 'E4': '6', 'D9': '6', 'H8': '2', 'F6': '125',
         'A9': '8', 'G4': '9', 'A8': '6', 'E7': '345', 'E3': '79', 'F1': '6', 'F2': '4', 'F3': '23', 'F4': '1235',
         'F5': '8', 'E2': '3', 'F7': '35', 'F8': '9', 'D2': '1', 'H1': '4', 'H6': '17', 'H2': '9', 'H4': '17',
         'D3': '79', 'B4': '27', 'B5': '1', 'B6': '8', 'B7': '27', 'E9': '2', 'B1': '9', 'B2': '5', 'B3': '6',
         'D6': '279', 'D7': '34', 'D4': '237', 'D5': '347', 'B8': '3', 'B9': '4', 'D1': '5'}
        ]

    before_naked_twins_2 = {'A1': '23', 'A2': '4', 'A3': '7', 'A4': '6', 'A5': '8', 'A6': '5', 'A7': '23', 'A8': '9',
                            'A9': '1', 'B1': '6', 'B2': '9', 'B3': '8', 'B4': '4', 'B5': '37', 'B6': '1', 'B7': '237',
                            'B8': '5', 'B9': '237', 'C1': '23', 'C2': '5', 'C3': '1', 'C4': '23', 'C5': '379',
                            'C6': '2379', 'C7': '8', 'C8': '6', 'C9': '4', 'D1': '8', 'D2': '17', 'D3': '9',
                            'D4': '1235', 'D5': '6', 'D6': '237', 'D7': '4', 'D8': '27', 'D9': '2357', 'E1': '5',
                            'E2': '6', 'E3': '2', 'E4': '8', 'E5': '347', 'E6': '347', 'E7': '37', 'E8': '1', 'E9': '9',
                            'F1': '4', 'F2': '17', 'F3': '3', 'F4': '125', 'F5': '579', 'F6': '279', 'F7': '6',
                            'F8': '8', 'F9': '257', 'G1': '1', 'G2': '8', 'G3': '6', 'G4': '35', 'G5': '345',
                            'G6': '34', 'G7': '9', 'G8': '27', 'G9': '27', 'H1': '7', 'H2': '2', 'H3': '4', 'H4': '9',
                            'H5': '1', 'H6': '8', 'H7': '5', 'H8': '3', 'H9': '6', 'I1': '9', 'I2': '3', 'I3': '5',
                            'I4': '7', 'I5': '2', 'I6': '6', 'I7': '1', 'I8': '4', 'I9': '8'}
    possible_solutions_2 = [
        {'A1': '23', 'A2': '4', 'A3': '7', 'A4': '6', 'A5': '8', 'A6': '5', 'A7': '23', 'A8': '9', 'A9': '1', 'B1': '6',
         'B2': '9', 'B3': '8', 'B4': '4', 'B5': '37', 'B6': '1', 'B7': '237', 'B8': '5', 'B9': '237', 'C1': '23',
         'C2': '5', 'C3': '1', 'C4': '23', 'C5': '79', 'C6': '79', 'C7': '8', 'C8': '6', 'C9': '4', 'D1': '8',
         'D2': '17', 'D3': '9', 'D4': '1235', 'D5': '6', 'D6': '237', 'D7': '4', 'D8': '27', 'D9': '2357', 'E1': '5',
         'E2': '6', 'E3': '2', 'E4': '8', 'E5': '347', 'E6': '347', 'E7': '37', 'E8': '1', 'E9': '9', 'F1': '4',
         'F2': '17', 'F3': '3', 'F4': '125', 'F5': '579', 'F6': '279', 'F7': '6', 'F8': '8', 'F9': '257', 'G1': '1',
         'G2': '8', 'G3': '6', 'G4': '35', 'G5': '345', 'G6': '34', 'G7': '9', 'G8': '27', 'G9': '27', 'H1': '7',
         'H2': '2', 'H3': '4', 'H4': '9', 'H5': '1', 'H6': '8', 'H7': '5', 'H8': '3', 'H9': '6', 'I1': '9', 'I2': '3',
         'I3': '5', 'I4': '7', 'I5': '2', 'I6': '6', 'I7': '1', 'I8': '4', 'I9': '8'},
        {'A1': '23', 'A2': '4', 'A3': '7', 'A4': '6', 'A5': '8', 'A6': '5', 'A7': '23', 'A8': '9', 'A9': '1', 'B1': '6',
         'B2': '9', 'B3': '8', 'B4': '4', 'B5': '3', 'B6': '1', 'B7': '237', 'B8': '5', 'B9': '237', 'C1': '23',
         'C2': '5', 'C3': '1', 'C4': '23', 'C5': '79', 'C6': '79', 'C7': '8', 'C8': '6', 'C9': '4', 'D1': '8',
         'D2': '17', 'D3': '9', 'D4': '1235', 'D5': '6', 'D6': '237', 'D7': '4', 'D8': '27', 'D9': '2357', 'E1': '5',
         'E2': '6', 'E3': '2', 'E4': '8', 'E5': '347', 'E6': '347', 'E7': '37', 'E8': '1', 'E9': '9', 'F1': '4',
         'F2': '17', 'F3': '3', 'F4': '125', 'F5': '579', 'F6': '279', 'F7': '6', 'F8': '8', 'F9': '257', 'G1': '1',
         'G2': '8', 'G3': '6', 'G4': '35', 'G5': '345', 'G6': '34', 'G7': '9', 'G8': '27', 'G9': '27', 'H1': '7',
         'H2': '2', 'H3': '4', 'H4': '9', 'H5': '1', 'H6': '8', 'H7': '5', 'H8': '3', 'H9': '6', 'I1': '9', 'I2': '3',
         'I3': '5', 'I4': '7', 'I5': '2', 'I6': '6', 'I7': '1', 'I8': '4', 'I9': '8'}
    ]

    def test_naked_twins(self):
        self.assertTrue(solution.naked_twins(self.before_naked_twins_1) in self.possible_solutions_1,
                        "Your naked_twins function produced an unexpected board.")

    def test_naked_twins2(self):
        self.assertTrue(solution.naked_twins(self.before_naked_twins_2) in self.possible_solutions_2,
                        "Your naked_twins function produced an unexpected board.")



class TestDiagonalSudoku(unittest.TestCase):
    diagonal_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    solved_diag_sudoku = {'G7': '8', 'G6': '9', 'G5': '7', 'G4': '3', 'G3': '2', 'G2': '4', 'G1': '6', 'G9': '5',
                          'G8': '1', 'C9': '6', 'C8': '7', 'C3': '1', 'C2': '9', 'C1': '4', 'C7': '5', 'C6': '3',
                          'C5': '2', 'C4': '8', 'E5': '9', 'E4': '1', 'F1': '1', 'F2': '2', 'F3': '9', 'F4': '6',
                          'F5': '5', 'F6': '7', 'F7': '4', 'F8': '3', 'F9': '8', 'B4': '7', 'B5': '1', 'B6': '6',
                          'B7': '2', 'B1': '8', 'B2': '5', 'B3': '3', 'B8': '4', 'B9': '9', 'I9': '3', 'I8': '2',
                          'I1': '7', 'I3': '8', 'I2': '1', 'I5': '6', 'I4': '5', 'I7': '9', 'I6': '4', 'A1': '2',
                          'A3': '7', 'A2': '6', 'E9': '7', 'A4': '9', 'A7': '3', 'A6': '5', 'A9': '1', 'A8': '8',
                          'E7': '6', 'E6': '2', 'E1': '3', 'E3': '4', 'E2': '8', 'E8': '5', 'A5': '4', 'H8': '6',
                          'H9': '4', 'H2': '3', 'H3': '5', 'H1': '9', 'H6': '1', 'H7': '7', 'H4': '2', 'H5': '8',
                          'D8': '9', 'D9': '2', 'D6': '8', 'D7': '1', 'D4': '4', 'D5': '3', 'D2': '7', 'D3': '6',
                          'D1': '5'}

    def test_solve(self):
        self.assertEqual(solution.solve(self.diagonal_grid), self.solved_diag_sudoku)


    def test_can_solve_diagonal_sudoku(self):
        test_grid = '.89.54...........9.....7.....6..2..41...4...33..7..6.....6.....5...........41.59.'
        answer_grid = "289354176437861259615927348956132784178546923324789615741695832593278461862413597"

        self.assertEqual(solution.solve(test_grid), solution.grid_values(answer_grid))

        test_grid = "..75..84.652148.9.4.8732.158.6491.5392.....6114.3269.823.9571.6.8.613524.61..47.."
        answer_grid = "317569842652148397498732615876491253923875461145326978234957186789613524561284739"
        
        self.assertEqual(solution.solve(test_grid), solution.grid_values(answer_grid))

    def test_can_solve_traditional_sudoku(self):
        test_grid = "276314958854962713913875264468127395597438621132596487325789146641253879789641532"
        answer_grid = "276314958854962713913875264468127395597438621132596487325789146641253879789641532"

        self.assertEqual(solution.solve(test_grid), solution.grid_values(answer_grid))


        



class TestEnvironment(unittest.TestCase):
    """Test initial variables such as boxes, unitlist, unittest
    """
    def test_eliminate_can_solve_undiagonal(self):
        test_grid = ".763149588549627.39138752644681.73955974386211325.648732.789146641253879789641532"
        answer_grid = "276314958854962713913875264468127395597438621132596487325789146641253879789641532"
        self.assertEqual(solution.eliminate(solution.grid_values(test_grid), False), solution.grid_values(answer_grid))

        test_grid = "..6314958854962713913875264.681273.559743862.132596487325789146641253879789641532"
        answer_grid = "276314958854962713913875264468127395597438621132596487325789146641253879789641532"
        self.assertEqual(solution.eliminate(solution.grid_values(test_grid), False), solution.grid_values(answer_grid))

    def test_only_choice_can_solve_undiagonal(self):
        test_grid = ".763149588549627139138752644.812739559.438621.32596487325789146641253879789641532"
        answer_grid = "276314958854962713913875264468127395597438621132596487325789146641253879789641532"

        self.assertEqual(solution.only_choice(solution.grid_values(test_grid), False), solution.grid_values(answer_grid))

    def test_can_solve_method_take_str_input(self):
        diagonal_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
        solved_diag_sudoku = {'G7': '8', 'G6': '9', 'G5': '7', 'G4': '3', 'G3': '2', 'G2': '4', 'G1': '6', 'G9': '5',
                              'G8': '1', 'C9': '6', 'C8': '7', 'C3': '1', 'C2': '9', 'C1': '4', 'C7': '5', 'C6': '3',
                              'C5': '2', 'C4': '8', 'E5': '9', 'E4': '1', 'F1': '1', 'F2': '2', 'F3': '9', 'F4': '6',
                              'F5': '5', 'F6': '7', 'F7': '4', 'F8': '3', 'F9': '8', 'B4': '7', 'B5': '1', 'B6': '6',
                              'B7': '2', 'B1': '8', 'B2': '5', 'B3': '3', 'B8': '4', 'B9': '9', 'I9': '3', 'I8': '2',
                              'I1': '7', 'I3': '8', 'I2': '1', 'I5': '6', 'I4': '5', 'I7': '9', 'I6': '4', 'A1': '2',
                              'A3': '7', 'A2': '6', 'E9': '7', 'A4': '9', 'A7': '3', 'A6': '5', 'A9': '1', 'A8': '8',
                              'E7': '6', 'E6': '2', 'E1': '3', 'E3': '4', 'E2': '8', 'E8': '5', 'A5': '4', 'H8': '6',
                              'H9': '4', 'H2': '3', 'H3': '5', 'H1': '9', 'H6': '1', 'H7': '7', 'H4': '2', 'H5': '8',
                              'D8': '9', 'D9': '2', 'D6': '8', 'D7': '1', 'D4': '4', 'D5': '3', 'D2': '7', 'D3': '6',
                              'D1': '5'}

        self.assertEqual(solution.solve(diagonal_grid), solved_diag_sudoku)

    def test_can_solve_method_take_dict_input(self):
        diagonal_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
        solved_diag_sudoku = {'G7': '8', 'G6': '9', 'G5': '7', 'G4': '3', 'G3': '2', 'G2': '4', 'G1': '6', 'G9': '5',
                              'G8': '1', 'C9': '6', 'C8': '7', 'C3': '1', 'C2': '9', 'C1': '4', 'C7': '5', 'C6': '3',
                              'C5': '2', 'C4': '8', 'E5': '9', 'E4': '1', 'F1': '1', 'F2': '2', 'F3': '9', 'F4': '6',
                              'F5': '5', 'F6': '7', 'F7': '4', 'F8': '3', 'F9': '8', 'B4': '7', 'B5': '1', 'B6': '6',
                              'B7': '2', 'B1': '8', 'B2': '5', 'B3': '3', 'B8': '4', 'B9': '9', 'I9': '3', 'I8': '2',
                              'I1': '7', 'I3': '8', 'I2': '1', 'I5': '6', 'I4': '5', 'I7': '9', 'I6': '4', 'A1': '2',
                              'A3': '7', 'A2': '6', 'E9': '7', 'A4': '9', 'A7': '3', 'A6': '5', 'A9': '1', 'A8': '8',
                              'E7': '6', 'E6': '2', 'E1': '3', 'E3': '4', 'E2': '8', 'E8': '5', 'A5': '4', 'H8': '6',
                              'H9': '4', 'H2': '3', 'H3': '5', 'H1': '9', 'H6': '1', 'H7': '7', 'H4': '2', 'H5': '8',
                              'D8': '9', 'D9': '2', 'D6': '8', 'D7': '1', 'D4': '4', 'D5': '3', 'D2': '7', 'D3': '6',
                              'D1': '5'}
        diagonal_grid = solution.grid_values(diagonal_grid)
        self.assertEqual(solution.solve(diagonal_grid), solved_diag_sudoku)

    def test_can_solve_method_return_error_when_wrong_input_type(self):
        grid = list()
        self.assertRaises(solution.WrongInputType, solve, grid)

    def test_rows_is_implemented(self):
        self.assertEqual(solution.rows, "ABCDEFGHI", msg="Define rows='ABCDEFGHI'")

    def test_cols_is_implemented(self):
        self.assertEqual(solution.cols, "123456789", msg='Define cols="123456789"')

    def test_row_units_is_implement(self):
        self.assertEqual(len(solution.row_units), 9, msg="Define row_units = ")

    def test_col_units_is_implement(self):
        self.assertEqual(len(solution.col_units), 9, msg="Define col_units = ")

    def test_square_units_is_implement(self):
        self.assertEqual(len(solution.square_units), 9, msg="Define square_units = ")

    def test_diagonal_units_is_implement(self):
        self.assertEqual(len(solution.diagonal_units), 2, msg="Define diagonal_units = ")
        self.assertEqual(len(solution.diagonal_units[0]), 9)
        self.assertEqual(len(solution.diagonal_units[1]), 9)
        self.assertEqual(solution.diagonal_units[0][0], "A1")
        self.assertEqual(solution.diagonal_units[0][-1], "I9")
        self.assertEqual(solution.diagonal_units[1][0], "A9")
        self.assertEqual(solution.diagonal_units[1][-1], "I1")

    def test_number_of_boxes_is_81(self):
        # There are 9 * 9 = 81 boxes
        self.assertEqual(len(solution.boxes), 81, msg="Define boxes = ")

    def test_number_of_unitlist_is_29(self):
        # Because there 9 rows + 9 cols + 9 squares + 2 diagonal => 29 units
        self.assertEqual(len(solution.unitlist), 29, msg="Define unitlist = ")

    def test_number_of_units_in_unitlist_undiagonal_is_27(self):
        # Because there 9 rows + 9 cols + 9 squares  => 27 units
        self.assertEqual(len(solution.unitlist_undiagonal), 27, msg="Define unitlist_undiagonal = ")

    def test_each_box_has_3_units_when_undiagonal(self):
        # Row (1) + ColumN(1) + Square(1)
        self.assertTrue(all([len(solution.units_undiagonal[box]) == 3 for box in solution.boxes]))

    def test_each_box_has_4_units(self):
        # Diagonal Non Center Box: There are 4 constraints: row unit, column unit, square units, diagonal units
        diagonal_except_center_box_list = [box for box in sum(solution.diagonal_units, []) if box != "E5"]
        self.assertTrue(all([len(solution.units[box]) == 4 for box in diagonal_except_center_box_list]))
        # Non Diagonal box: there are 3 constrains
        non_diagonal_box_list = [box for box in solution.boxes if box not in sum(solution.diagonal_units, [])]
        self.assertTrue(all([len(solution.units[box]) == 3 for box in non_diagonal_box_list]))
        # Center Box: There are 5 constrains (2 for diagonal unis)
        self.assertTrue(len(solution.units['E5']) == 5)

    def test_each_box_has_correct_peers(self):
        # Each box has 20 peers 8 peers in rows + 8 peers in columns + 8 peers in its square - 4 (duplicate)
        # If a box is in diagonal not center, 8 peers in row, 8 peers in column, 8 peers in square, 8 peers in diagonal  - 6 duplciate
        # -> 32 - 6 = 26
        diagonal_except_center_box_list = [box for box in sum(solution.diagonal_units, []) if box != "E5"]
        self.assertTrue(all([len(solution.peers[box]) == 26 for box in diagonal_except_center_box_list]))
        # If a box is not in diagonal, 20 peers
        non_diagonal_box_list = [box for box in solution.boxes if box not in sum(solution.diagonal_units, [])]
        self.assertTrue(all([len(solution.peers[box]) == 20 for box in non_diagonal_box_list]))
        # If a box is not in diagonal, 20 peers
        # If a box is at center (E5), it has 20 + 16 - 4 = 32
        self.assertEqual(len(solution.peers['E5']), 32)

    def test_unit_implementation(self):
        self.assertEqual(solution.units['C2'], [['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
                                                     ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
                                                     ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']])

    def test_peer_implementation(self):
        self.assertEqual(solution.peers['C2'], set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                                                         'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                                                         'A1', 'A3', 'B1', 'B3']))

    def test_grid_values(self):
        values = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
        grid_values = solution.grid_values
        self.assertEqual(type(grid_values(values)), dict)
        self.assertEqual(grid_values(values), {'A1': '123456789', 'A2': '123456789', 'A3': '3', 'A4': '123456789', 'A5': '2', 'A6': '123456789', 'A7': '6', 'A8': '123456789', 'A9': '123456789', 'B1': '9', 'B2': '123456789', 'B3': '123456789', 'B4': '3', 'B5': '123456789', 'B6': '5', 'B7': '123456789', 'B8': '123456789', 'B9': '1', 'C1': '123456789', 'C2': '123456789', 'C3': '1', 'C4': '8', 'C5': '123456789', 'C6': '6', 'C7': '4', 'C8': '123456789', 'C9': '123456789', 'D1': '123456789', 'D2': '123456789', 'D3': '8', 'D4': '1', 'D5': '123456789', 'D6': '2', 'D7': '9', 'D8': '123456789', 'D9': '123456789', 'E1': '7', 'E2': '123456789', 'E3': '123456789', 'E4': '123456789', 'E5': '123456789', 'E6': '123456789', 'E7': '123456789', 'E8': '123456789', 'E9': '8', 'F1': '123456789', 'F2': '123456789', 'F3': '6', 'F4': '7', 'F5': '123456789', 'F6': '8', 'F7': '2', 'F8': '123456789', 'F9': '123456789', 'G1': '123456789', 'G2': '123456789', 'G3': '2', 'G4': '6', 'G5': '123456789', 'G6': '9', 'G7': '5', 'G8': '123456789', 'G9': '123456789', 'H1': '8', 'H2': '123456789', 'H3': '123456789', 'H4': '2', 'H5': '123456789', 'H6': '3', 'H7': '123456789', 'H8': '123456789', 'H9': '9', 'I1': '123456789', 'I2': '123456789', 'I3': '5', 'I4': '123456789', 'I5': '1', 'I6': '123456789', 'I7': '3', 'I8': '123456789', 'I9': '123456789'})

    def test_only_choice(self):
        grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
        values = solution.grid_values(grid)
        result = solution.eliminate(values)
        only_choice_result = solution.only_choice(result)
        self.assertEqual(type(only_choice_result), dict)

        test_grid = dict([(box, "23456789") for box in solution.boxes])
        test_grid["A1"] = "123456789"

        expected_grid = dict([(box, "23456789") for box in solution.boxes])
        expected_grid["A1"] = "1"
        self.assertEqual(solution.only_choice(test_grid), expected_grid)

    def test_eliminate(self):
        grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
        values = solution.grid_values(grid)
        result = solution.eliminate(values)
        self.assertEqual(type(result), dict)

        answer_grid = "289354176437861259615927348956132784178546923324789615741695832593278461862413597"
        grid = solution.grid_values(answer_grid)
        grid["A1"] = "289"
        self.assertEqual(solution.eliminate(grid), solution.grid_values(answer_grid))

    def test_reduce_puzzle(self):
        grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
        values = solution.grid_values(grid)
        #self.assertEqual(solution.reduce_puzzle(values), {'A1': '4', 'A2': '8', 'A3': '3', 'A4': '9', 'A5': '2', 'A6': '1', 'A7': '6', 'A8': '5', 'A9': '7', 'B1': '9', 'B2': '6', 'B3': '7', 'B4': '3', 'B5': '4', 'B6': '5', 'B7': '8', 'B8': '2', 'B9': '1', 'C1': '2', 'C2': '5', 'C3': '1', 'C4': '8', 'C5': '7', 'C6': '6', 'C7': '4', 'C8': '9', 'C9': '3', 'D1': '5', 'D2': '4', 'D3': '8', 'D4': '1', 'D5': '3', 'D6': '2', 'D7': '9', 'D8': '7', 'D9': '6', 'E1': '7', 'E2': '2', 'E3': '9', 'E4': '5', 'E5': '6', 'E6': '4', 'E7': '1', 'E8': '3', 'E9': '8', 'F1': '1', 'F2': '3', 'F3': '6', 'F4': '7', 'F5': '9', 'F6': '8', 'F7': '2', 'F8': '4', 'F9': '5', 'G1': '3', 'G2': '7', 'G3': '2', 'G4': '6', 'G5': '8', 'G6': '9', 'G7': '5', 'G8': '1', 'G9': '4', 'H1': '8', 'H2': '1', 'H3': '4', 'H4': '2', 'H5': '5', 'H6': '3', 'H7': '7', 'H8': '6', 'H9': '9', 'I1': '6', 'I2': '9', 'I3': '5', 'I4': '4', 'I5': '1', 'I6': '7', 'I7': '3', 'I8': '8', 'I9': '2'})

    def test_print(self):
        values = {'B4': '1', 'B6': '8', 'E6': '6', 'B9': '7', 'G7': '5', 'E1': '7', 'C1': '9', 'C4': '7', 'D3': '5', 'A5': '6', 'D5': '3', 'E3': '1', 'G1': '2', 'I1': '1', 'F2': '4', 'E7': '4', 'C2': '5', 'E2': '9', 'E8': '3', 'H2': '7', 'H9': '4', 'D4': '4', 'A2': '1', 'F3': '6', 'H4': '2', 'F9': '8', 'B2': '3', 'I9': '3', 'D8': '6', 'G8': '7', 'G2': '8', 'H3': '3', 'A6': '9', 'G4': '6', 'F4': '9', 'F6': '2', 'I5': '7', 'I3': '4', 'A1': '4', 'B7': '9', 'I4': '8', 'A9': '5', 'I7': '2', 'C6': '4', 'H6': '1', 'F8': '5', 'C5': '2', 'F5': '1', 'I2': '6', 'I6': '5', 'D9': '9', 'C3': '8', 'A4': '3', 'A3': '7', 'C9': '6', 'G6': '3', 'B3': '2', 'D6': '7', 'C7': '3', 'D1': '8', 'C8': '1', 'D2': '2', 'A8': '2', 'B8': '4', 'I8': '9', 'A7': '8', 'F7': '7', 'H5': '9', 'G3': '9', 'G5': '4', 'H8': '8', 'B1': '6', 'F1': '3', 'E4': '5', 'E5': '8', 'E9': '2', 'G9': '1', 'B5': '5', 'H7': '6', 'D7': '1', 'H1': '5'}
        expected = """4 1 7 |3 6 9 |8 2 5 
6 3 2 |1 5 8 |9 4 7 
9 5 8 |7 2 4 |3 1 6 
------+------+------
8 2 5 |4 3 7 |1 6 9 
7 9 1 |5 8 6 |4 3 2 
3 4 6 |9 1 2 |7 5 8 
------+------+------
2 8 9 |6 4 3 |5 7 1 
5 7 3 |2 9 1 |6 8 4 
1 6 4 |8 7 5 |2 9 3 
"""
        self.assertEqual(solution.display(values), expected)


if __name__ == '__main__':
    unittest.main()

