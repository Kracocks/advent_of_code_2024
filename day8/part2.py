def txt_to_matrix(file_path:str):
    matrix = []
    with open(file_path, 'r') as file:
            for line in file:
                row = list(line.strip())
                matrix.append(row)
    return matrix

antennas = dict() # key = the caracter ; value = list of all their position

def get_antennas(matrix) -> dict[str, list[tuple]]:
    antennas[str, list[tuple]] = dict()
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            carac = matrix[y][x]
            if (carac == '.'):
                continue
            if (carac not in antennas.keys()):
                antennas[carac] = [(x+1, y+1)]
            else:
                antennas[carac].append((x+1, y+1))
    return antennas

def pos_antinodes(antennas:dict[str, list[tuple]], size_x:int, size_y:int) -> set[tuple]:
    antinodes = set()
    antennas_passed:list[tuple] = []
    for carac in antennas.keys():
        for pos_antenna1 in antennas[carac]:
            antennas_passed.append(pos_antenna1)
            antinodes.add(pos_antenna1)
            for pos_antenna2 in antennas[carac]:
                if (pos_antenna2 in antennas_passed):
                    continue
                step = (pos_antenna1[0]-pos_antenna2[0], pos_antenna1[1]-pos_antenna2[1])
                next1 = (pos_antenna1[0] + step[0], pos_antenna1[1] + step[1])
                next2 = (pos_antenna2[0] - step[0], pos_antenna2[1] - step[1])
                
                while (next1[0] >= 0 and next1[0] <= size_x and next1[1] >= 0 and next1[1] <= size_y):
                    antinodes.add(next1)
                    step = (pos_antenna1[0]-pos_antenna2[0], pos_antenna1[1]-pos_antenna2[1])
                    next1 = (next1[0] + step[0], next1[1] + step[1])
                while (next2[0] >= 0 and next2[0] <= size_x and next2[1] >= 0 and next2[1] <= size_y):
                    antinodes.add(next2)
                    step = (pos_antenna1[0]-pos_antenna2[0], pos_antenna1[1]-pos_antenna2[1])
                    next2 = (next2[0] - step[0], next2[1] - step[1])
    return antinodes

def get_nb_antinode_correct(size_x:int, size_y:int, antinodes:set[tuple]) -> int:
    res = set()
    for antinode in antinodes:
        if (antinode[0] >=1 and antinode[1] >= 1 and antinode[0] <= size_x and antinode[1] <= size_y):
            res.add(antinode)
    print(res)
    return len(res)

m = txt_to_matrix("day8/input.txt")
size_x = len(m[0])
size_y = len(m)
print(size_x)
print(size_y)

antennas = get_antennas(m)

antinodes = pos_antinodes(antennas, size_x, size_y)
print(get_nb_antinode_correct(size_x, size_y, antinodes))
