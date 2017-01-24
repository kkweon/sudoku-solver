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
    pass

def display(values):
    "Display these values as a 2-D grid."
    pass

def eliminate(values):
    pass

def only_choice(values):
    pass

def reduce_puzzle(values):
    pass


def solve(grid):
    pass


def search(values):
    pass


if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(grid_values(diag_sudoku_grid)))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')

    #   | 1 | 2 | 3 | ...
    # A |   |   |   | ...
    # B |   |   |   | ...
    # C |   |   |   | ...
    # . |   |   |   | ...
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

    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(grid_values(diag_sudoku_grid)))

