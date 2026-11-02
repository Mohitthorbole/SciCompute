
def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("PLEASE ENTER A VALID INTEGER")


def matrix_multiplication():

    # Get number of matrices
    n = get_integer("Enter The Number Of Matrices: ")

    while n < 1:
        print("PLEASE ENTER AT LEAST ONE MATRIX")
        n = get_integer("Enter The Number Of Matrices: ")

    all_matrices = []

    # Input all matrices
    for i in range(n):

        print(f"\n--- Matrix {i + 1} ---")

        rows = get_integer("Enter The Number Of Rows: ")

        while rows < 1:
            print("PLEASE ENTER A POSITIVE NUMBER OF ROWS")
            rows = get_integer("Enter The Number Of Rows: ")

        cols = get_integer("Enter The Number Of Columns: ")

        while cols < 1:
            print("PLEASE ENTER A POSITIVE NUMBER OF COLUMNS")
            cols = get_integer("Enter The Number Of Columns: ")

        matrix = []

        # Input matrix elements
        for r in range(rows):
            row = []

            for c in range(cols):
                val = get_integer(
                    f"Enter element [{r + 1}][{c + 1}]: "
                )
                row.append(val)

            matrix.append(row)

        all_matrices.append(matrix)

    # Display entered matrices
    print("\n--- ENTERED MATRICES ---")

    for i, matrix in enumerate(all_matrices):
        print(f"\nMatrix {i + 1}:")
        for row in matrix:
            print(row)

    # Multiply matrices
    result = all_matrices[0]

    for matrix in all_matrices[1:]:

        # Check multiplication compatibility
        if len(result[0]) != len(matrix):
            print("\nMATRIX MULTIPLICATION IS NOT POSSIBLE")
            return

        new_result = []

        for i in range(len(result)):
            row = []

            for j in range(len(matrix[0])):
                total = 0

                for k in range(len(matrix)):
                    total += result[i][k] * matrix[k][j]

                row.append(total)

            new_result.append(row)

        result = new_result

    # Display final result
    print("\n--- FINAL MULTIPLICATION RESULT ---")

    for row in result:
        print(row)


# Function call
matrix_multiplication()

                    
                        

                                 

