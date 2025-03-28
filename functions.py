import tkinter as tk

def validate_matrix_input(matrix_entries, rows, cols):
    matrix_data = []
    for r in range(rows):
        row_data = []
        for c in range(cols):
            try:
                value = float(matrix_entries[r][c].get())  # Assuming the matrix is of float values
                row_data.append(value)
            except ValueError:
                return None, "Please enter valid numbers for the matrix."
        matrix_data.append(row_data)
    return matrix_data, ""

def display_matrix(window, matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            label = tk.Label(window, text=str(matrix[i][j]), width=5)
            label.grid(row=i+5, column=j)
