import tkinter as tk
from pages import introduction_page  # Import the introduction page
import constants # Access to our constant variables

# Main application setup
root = tk.Tk()
root.title(constants.TITLE)
root.geometry("600x400")

# Start with the Introduction Page
introduction_page(root)

# Run the Tkinter event loop
root.mainloop()
