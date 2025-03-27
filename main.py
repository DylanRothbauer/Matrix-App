import tkinter as tk
    
window = tk.Tk()
window.title("My First GUI")
    
label = tk.Label(window, text="Hello, GUI!")
label.pack()
    
button = tk.Button(window, text="Click Me")
button.pack()
    
window.mainloop()