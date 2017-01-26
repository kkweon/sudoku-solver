from itertools import combinations

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


def naked_twins(values, diagonal=True):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers
    possible_unsolved_boxes = [box for box in boxes if len(values[box]) == 2]

    if len(possible_unsolved_boxes) >= 2:
        for first_box, second_box in combinations(possible_unsolved_boxes, 2):
            first_box_digit = values[first_box]
            second_box_digit = values[second_box]

            # If they have same value, check if they belong to the same unit
            # if true, it's naked twins
            if first_box_digit == second_box_digit:
                # Received the feedback (Changed to List Comprehension instead of explicit for loop)
                if diagonal:
                    [[[assign_value(values, box, values[box].replace(digit, '')) for digit in first_box_digit] for box in unit if not box in (first_box, second_box)] for unit in [unit for unit in units[first_box] if second_box in unit]]
                else:
                    [[[assign_value(values, box, values[box].replace(digit, '')) for digit in first_box_digit] for box in unit if not box in (first_box, second_box)] for unit in [unit for unit in units_undiagonal[first_box] if second_box in unit]]

    return values

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a + b for a in A for b in B]


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    values = ['123456789' if char in ('.', '0') else char for char in grid]
    assert len(values) == 81

    return dict(zip(boxes, values))

def display(values):
    """
    Display the values as a 2-D grid.
    
    Args:
        values(dict): The sudoku in dictionary form
    """
    msg = ""
    width = 1 + max(len(values[box]) for box in values.keys())
    line = "+".join(["-" * (width*3)] * 3)
    print("")
    for r in rows:
        row_print = "".join([values[r+c].center(width)  + "|" if c in "36" else values[r+c].center(width)  for c in cols])
        if r in "CF":
            row_print += "\n" + line
        print(row_print)
        msg += row_print + "\n"
    print("")

    return msg

def eliminate(values, diagonal=True):
    """Remove the digit of each known places from its peers

    Args:
        values (dict): {
                            "C1": "123456789" if unknown places
                            "D4": "1" if known
                       }
    """

    # Find solved places and its digit
    # Remove the digit from the peers of each solved place
    solved_places = [box for box in boxes if len(values[box]) == 1]
    for box in solved_places:
        digit = values[box]
        if diagonal:
            its_peers = peers[box]
        else:
            its_peers = peers_undiagonal[box]
        for peer in its_peers:
            values = assign_value(values, peer, values[peer].replace(digit, ''))

    return values


def only_choice(values, diagonal=True):
    # for box in each unit
    # check if a box has unique digit among boxes in the same unit
    # if it does, the box should have that digit assigned
    if not diagonal:
        unit_list = unitlist_undiagonal
    else:
        unit_list = unitlist

    for unit in unit_list:
        for digit in '123456789':
            digit_places = [box for box in unit if digit in values[box]]
            if len(digit_places) == 1:
                values = assign_value(values, digit_places[0], digit)
    return values


def reduce_puzzle(values, diagonal=True):
    stalled = False

    while not stalled:
        # go through eliminate -> only choice -> naked twins
        # if the values did not change after that, it's stalled and just return values
        # if one box has length of 0, there is a problem => return False
        before_reduce_values = values.copy()

        values = eliminate(values, diagonal)
        values = only_choice(values, diagonal)
        values = naked_twins(values, diagonal)

        after_reduce_values = values

        if before_reduce_values == after_reduce_values:
            stalled = True

        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False

    return values


def solve(grid):
    """Find the solution to a Sudoku grid.
    
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    if isinstance(grid, str):
        values = grid_values(grid)
    elif isinstance(grid, dict):
        values = grid
    else:
        raise WrongInputType("Unknown Input Type for solve(grid)")

    values_save = values.copy()
    result = search(values)
    if not result:
        #If it can't solve diagoanl sudoku, solve traditional sudokus
        return search(values_save, diagonal=False)
    return result


def search(values, diagonal=True):
    values = reduce_puzzle(values, diagonal)
    if not values:
        # reduce_puzzle can't solve -> return False
        return values

    if max([len(values[box]) for box in values.keys()]) == 1:
        # solved sudoku -> returns values
        return values

    min_len, min_box = min([(len(values[box]), box) for box in values.keys() if len(values[box]) > 1])

    for i in values[min_box]:
        # choose each case of values[min_box]
        # e.g. values[min_box] = "1234"
        # e.g. i = "1", "2", "3", "4"
        values_copy = values.copy()
        values_copy[min_box] = i

        result = search(values_copy, diagonal)

        if result:
            # only return when result has some values 
            return result


##### Global Variables BEGINS HERE #####
rows = "ABCDEFGHI"
cols = "123456789"

boxes = cross(rows, cols)
# returns each "box" of grid => ["A1", ..., "I9"]

row_units = [cross(r, cols) for r in rows]
# returns a row unit list. [row1, row2, ..., row9] where row1 = ["A1", "A2", ..., "A9"]

col_units = [cross(rows, c) for c in cols]
# returns a column unit list. [col1, col2, ..., col9] where col1 = ["A1", "B1", ..., "I1"]

square_units = [cross(rs, cs) for rs in ["ABC", "DEF", "GHI"] for cs in ["123", "456", "789"]]
# returns a square unit list. [square1, square2, ..., square9] where
# square1 = ['A1', 'A2', 'A3', 'B1', 'B2', ..., 'C3']

diagonal_units = [[r + c for r, c in zip(rows, cols)]] + [[r + c for r, c in zip(rows, cols[::-1])]]
# [diag1, diag2] where diag1 = from left-top to right-bottom
# diag2 = from right-top to left-bottom

unitlist = row_units + col_units + square_units + diagonal_units
unitlist_undiagonal = row_units + col_units + square_units

units = dict([(box, [unit for unit in unitlist if box in unit]) for box in boxes])
units_undiagonal = dict([(box, [unit for unit in unitlist_undiagonal if box in unit]) for box in boxes])

peers = dict([(box, set(sum(units[box], [])) - set([box])) for box in boxes])
peers_undiagonal = dict([(box, set(sum(units_undiagonal[box], [])) - set([box])) for box in boxes])
class WrongInputType(Exception): pass 
##### Global Variables ENDS HERE #####

if __name__ == '__main__':
    ############## GIVEN CODE BELOW ####################
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
