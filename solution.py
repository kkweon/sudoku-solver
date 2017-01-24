assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.

    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers


def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a + b for a in A for b in B]


def grid_values(grid):
    "Convert grid into a dict of {square: char} with '.' for empties."
    values = ['123456789' if char in ('.', '0') else char for char in grid]
    assert len(values) == 81

    return dict(zip(boxes, values))

def display(values):
    "Display these values as a 2-D grid."
    msg = """
|-------+-------+-------|
| {A1} {A2} {A3} | {A4} {A5} {A6} | {A7} {A8} {A9} |
| {B1} {B2} {B3} | {B4} {B5} {B6} | {B7} {B8} {B9} |
| {C1} {C2} {C3} | {C4} {C5} {C6} | {C7} {C8} {C9} |
|-------+-------+-------|
| {D1} {D2} {D3} | {D4} {D5} {D6} | {D7} {D8} {D9} |
| {E1} {E2} {E3} | {E4} {E5} {E6} | {E7} {E8} {E9} |
| {F1} {F2} {F3} | {F4} {F5} {F6} | {F7} {F8} {F9} |
|-------+-------+-------|
| {G1} {G2} {G3} | {G4} {G5} {G6} | {G7} {G8} {G9} |
| {H1} {H2} {H3} | {H4} {H5} {H6} | {H7} {H8} {H9} |
| {I1} {I2} {I3} | {I4} {I5} {I6} | {I7} {I8} {I9} |
|-------+-------+-------|
""".format(**values) 
    print(msg)
    return msg


def eliminate(values):
    """Remove the digit of each known places from its peers
    
    Args:
        values (dict): {
                            "C1": "123456789" if unknown places
                            "D4": "1" if known
                       }
    """
    solved_places = [box for box in boxes if len(values[box]) == 1]
    for box in solved_places:
        digit = values[box]
        its_peers = peers[box]
        for peer in its_peers:
            values = assign_value(values, peer, values[peer].replace(digit, ''))

    return values

def only_choice(values):
    for unit in unit_list:
        for digit in '123456789':
            digit_places = [box for box in unit if digit in values[box]]
            if len(digit_places) == 1:
                values = assign_value(values, digit_places[0], digit)
    return values

def reduce_puzzle(values):
    solved_values = [box for box]
    pass


def solve(grid):
    pass


def search(values):
    pass


# Global Variables
rows = "ABCDEFGHI"
cols = "123456789"

boxes = cross(rows, cols) 
# returns each "box" of grid => ["A1", ..., "I9"]

row_units = [cross(r, cols) for r in rows]
# returns a row unit list. [row1, row2, ..., row9] where row1 = ["A1", "A2", ..., "A9"]

col_units = [cross(rows, c) for c in cols]
# returns a column unit list. [col1, col2, ..., col9] where col1 = ["A1", "B1", ..., "I1"]

square_units = [cross(rs, cs) for rs in ["ABC", "DEF", "GHI"] for cs in ["123", "456", "789"]] 
# returns a square unit list. [square1, square2, ..., square9] where square1 = ['A1', 'A2', 'A3', 'B1', 'B2', ..., 'C3']

unit_list = row_units + col_units + square_units

units = dict([(box, [unit for unit in unit_list if box in unit]) for box in boxes])
peers = dict([(box, set(sum(units[box], [])) - set([box])) for box in boxes])


if __name__ == '__main__':
    ############## GIVEN CODE BELOW ####################
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    #display(solve(grid_values(diag_sudoku_grid)))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')



