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
            match (matrix[i][j]):
                case "^":
                    return ((i, j), 0)
                case ">":
                    return ((i, j), 90)
                case "v":
                    return ((i, j), 180)
                case "<":
                    return ((i, j), 270)

def get_front(matrix, guard_position, direction):
    try:
        match direction:
            case 0:
                return matrix[guard_position[0]-1][guard_position[1]]
            case 90:
                return matrix[guard_position[0]][guard_position[1]+1]
            case 180:
                return matrix[guard_position[0]+1][guard_position[1]]
            case 270:
                return matrix[guard_position[0]][guard_position[1]-1]
    except:
        return None
            
def start(matrix, position:tuple, direction:int):
    res = 0
    while (get_front(matrix, position, direction) != None):
        if (get_front(matrix, position, direction) == "#"):
            direction = (direction+90)%360
        # advence
        matrix[position[0]][position[1]] = "X"
        match direction:
            case 0:
                position = (position[0]-1, position[1])
            case 90:
                position = (position[0], position[1]+1)
            case 180:
                position = (position[0]+1, position[1])
            case 270:
                position = (position[0], position[1]-1)
        if (matrix[position[0]][position[1]] != "X"):
            res += 1
    return res +1

m = txt_to_matrix("day6/test.txt")

position_depart, direction_depart = get_position_depart(m)
print(start(m, position_depart, direction_depart))

print(m)