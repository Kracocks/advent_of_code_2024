def txt_to_matrix(file_path:str):
    matrix = []
    with open(file_path, 'r') as file:
            for line in file:
                row = list(line.strip())
                matrix.append(row)
    return matrix

# def count_occurence(matrix, occurence = "XMAS"):
#     count = 0
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if (i + len(occurence) <= len(matrix) and i - len(occurence) >= 0):
#                 # vertical bas
#                 if ("".join(row[j] for row in matrix[i:i+len(occurence)])):
#                     count += 1
#                 # vertical haut
#                 if ("".join(row[j] for row in matrix[i:i-len(occurence)])):
#                     count += 1

#             if (j + len(occurence) <= len(matrix[0]) and j - len(occurence) >= 0):
#                 # horizontal droit
#                 if ("".join(matrix[i][j:j+len(occurence)]) == occurence):
#                     count += 1
#                 # horizontal gauche
#                 if ("".join(matrix[i][j:j-len(occurence)]) == occurence):
#                     count += 1

#                 if (i + len(occurence) <= len(matrix) and i - len(occurence) >= 0):
#                     if ("".join(matrix[i+k][j+k] for k in range(len(occurence))) == occurence):
#                         count += 1
#                     if ("".join(matrix[i+k][j-k] for k in range(len(occurence))) == occurence):
#                         count += 1
#                     if ("".join(matrix[i-k][j-k] for k in range(len(occurence))) == occurence):
#                         count += 1
#                     if ("".join(matrix[i-k][j+k] for k in range(len(occurence))) == occurence):
#                         count += 1
#     return count

def count_occurence(matrix, occurence="XMAS"):
    """Compte les occurrences d'une séquence dans une matrice."""
    count = 0
    seq_len = len(occurence)
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            # Droite
            if j + seq_len <= cols:
                if "".join(matrix[i][j:j+seq_len]) == occurence:
                    count += 1

            # Gauche
            if j - seq_len + 1 >= 0:
                if "".join(matrix[i][j-k] for k in range(seq_len)) == occurence:
                    count += 1

            # Bas
            if i + seq_len <= rows:
                if "".join(matrix[i+k][j] for k in range(seq_len)) == occurence:
                    count += 1

            # Haut
            if i - seq_len + 1 >= 0:
                if "".join(matrix[i-k][j] for k in range(seq_len)) == occurence:
                    count += 1

            # Diagonale bas-droite
            if i + seq_len <= rows and j + seq_len <= cols:
                if "".join(matrix[i+k][j+k] for k in range(seq_len)) == occurence:
                    count += 1

            # Diagonale bas-gauche
            if i + seq_len <= rows and j - seq_len + 1 >= 0:
                if "".join(matrix[i+k][j-k] for k in range(seq_len)) == occurence:
                    count += 1

            # Diagonale haut-droite
            if i - seq_len + 1 >= 0 and j + seq_len <= cols:
                if "".join(matrix[i-k][j+k] for k in range(seq_len)) == occurence:
                    count += 1

            # Diagonale haut-gauche
            if i - seq_len + 1 >= 0 and j - seq_len + 1 >= 0:
                if "".join(matrix[i-k][j-k] for k in range(seq_len)) == occurence:
                    count += 1


    return count
                
m = txt_to_matrix("day4/input.txt")

print(count_occurence(m))