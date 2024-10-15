##1. Write a Python program that performs matrix operations (addition, subtraction, multiplication) using nested loops and functions. The program should handle various matrix input errors such as dimension mismatches, non-numeric entries, or empty matrices, using exception handling and logging.
import logging

# Configure logging
logging.basicConfig(filename='matrix_operations.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def create_matrix(rows, cols):
    """
    Creates a matrix with given rows and columns, taking input from the user.
    Handles non-numeric inputs and empty matrix cases.
    """
    matrix = []
    print(f"Enter elements for a {rows}x{cols} matrix:")
    try:
        for i in range(rows):
            row = input(f"Enter row {i + 1} (space-separated): ").split()
            if len(row) != cols:
                raise ValueError("Incorrect number of elements in row.")
            matrix.append([float(num) for num in row])
        if not matrix:
            raise ValueError("Matrix cannot be empty.")
    except ValueError as e:
        logging.error(f"Error in creating matrix: {e}")
        print(f"Error: {e}")
        return None
    return matrix


def print_matrix(matrix):
    """
    Prints a matrix in a formatted way.
    """
    for row in matrix:
        print(" ".join(map(str, row)))


def add_matrices(matrix1, matrix2):
    """
    Adds two matrices if dimensions match.
    """
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions to add.")
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


def subtract_matrices(matrix1, matrix2):
    """
    Subtracts matrix2 from matrix1 if dimensions match.
    """
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions to subtract.")
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


def multiply_matrices(matrix1, matrix2):
    """
    Multiplies two matrices if dimensions are compatible.
    """
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Matrices cannot be multiplied due to dimension mismatch.")

    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


def matrix_operations():
    try:
        # Input for the first matrix
        rows1 = int(input("Enter number of rows for the first matrix: "))
        cols1 = int(input("Enter number of columns for the first matrix: "))
        matrix1 = create_matrix(rows1, cols1)
        if matrix1 is None:
            raise ValueError("First matrix creation failed.")

        # Input for the second matrix
        rows2 = int(input("Enter number of rows for the second matrix: "))
        cols2 = int(input("Enter number of columns for the second matrix: "))
        matrix2 = create_matrix(rows2, cols2)
        if matrix2 is None:
            raise ValueError("Second matrix creation failed.")

        # Matrix operations menu
        print("\nChoose an operation:")
        print("1. Add Matrices")
        print("2. Subtract Matrices")
        print("3. Multiply Matrices")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            # Perform addition
            print("\nResult of Matrix Addition:")
            result = add_matrices(matrix1, matrix2)
            print_matrix(result)

        elif choice == '2':
            # Perform subtraction
            print("\nResult of Matrix Subtraction:")
            result = subtract_matrices(matrix1, matrix2)
            print_matrix(result)

        elif choice == '3':
            # Perform multiplication
            print("\nResult of Matrix Multiplication:")
            result = multiply_matrices(matrix1, matrix2)
            print_matrix(result)

        else:
            print("Invalid choice! Please choose a valid operation.")

    except ValueError as e:
        logging.error(f"ValueError: {e}")
        print(f"Error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    matrix_operations()
