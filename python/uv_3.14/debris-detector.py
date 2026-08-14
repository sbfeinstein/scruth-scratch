from copy import deepcopy

SPACE_CHAR = "·"
CELL_RENDER_WIDTH = 3
next_ship_id = 2


def main():
    """
    A ship is represented as a double array
     0 is empty space
     1 is a regular part of ship 1
     -1 is a core part of ship 1

    A ship always has exactly one core part

    Part coordinates are always given as (row, col) in the double array, with
    zero-based indexes for both.

    Destroying a regular part may result in some of the ship no longer being connected
    to the core. In this case, a new debris "ship" with the next incremental ID is
    "created" from the disconnected parts.  For the new debris ship, the first part
    (that was adjacent to the destroyed part) is promoted to core.

    Output:

        0  1  2  3  4  5  6  7  8  9
     0  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
     1  ·  ·  ·  ·  1  1  1  ·  ·  ·
     2  ·  ·  ·  ·  1  ·  1  ·  ·  ·
     3  ·  ·  1  1  1  1 -1  ·  ·  ·
     4  ·  ·  ·  ·  1  ·  ·  ·  ·  ·
     5  ·  ·  ·  ·  1  1  ·  ·  ·  ·
     6  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·

    Destroying part (3,4)!

        0  1  2  3  4  5  6  7  8  9
     0  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
     1  ·  ·  ·  ·  1  1  1  ·  ·  ·
     2  ·  ·  ·  ·  1  ·  1  ·  ·  ·
     3  ·  ·  3 -3  ·  1 -1  ·  ·  ·
     4  ·  ·  ·  · -2  ·  ·  ·  ·  ·
     5  ·  ·  ·  ·  2  2  ·  ·  ·  ·
     6  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·

    """
    ship_1 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, -1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    render(ship_1)
    print("Destroying part (3,4)!")
    output = destroy(ship_1, 3, 4)
    render(output)


def render(ship):
    print()
    print(" " * CELL_RENDER_WIDTH, end="")
    for col_header in range(0, len(ship[0])):
        print(f"{col_header:^{CELL_RENDER_WIDTH}}", end="")
    print()
    for row_header, row in enumerate(ship):
        print(f"{row_header:^{CELL_RENDER_WIDTH}}", end="")
        for cell in row:
            val = cell if cell != 0 else SPACE_CHAR
            print(f"{val:^{CELL_RENDER_WIDTH}}", end="")
        print()
    print()


def destroy(ship, row, col):
    new_ship = deepcopy(ship)

    if ship[row][col] == 0 or ship[row][col] < 0:
        # Can't destroy empty space or a core part
        return new_ship

    # Destroy the given part by making it empty space
    new_ship[row][col] = 0

    # Potentially create a new ship for each part adjacent to what was destroyed
    make_new_ship_if_disconnected(new_ship, row - 1, col)
    make_new_ship_if_disconnected(new_ship, row + 1, col)
    make_new_ship_if_disconnected(new_ship, row, col - 1)
    make_new_ship_if_disconnected(new_ship, row, col + 1)

    return new_ship


def make_new_ship_if_disconnected(ship, row, col):
    """
    If the adjacent parts starting at (row, col) are not connected to any core,
    make them a new ship with the given (row, col) as a new core.
    """
    global next_ship_id

    # Return immediately for out-of-bounds coords
    if row < 0 or col < 0 or row > len(ship) or col > len(ship[0]):
        return

    disconnected_parts = disconnected_from_any_core(ship, row, col)

    # Return immediately if there were no disconnected parts starting from the
    # given coordinates
    if not disconnected_parts:
        return

    for disconnected_row, disconnected_col in disconnected_parts:
        ship[disconnected_row][disconnected_col] = next_ship_id
    ship[row][col] = -next_ship_id

    next_ship_id += 1


def disconnected_from_any_core(ship, root_row, root_col):
    coords_queue = [(root_row, root_col)]
    disconnected = []
    visited = set()

    while coords_queue:
        row, col = coords_queue.pop()

        # Ignore coords that are out of bounds
        if row < 0 or col < 0 or row > len(ship) or col > len(ship[0]):
            continue

        # Ignore visited coords
        if (row, col) in visited:
            continue
        else:
            visited.add((row, col))

        # Ignore empty space
        if ship[row][col] == 0:
            continue

        # If any core is found, the overall answer is there are no disconnected parts
        # so return an empty result
        if ship[row][col] < 0:
            return []

        disconnected.append((row, col))
        coords_queue.append((row - 1, col))
        coords_queue.append((row + 1, col))
        coords_queue.append((row, col - 1))
        coords_queue.append((row, col + 1))

    return disconnected


if __name__ == "__main__":
    main()
