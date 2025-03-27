import tkinter as tk
from pages import introduction_page  # Import the introduction page

# Main application setup
root = tk.Tk()
root.title("Matrix Input App")
root.geometry("400x300")

# Start with the Introduction Page
introduction_page(root)

# Run the Tkinter event loop
root.mainloop()
