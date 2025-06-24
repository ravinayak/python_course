import tkinter as tk
from tkinter import ttk

def create_file():
    text_area = tk.Text(notebook)
    # The text area will fill the new tab's frame
    text_area.pack(fill='both', expand=True)
    # Set the title of the tab when adding it to the notebook
    notebook.add(text_area, text='Untitled')
    # Select the newly created tab
    notebook.select(text_area)
    
root = tk.Tk()
root.title('Editor')

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
root.option_add('*tearOff', False)

file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(menu=file_menu, label='File')
file_menu.add_command(label='New', command=create_file)


main = ttk.Frame(root)
# FIX: Removed the invalid 'text' option from the pack() method
main.pack(side='left', fill='both', expand=True, padx=1, pady=(4, 0))

notebook = ttk.Notebook(main)
notebook.pack(side='left', fill='both', expand=True)

create_file()
create_file()
root.mainloop()