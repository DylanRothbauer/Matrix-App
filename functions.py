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
