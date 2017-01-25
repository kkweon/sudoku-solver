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
    possible_unsolved_boxes = [box for box in boxes if len(values[box]) == 2]

    for i in range(len(possible_unsolved_boxes) - 1):
        first_box = possible_unsolved_boxes[i]
        digits = values[first_box]
        for j in range(i + 1, len(possible_unsolved_boxes)):
            second_box = possible_unsolved_boxes[j]

            # if they have same value
            # check if they belong to the same unit
            # if true, it's naked twins
            if values[second_box] == digits:
                for unit in units[first_box]:
                    if second_box in unit:
                        # Found Naked Twins:
                        for box in unit:
                            if box not in (first_box, second_box):
                                for digit in digits:
                                    values = assign_value(values, box, values[box].replace(digit, ''))

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
    for unit in unitlist:
        for digit in '123456789':
            digit_places = [box for box in unit if digit in values[box]]
            if len(digit_places) == 1:
                values = assign_value(values, digit_places[0], digit)
    return values


def reduce_puzzle(values):
    solved_values = [box for box in boxes if len(values[box]) == 1]
    stalled = False

    while not stalled:
        before_reduce_values = values.copy()

        values = eliminate(values)
        values = only_choice(values)
        #values = naked_twins(values)

        after_reduce_values = values

        if before_reduce_values == after_reduce_values:
            stalled = True

    return values


def solve(grid):
    values = grid_values(grid)
    return search(values)

def search(values):
    values = reduce_puzzle(values)
    if not values:
        # values is stalled -> False
        return values

    if max([len(values[box]) for box in values.keys()]) == 1:
        # solved sudoku and returns values
        return values

    min_len, min_box = min([(len(values[box]), box) for box in values.keys() if len(values[box]) > 1])

    for i in values[min_box]:
        # values[min_box] = "1234"
        # i = "1", "2", "3", "4"
        values_copy = values.copy()
        values_copy[min_box] = i

        result = search(values_copy)

        if result:
            # only return when result is not false
            return result


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
# returns a square unit list. [square1, square2, ..., square9] where
# square1 = ['A1', 'A2', 'A3', 'B1', 'B2', ..., 'C3']


diagonal_units = [[r + c for r, c in zip(rows, cols)]] + [[r + c for r, c in zip(rows, cols[::-1])]]

unitlist = row_units + col_units + square_units + diagonal_units

units = dict([(box, [unit for unit in unitlist if box in unit])
              for box in boxes])
peers = dict([(box, set(sum(units[box], [])) - set([box])) for box in boxes])


if __name__ == '__main__':
    ############## GIVEN CODE BELOW ####################
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
