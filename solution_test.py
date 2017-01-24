import solution
import unittest

before_naked_twins = {'I6': '4', 'H9': '3', 'I2': '6', 'E8': '1', 'H3': '5', 'H7': '8', 'I7': '1', 'I4': '8', 'H5': '6', 'F9': '7', 'G7': '6', 'G6': '3', 'G5': '2', 'E1': '8', 'G3': '1', 'G2': '8', 'G1': '7', 'I1': '23', 'C8': '5', 'I3': '23', 'E5': '347', 'I5': '5', 'C9': '1', 'G9': '5', 'G8': '4', 'A1': '1', 'A3': '4', 'A2': '237', 'A5': '9', 'A4': '2357', 'A7': '27', 'A6': '257', 'C3': '8', 'C2': '237', 'C1': '23', 'E6': '579', 'C7': '9', 'C6': '6', 'C5': '37', 'C4': '4', 'I9': '9', 'D8': '8', 'I8': '7', 'E4': '6', 'D9': '6', 'H8': '2', 'F6': '125', 'A9': '8', 'G4': '9', 'A8': '6', 'E7': '345', 'E3': '379', 'F1': '6', 'F2': '4', 'F3': '23', 'F4': '1235', 'F5': '8', 'E2': '37', 'F7': '35', 'F8': '9', 'D2': '1', 'H1': '4', 'H6': '17', 'H2': '9', 'H4': '17', 'D3': '2379', 'B4': '27', 'B5': '1', 'B6': '8', 'B7': '27', 'E9': '2', 'B1': '9', 'B2': '5', 'B3': '6', 'D6': '279', 'D7': '34', 'D4': '237', 'D5': '347', 'B8': '3', 'B9': '4', 'D1': '5'}

after_naked_twins = {'G7': '6', 'G6': '3', 'G5': '2', 'G4': '9', 'G3': '1', 'G2': '8', 'G1': '7', 'G9': '5', 'G8': '4', 'C9': '1', 'C8': '5', 'C3': '8', 'C2': '237', 'C1': '23', 'C7': '9', 'C6': '6', 'C5': '37', 'A4': '2357', 'A9': '8', 'A8': '6', 'F1': '6', 'F2': '4', 'F3': '23', 'F4': '1235', 'F5': '8', 'F6': '125', 'F7': '35', 'F8': '9', 'F9': '7', 'B4': '27', 'B5': '1', 'B6': '8', 'B7': '27', 'E9': '2', 'B1': '9', 'B2': '5', 'B3': '6', 'C4': '4', 'B8': '3', 'B9': '4', 'I9': '9', 'I8': '7', 'I1': '23', 'I3': '23', 'I2': '6', 'I5': '5', 'I4': '8', 'I7': '1', 'I6': '4', 'A1': '1', 'A3': '4', 'A2': '237', 'A5': '9', 'E8': '1', 'A7': '27', 'A6': '257', 'E5': '347', 'E4': '6', 'E7': '345', 'E6': '579', 'E1': '8', 'E3': '79', 'E2': '37', 'H8': '2', 'H9': '3', 'H2': '9', 'H3': '5', 'H1': '4', 'H6': '17', 'H7': '8', 'H4': '17', 'H5': '6', 'D8': '8', 'D9': '6', 'D6': '279', 'D7': '34', 'D4': '237', 'D5': '347', 'D2': '1', 'D3': '79', 'D1': '5'}

class TestNakedTwins(unittest.TestCase):
    def test_naked_twins(self):
        self.assertEqual(solution.naked_twins(before_naked_twins), after_naked_twins)


