import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os

# What are the features in Tkinter project?
# 1. Notebook - Multiple Files
# 2. Each file will show Untitled in the beginning until saved
# 3. If no changes - Name (Untitled if no name)
# 4. If changes - Name* 
# 5. Save File to disc
# 6. Open File from disc
# 7. Quit - Close all the tabs and destroy GUI
# 8. Close individual Tabs - Ask to save if not saved
# 9. Key Bindings for shortcuts
# 10. Menu - Cascade - Options - File/Help

text_contents = dict()

def create_file(content='', title='Untitled'):
    # Frame for notebook which will hold 2 components
    # text_area and a scroll bar to the right
    frame_text_area = ttk.Frame(notebook)
    frame_text_area.pack()

    # Text Area setup with title and content in the frame
    text_area = tk.Text(frame_text_area)
    text_area.insert("end", content)
    text_area.pack(fill='both', expand=True)
    
    # Add frame to notebook with the title and select it
    notebook.add(frame_text_area, text=title)
    notebook.select(frame_text_area)
    
    # Scroll bar positioned on the right
    scroll_bar = ttk.Scrollbar(frame_text_area, orient='vertical', command=text_area.yview)
    scroll_bar.pack(side='right', fill='y')
    text_area['yscrollcommand'] = scroll_bar.set
    
    # Store hash of contents of text_area in the dict
    text_contents[str(text_area)] = hash(content)
    

def open_file():
    file_path = filedialog.askopenfilename()
    file_name = os.path.basename(file_path)
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        create_file(content = content, title = file_name)
    except(FileNotFoundError, AttributeError):
        print('File not found, Sorry I could not open the file')
    
def save_file():
    file_path = filedialog.asksaveasfilename()
    file_name = os.path.basename(file_path)

    text_area = text_widget()
    content = text_area.get("1.0", "end-1c")

    try:
        with open(file_path, 'w') as file:
            file.write(content)

        notebook.tab('current', text=file_name)
        text_contents[str(text_area)] = hash(content)
    except(FileNotFoundError, AttributeError):
        print('File not found, Sorry I could not open the file')
        return

def confirm_for_close():
	return messagebox.askyesno(
        message = 'Do you want to close this tab',
        title = 'Info'
    )

def confirm_for_save():
    return messagebox.askyesno(
        message = 'Do you want to save the file',
        title = 'Save'
    )

def text_widget():
    tab = notebook.select()
    if not tab:
        return
    tab_widget = notebook.nametowidget(tab)
    return tab_widget.winfo_children()[0]

def close_tab():
    text_area = text_widget()
    
    if hash[str(text_area)] != text_contents[str(text_area)]:
        if confirm_for_save():
            save_file()
            
    if confirm_for_close():
        if len(notebook.tabs()) == 1:
            create_file()
        notebook.forget(notebook.select())
    else:
        return
    
def quit_gui():
    confirm = confirm_for_close()
    if not confirm:
        return

    unsaved = False
    
    for tab in notebook.tabs():
        tab_widget = root.nametowidget(tab)
        text_area = tab_widget.winfo_children()[0]
        content = text_area.get("1.0", "end-1c")
        if hash(content) != text_contents[str(text_area)]:
            unsaved = True
            
    if unsaved:
        confirm = messagebox.askyesno(
            title='Unsaved Changes', 
            message = 'You have unsaved changes in your files, do you want to quit?'
        )
        if confirm:
            root.destroy()
    else:
        root.destroy()

def show_info():
    messagebox.showinfo(
        message = 'This is an editor which is built using Tkinter for GUI in Python',
        icon = 'info'
    )

def check_for_changes():
    text_area = text_widget()
    if not text_area:
        return
    content = text_area.get("1.0", "end-1c")
    name = notebook.tab('current')['text']

    if hash(content) != text_contents[str(text_area)]:
        if name[-1] != '*':
            notebook.tab('current', text = name + '*')
    else:
        if name[-1] == '*':
            notebook.tab('current', text = name[:-1])       

# Create basic frame for the container
root = tk.Tk()
root.title('PYTHON GUI Editor')

# Prevent Menu options from being torn off
root.option_add('*tearOff', False)

# Create Menu for root
menubar = tk.Menu(root)
# A menubar is added to the root container
# All the other menus will be added to it
# Sub-Menus to those menus will be added
# as commands
root.config(menu=menubar)

file_menu = tk.Menu(menubar)
menubar.add_cascade(menu=file_menu, label='File')

help_menu = tk.Menu(menubar)
menubar.add_cascade(menu=help_menu, label='Help')

# Add Sub-Menus as commands
file_menu.add_command(label='New', command=create_file, accelerator='Ctrl+N')
file_menu.add_command(label='Open', command=open_file, accelerator='Ctrl+O')
file_menu.add_command(label='Save', command=save_file, accelerator='Ctrl+S')
file_menu.add_command(label='Quit', command=quit_gui, accelerator='Ctrl+Q')

help_menu.add_command(label='ShowInfo', command=show_info)

# Bind keys to root container
root.bind('<Control-n>', lambda event: create_file())
root.bind('<Control-o>', lambda event: open_file())
root.bind('<Control-s>', lambda event: save_file())
root.bind('<Control-q>', lambda event: quit_gui())
root.bind('<KeyPress>', lambda event: check_for_changes())

# Create a Frame for root container
main = ttk.Frame(root)
main.pack(side='left', fill='both', expand=True, padx=0, pady=(4, 2))

# Create a notepad for this frame which will hold all the tabs for files
notebook = ttk.Notebook(main)
notebook.pack(side='left', fill='both', expand=True)

root.mainloop()