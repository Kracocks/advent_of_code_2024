def txt_to_matrix(file_path:str):
    matrix = []
    with open(file_path, 'r') as file:
            for line in file:
                row = list(line.strip())
                matrix.append(row)
    return matrix

def is_xmas(matrix, x, y):
    tl_letter = matrix[x][y]
    tr_letter = matrix[x][y+2]
    center_letter = matrix[x+1][y+1]
    bl_letter = matrix[x+2][y]
    br_letter = matrix[x+2][y+2]
    
    if (center_letter == "A"):
        if (tl_letter == "M"):
            if (br_letter == "S"):

                if (tr_letter == "M"):
                    if (bl_letter == "S"):
                        return True

                elif (tr_letter == "S"):
                    if (bl_letter == "M"):
                        return True

        if (matrix[x][y] == "S"):
            if (br_letter == "M"):

                if (tr_letter == "M"):
                    if (bl_letter == "S"):
                        return True

                elif (tr_letter == "S"):
                    if (bl_letter == "M"):
                        return True
            
    return False

def count_occurence(matrix):
    count = 0
    for i in range(len(matrix)-2):
        for j in range(len(matrix[i])-2):
            if (is_xmas(matrix, i, j)):
                count += 1
    return count

m = txt_to_matrix("day4/input.txt")
print(count_occurence(m))