diagonal_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
diag_sudoku = solution.grid_values(diagonal_grid)
solved_diag_sudoku = {'G7': '8', 'G6': '9', 'G5': '7', 'G4': '3', 'G3': '2', 'G2': '4', 'G1': '6', 'G9': '5', 'G8': '1', 'C9': '6', 'C8': '7', 'C3': '1', 'C2': '9', 'C1': '4', 'C7': '5', 'C6': '3', 'C5': '2', 'C4': '8', 'E5': '9', 'E4': '1', 'F1': '1', 'F2': '2', 'F3': '9', 'F4': '6', 'F5': '5', 'F6': '7', 'F7': '4', 'F8': '3', 'F9': '8', 'B4': '7', 'B5': '1', 'B6': '6', 'B7': '2', 'B1': '8', 'B2': '5', 'B3': '3', 'B8': '4', 'B9': '9', 'I9': '3', 'I8': '2', 'I1': '7', 'I3': '8', 'I2': '1', 'I5': '6', 'I4': '5', 'I7': '9', 'I6': '4', 'A1': '2', 'A3': '7', 'A2': '6', 'E9': '7', 'A4': '9', 'A7': '3', 'A6': '5', 'A9': '1', 'A8': '8', 'E7': '6', 'E6': '2', 'E1': '3', 'E3': '4', 'E2': '8', 'E8': '5', 'A5': '4', 'H8': '6', 'H9': '4', 'H2': '3', 'H3': '5', 'H1': '9', 'H6': '1', 'H7': '7', 'H4': '2', 'H5': '8', 'D8': '9', 'D9': '2', 'D6': '8', 'D7': '1', 'D4': '4', 'D5': '3', 'D2': '7', 'D3': '6', 'D1': '5'}

class TestDiagonalSudoku(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solution.solve(diag_sudoku), solved_diag_sudoku)


