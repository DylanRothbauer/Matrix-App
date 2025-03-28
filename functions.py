import tkinter as tk
import constants

# Function to clear all widgets from the window
def clear_page(window):
    for widget in window.winfo_children():
        widget.destroy()

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
    clear_page(window)
    
    # Canvas to draw the matrix
    canvas = tk.Canvas(window, width=constants.SCREEN_WIDTH, height=constants.SCREEN_HEIGHT)
    canvas.pack(padx=10, pady=10)

    cell_size = 50
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            x1 = j * cell_size
            y1 = i * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            
            # Draw rectangle
            canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black")
            
            # Draw text in the center of the cell
            canvas.create_text((x1 + x2)//2, (y1 + y2)//2, text=str(matrix[i][j]), font=("Arial", 14))

