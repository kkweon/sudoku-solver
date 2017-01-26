"""Includes

1) Sudoku Puzzle Generator

2) values_to_grid function

"""
import random

from solution import (
    boxes,
    reduce_puzzle,
    solve,
    display,
    grid_values
)


def create_puzzle(N=80, diagonal=False):
    """Create a sudoku puzzle with N filled places, recursively
    
    Args:
        N (int, optional): if N = 10, Sudoku Puzzle will be generated with 10 already filled places
    
    Returns:
        str:  a string representation of sudoku puzzle like "....1...4" 
    """
    assert N >= 9
    digits = "123456789"
    values = dict((box, digits) for box in boxes)

    choices = random.sample(list(values), N)
    for choice in choices:
        randint = str(random.randint(1, 9))
        values[choice] = randint

    values = reduce_puzzle(values, diagonal)
    if values:
        solved_places = [values[box] for box in boxes if len(values[box]) == 1]
        if len(solved_places) == N:
            return values_to_grid(values)

    return create_puzzle(N)


def values_to_grid(values):
    """Convert values({"A1":"123456789", "A2":"1", ...})  to grid format (".1.4..5...")
    
    Args:
        values (dict): sudoku values
    
    Returns:
        str: a string representation of sudoku puzzle
    """
    grid = ""
    for box in boxes:
        grid += values.get(box, '.') if len(values.get(box, '.')) == 1 else '.'
    return grid


if __name__ == '__main__':
    puzzle = create_puzzle(15)
    display(grid_values(puzzle))

    solved_puzzle = solve(puzzle)
    display(solved_puzzle)



