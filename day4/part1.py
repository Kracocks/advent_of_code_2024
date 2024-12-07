def txt_to_matrix(file_path:str):
    matrix = []
    with open(file_path, 'r') as file:
            for line in file:
                row = list(line.strip())
                matrix.append(row)
    return matrix

def count_occurence(matrix, occurence="XMAS"):
    """Compte les occurrences d'une séquence dans une matrice."""
    count = 0
    seq_len = len(occurence)
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            # Right
            if j + seq_len <= cols:
                if "".join(matrix[i][j:j+seq_len]) == occurence:
                    count += 1

            # Left
            if j - seq_len + 1 >= 0:
                if "".join(matrix[i][j-k] for k in range(seq_len)) == occurence:
                    count += 1

            # Bottom
            if i + seq_len <= rows:
                if "".join(matrix[i+k][j] for k in range(seq_len)) == occurence:
                    count += 1

            # Top
            if i - seq_len + 1 >= 0:
                if "".join(matrix[i-k][j] for k in range(seq_len)) == occurence:
                    count += 1

            # Bottom-right diagonal
            if i + seq_len <= rows and j + seq_len <= cols:
                if "".join(matrix[i+k][j+k] for k in range(seq_len)) == occurence:
                    count += 1

            # Bottom-left diagonal
            if i + seq_len <= rows and j - seq_len + 1 >= 0:
                if "".join(matrix[i+k][j-k] for k in range(seq_len)) == occurence:
                    count += 1

            # Top-right diagonal
            if i - seq_len + 1 >= 0 and j + seq_len <= cols:
                if "".join(matrix[i-k][j+k] for k in range(seq_len)) == occurence:
                    count += 1

            # Top-left diagonal
            if i - seq_len + 1 >= 0 and j - seq_len + 1 >= 0:
                if "".join(matrix[i-k][j-k] for k in range(seq_len)) == occurence:
                    count += 1


    return count
                
m = txt_to_matrix("day4/input.txt")

print(count_occurence(m))