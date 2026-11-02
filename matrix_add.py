
def get_integer(prompt):
    try:
        return int(input(prompt))

    except ValueError:
        print("PLEASE ENTER A VALID INTEGER")
        return get_integer(prompt)


def matrix_addition():

    n = get_integer("Enter The Number Of Matrices: ")

    while n < 2:
        print("PLEASE ENTER AT LEAST TWO MATRICES")
        n = get_integer("Enter The Number Of Matrices: ")

    all_matrices = []

    for _ in range(n):

        rows = get_integer("Enter The Number Of Rows: ")

        while rows < 1:
            print("ENTER A POSITIVE NUMBER OF ROWS")
            rows = get_integer("Enter The Number Of Rows: ")

        cols = get_integer("Enter The Number Of Columns: ")

        while cols < 1:
            print("PLEASE ENTER A POSITIVE NUMBER OF COLUMNS")
            cols = get_integer("Enter The Number Of Columns: ")

        current_matrix = []

        for i in range(rows):
            row = []

            for j in range(cols):
                elements = get_integer(
                    f"ENTER THE [{i}][{j}] POSITION VALUE: "
                )
                row.append(elements)

            current_matrix.append(row)

        all_matrices.append(current_matrix)

    # Checking dimensions
    rows = len(all_matrices[0])
    cols = len(all_matrices[0][0])

    for matrix in all_matrices:

        if len(matrix) != rows or len(matrix[0]) != cols:
            print("MATRIX ADDITION IS NOT POSSIBLE")
            return

    # Initializing result matrix
    result = []

    for i in range(rows):
        row = []

        for j in range(cols):
            total = 0

            for k in range(n):
                total += all_matrices[k][i][j]

            row.append(total)

        result.append(row)

    # Displaying result
    print("\nTHE RESULTANT MATRIX IS:")

    for row in result:
        print(*row)


matrix_addition()


