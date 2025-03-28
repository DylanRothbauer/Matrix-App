import tkinter as tk
from functions import validate_matrix_input, display_matrix, clear_page

# Introduction Page
def introduction_page(window):
    clear_page(window)

    tk.Label(window, text="Welcome to the Matrix Calculator!", font=("Helvetica", 16)).grid(row=0, column=0, pady=20)
    tk.Label(window, text="This application allows you to input a matrix and calculate its properties.").grid(row=1, column=0, pady=10)
    tk.Label(window, text="Made by Dylan Rothbauer & Colin Kintzinger").grid(row=2, column=0, pady=10)
    tk.Label(window, text="Click 'Start' to begin.").grid(row=3, column=0, pady=10)

    # Button to go to Page 1 (matrix dimension input)
    tk.Button(window, text="Start", command=lambda: page1(window)).grid(row=4, column=0, pady=20)

# Function for Page 1 (Input matrix size: rows and columns)
def page1(window):
    clear_page(window)

    def on_next():
        try:
            # Get matrix dimensions from the user
            rows = int(row_entry.get())
            cols = int(col_entry.get())

            # Pass rows and columns to the next page
            page2(window, rows, cols)
        except ValueError:
            error_label.config(text="Please enter valid integers for rows and columns.")

    # UI components for Page 1
    tk.Label(window, text="Enter the number of rows:").grid(row=0, column=0, pady=5)
    row_entry = tk.Entry(window)
    row_entry.grid(row=0, column=1, pady=5)

    tk.Label(window, text="Enter the number of columns:").grid(row=1, column=0, pady=5)
    col_entry = tk.Entry(window)
    col_entry.grid(row=1, column=1, pady=5)

    # Error message for invalid input
    error_label = tk.Label(window, text="", fg="red")
    error_label.grid(row=2, columnspan=2, pady=5)

    tk.Button(window, text="Next", command=on_next).grid(row=3, columnspan=2, pady=20)

# Function for Page 2 (Input matrix data based on rows and columns)
def page2(window, rows, cols):
    clear_page(window)

    matrix_entries = []

    # Function to collect matrix values and validate
    def on_submit():
        matrix_data, error_msg = validate_matrix_input(matrix_entries, rows, cols)
        if matrix_data is None:
            error_label.config(text=error_msg)
        else:
            print("Matrix Data:", matrix_data)
            # Go to operations page. Also, we should pass the matrix to this page so we can call operations/functions on it
            Operations(window, matrix_data)
            

    # Create the matrix input fields dynamically based on rows and columns
    for r in range(rows):
        row_entries = []
        for c in range(cols):
            entry = tk.Entry(window, width=5)
            entry.grid(row=r, column=c, padx=5, pady=5)  # Add the entry to the grid
            row_entries.append(entry)
        matrix_entries.append(row_entries)

    submit_button = tk.Button(window, text="Submit Matrix", command=on_submit)
    submit_button.grid(row=rows, columnspan=cols, pady=20)

    # Error message for invalid input
    error_label = tk.Label(window, text="", fg="red")
    error_label.grid(row=rows+1, columnspan=cols, pady=5)

    back_button = tk.Button(window, text="Back to Home", command=lambda: page1(window))
    back_button.grid(row=rows+3, columnspan=cols, pady=10)

def Operations(window, matrix):
    clear_page(window)
    tk.Label(window, text="Matrix submitted successfully!").grid(row=1, columnspan=1, pady=20)
    display_matrix(window, matrix)
