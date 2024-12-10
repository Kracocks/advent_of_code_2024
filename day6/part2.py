def txt_to_matrix(file_path:str):
    matrix = []
    with open(file_path, 'r') as file:
            for line in file:
                row = list(line.strip())
                matrix.append(row)
    return matrix

def get_position_depart(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            match matrix[i][j]:
                case "^":
                    return ((i, j), 0)
                case ">":
                    return ((i, j), 90)
                case "v":
                    return ((i, j), 180)
                case "<":
                    return ((i, j), 270)

def get_front(matrix, guard_position, direction):
    i, j = guard_position
    match direction:
        case 0:
            return matrix[i-1][j] if i > 0 else None
        case 90:
            return matrix[i][j+1] if j < len(matrix[0]) - 1 else None
        case 180:
            return matrix[i+1][j] if i < len(matrix) - 1 else None
        case 270:
            return matrix[i][j-1] if j > 0 else None

def move_position(position, direction):
    i, j = position
    match direction:
        case 0:
            return (i - 1, j)
        case 90:
            return (i, j + 1)
        case 180:
            return (i + 1, j)
        case 270:
            return (i, j - 1)

def can_obstruct(matrix, position, direction):
    i, j = position
    matrix_copy = [row[:] for row in matrix]
    max_steps = len(matrix) * len(matrix[0]) * 4
    steps = 0

    while steps < max_steps:
        steps += 1

        next_cell = get_front(matrix_copy, (i, j), direction)
        if next_cell is None:
            return False
        if next_cell == "#":
            direction = (direction + 90) % 360
        else:
            i, j = move_position((i, j), direction)

    return True

def find_blocking_positions(matrix, position, direction):
    blocking_positions = 0
    empty_positions = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j] == "."]

    for i, j in empty_positions:
        matrix[i][j] = "#"
        if can_obstruct(matrix, position, direction):
            blocking_positions += 1
        matrix[i][j] = "."
    
    return blocking_positions

m = txt_to_matrix("day6/input.txt")

position_depart, direction_depart = get_position_depart(m)
blocking_positions = find_blocking_positions(m, position_depart, direction_depart)

print(blocking_positions)