class TestEnvironment(unittest.TestCase):
    """Test initial variables such as boxes, unitlist, unittest
    """
    def test_number_of_boxes_is_81(self):
        # There are 9 * 9 = 81 boxes
        self.assertEqual(len(solution.boxes), 81)

    def test_number_of_unitlist_is_27(self):
        # Because there 9 rows + 9 cols + 9 squares => 27 units
        self.assertEqual(len(solution.unit_list), 27)

    def test_each_box_has_3_units(self):
        # There are 3 constraints: row unit, column unit, square units
        self.assertTrue(all([len(v) == 3 for k, v in solution.units.items()])) 

    def test_each_box_has_20_peers(self):
        # Each box has 20 peers 8 peers in rows + 8 peers in columns + 8 peers in its square - 4 (duplicate)
        self.assertTrue(all([len(v) == 20 for k, v in solution.peers.items()])) 

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
        self.assertEqual(grid_values(values), {'A1': '.', 'A2': '.', 'A3': '3', 'A4': '.', 'A5': '2', 'A6': '.', 'A7': '6', 'A8': '.', 'A9': '.', 'B1': '9', 'B2': '.', 'B3': '.', 'B4': '3', 'B5': '.', 'B6': '5', 'B7': '.', 'B8': '.', 'B9': '1', 'C1': '.', 'C2': '.', 'C3': '1', 'C4': '8', 'C5': '.', 'C6': '6', 'C7': '4', 'C8': '.', 'C9': '.', 'D1': '.', 'D2': '.', 'D3': '8', 'D4': '1', 'D5': '.', 'D6': '2', 'D7': '9', 'D8': '.', 'D9': '.', 'E1': '7', 'E2': '.', 'E3': '.', 'E4': '.', 'E5': '.', 'E6': '.', 'E7': '.', 'E8': '.', 'E9': '8', 'F1': '.', 'F2': '.', 'F3': '6', 'F4': '7', 'F5': '.', 'F6': '8', 'F7': '2', 'F8': '.', 'F9': '.', 'G1': '.', 'G2': '.', 'G3': '2', 'G4': '6', 'G5': '.', 'G6': '9', 'G7': '5', 'G8': '.', 'G9': '.', 'H1': '8', 'H2': '.', 'H3': '.', 'H4': '2', 'H5': '.', 'H6': '3', 'H7': '.', 'H8': '.', 'H9': '9', 'I1': '.', 'I2': '.', 'I3': '5', 'I4': '.', 'I5': '1', 'I6': '.', 'I7': '3', 'I8': '.', 'I9': '.'})

    def test_only_choice(self):
        grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
        values = solution.grid_values(grid)
        result = solution.eliminate(values)
        only_choice_result = solution.only_choice(result)
        self.assertEqual(type(only_choice_result), dict)
        self.assertEqual(only_choice_result, {'A1': '45', 'A2': '8', 'A3': '3', 'A4': '9', 'A5': '2', 'A6': '1', 'A7': '6', 'A8': '5789', 'A9': '57', 'B1': '9', 'B2': '6', 'B3': '47', 'B4': '3', 'B5': '4', 'B6': '5', 'B7': '8', 'B8': '278', 'B9': '1', 'C1': '2', 'C2': '257', 'C3': '1', 'C4': '8', 'C5': '7', 'C6': '6', 'C7': '4', 'C8': '23579', 'C9': '2357', 'D1': '345', 'D2': '345', 'D3': '8', 'D4': '1', 'D5': '3456', 'D6': '2', 'D7': '9', 'D8': '34567', 'D9': '34567', 'E1': '7', 'E2': '2', 'E3': '9', 'E4': '5', 'E5': '34569', 'E6': '4', 'E7': '1', 'E8': '13456', 'E9': '8', 'F1': '1345', 'F2': '13459', 'F3': '6', 'F4': '7', 'F5': '3459', 'F6': '8', 'F7': '2', 'F8': '1345', 'F9': '345', 'G1': '134', 'G2': '1347', 'G3': '2', 'G4': '6', 'G5': '8', 'G6': '9', 'G7': '5', 'G8': '1478', 'G9': '47', 'H1': '8', 'H2': '1467', 'H3': '47', 'H4': '2', 'H5': '5', 'H6': '3', 'H7': '17', 'H8': '6', 'H9': '9', 'I1': '6', 'I2': '9', 'I3': '5', 'I4': '4', 'I5': '1', 'I6': '7', 'I7': '3', 'I8': '8', 'I9': '2'})

    def test_eliminate(self):
        grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
        values = solution.grid_values(grid)
        result = solution.eliminate(values)
        self.assertEqual(type(result), dict)
        self.assertEqual(result, {'A1': '45', 'A2': '4578', 'A3': '3', 'A4': '49', 'A5': '2', 'A6': '147', 'A7': '6', 'A8': '5789', 'A9': '57', 'B1': '9', 'B2': '24678', 'B3': '47', 'B4': '3', 'B5': '47', 'B6': '5', 'B7': '78', 'B8': '278', 'B9': '1', 'C1': '25', 'C2': '257', 'C3': '1', 'C4': '8', 'C5': '79', 'C6': '6', 'C7': '4', 'C8': '23579', 'C9': '2357', 'D1': '345', 'D2': '345', 'D3': '8', 'D4': '1', 'D5': '3456', 'D6': '2', 'D7': '9', 'D8': '34567', 'D9': '34567', 'E1': '7', 'E2': '123459', 'E3': '49', 'E4': '459', 'E5': '34569', 'E6': '4', 'E7': '1', 'E8': '13456', 'E9': '8', 'F1': '1345', 'F2': '13459', 'F3': '6', 'F4': '7', 'F5': '3459', 'F6': '8', 'F7': '2', 'F8': '1345', 'F9': '345', 'G1': '134', 'G2': '1347', 'G3': '2', 'G4': '6', 'G5': '478', 'G6': '9', 'G7': '5', 'G8': '1478', 'G9': '47', 'H1': '8', 'H2': '1467', 'H3': '47', 'H4': '2', 'H5': '457', 'H6': '3', 'H7': '17', 'H8': '1467', 'H9': '9', 'I1': '46', 'I2': '4679', 'I3': '5', 'I4': '4', 'I5': '1', 'I6': '47', 'I7': '3', 'I8': '24678', 'I9': '2467'})

    def test_reduce_puzzle(self):
        grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
        values = solution.grid_values(grid)
        self.assertEqual(solution.reduce_puzzle(values), {'A1': '4', 'A2': '8', 'A3': '3', 'A4': '9', 'A5': '2', 'A6': '1', 'A7': '6', 'A8': '5', 'A9': '7', 'B1': '9', 'B2': '6', 'B3': '7', 'B4': '3', 'B5': '4', 'B6': '5', 'B7': '8', 'B8': '2', 'B9': '1', 'C1': '2', 'C2': '5', 'C3': '1', 'C4': '8', 'C5': '7', 'C6': '6', 'C7': '4', 'C8': '9', 'C9': '3', 'D1': '5', 'D2': '4', 'D3': '8', 'D4': '1', 'D5': '3', 'D6': '2', 'D7': '9', 'D8': '7', 'D9': '6', 'E1': '7', 'E2': '2', 'E3': '9', 'E4': '5', 'E5': '6', 'E6': '4', 'E7': '1', 'E8': '3', 'E9': '8', 'F1': '1', 'F2': '3', 'F3': '6', 'F4': '7', 'F5': '9', 'F6': '8', 'F7': '2', 'F8': '4', 'F9': '5', 'G1': '3', 'G2': '7', 'G3': '2', 'G4': '6', 'G5': '8', 'G6': '9', 'G7': '5', 'G8': '1', 'G9': '4', 'H1': '8', 'H2': '1', 'H3': '4', 'H4': '2', 'H5': '5', 'H6': '3', 'H7': '7', 'H8': '6', 'H9': '9', 'I1': '6', 'I2': '9', 'I3': '5', 'I4': '4', 'I5': '1', 'I6': '7', 'I7': '3', 'I8': '8', 'I9': '2'})


    def test_solve(self):
        grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
        values = {'C8': '123456789', 'B6': '123456789', 'A3': '123456789', 'D8': '6', 'H4': '2', 'B3': '123456789', 'A5': '123456789', 'F4': '123456789', 'F5': '1', 'G4': '6', 'C3': '123456789', 'I3': '4', 'H7': '123456789', 'G9': '123456789', 'A6': '123456789', 'A2': '123456789', 'E4': '123456789', 'D5': '123456789', 'C4': '7', 'A7': '8', 'D7': '123456789', 'H9': '123456789', 'D3': '123456789', 'F3': '123456789', 'H3': '123456789', 'D1': '123456789', 'C5': '123456789', 'G2': '123456789', 'E7': '4', 'H2': '123456789', 'I1': '1', 'F8': '123456789', 'I4': '123456789', 'G3': '123456789', 'G7': '123456789', 'F2': '123456789', 'I6': '123456789', 'F1': '123456789', 'G6': '3', 'B8': '123456789', 'C9': '123456789', 'D2': '2', 'I8': '123456789', 'B7': '123456789', 'E3': '123456789', 'B2': '3', 'E1': '123456789', 'I5': '123456789', 'G1': '123456789', 'A1': '4', 'H5': '123456789', 'I2': '123456789', 'H8': '123456789', 'F6': '123456789', 'E9': '123456789', 'B4': '123456789', 'F7': '123456789', 'D9': '123456789', 'E8': '123456789', 'A8': '123456789', 'I9': '123456789', 'A4': '123456789', 'B5': '123456789', 'H6': '123456789', 'C6': '123456789', 'G8': '7', 'F9': '123456789', 'E2': '123456789', 'C2': '123456789', 'D4': '123456789', 'B1': '123456789', 'A9': '5', 'C7': '123456789', 'I7': '123456789', 'E6': '123456789', 'D6': '123456789', 'B9': '123456789', 'G5': '123456789', 'H1': '5', 'C1': '123456789', 'E5': '8'}
        self.assertEqual(solution.solve(values), {'B4': '1', 'B6': '8', 'E6': '6', 'B9': '7', 'G7': '5', 'E1': '7', 'C1': '9', 'C4': '7', 'D3': '5', 'A5': '6', 'D5': '3', 'E3': '1', 'G1': '2', 'I1': '1', 'F2': '4', 'E7': '4', 'C2': '5', 'E2': '9', 'E8': '3', 'H2': '7', 'H9': '4', 'D4': '4', 'A2': '1', 'F3': '6', 'H4': '2', 'F9': '8', 'B2': '3', 'I9': '3', 'D8': '6', 'G8': '7', 'G2': '8', 'H3': '3', 'A6': '9', 'G4': '6', 'F4': '9', 'F6': '2', 'I5': '7', 'I3': '4', 'A1': '4', 'B7': '9', 'I4': '8', 'A9': '5', 'I7': '2', 'C6': '4', 'H6': '1', 'F8': '5', 'C5': '2', 'F5': '1', 'I2': '6', 'I6': '5', 'D9': '9', 'C3': '8', 'A4': '3', 'A3': '7', 'C9': '6', 'G6': '3', 'B3': '2', 'D6': '7', 'C7': '3', 'D1': '8', 'C8': '1', 'D2': '2', 'A8': '2', 'B8': '4', 'I8': '9', 'A7': '8', 'F7': '7', 'H5': '9', 'G3': '9', 'G5': '4', 'H8': '8', 'B1': '6', 'F1': '3', 'E4': '5', 'E5': '8', 'E9': '2', 'G9': '1', 'B5': '5', 'H7': '6', 'D7': '1', 'H1': '5'})




if __name__ == '__main__':
    unittest.main()

