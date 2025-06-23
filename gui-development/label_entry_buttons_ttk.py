import tkinter as tk
from tkinter import ttk

# This is the root container - primary UI component which will hold all the other
# UI components inside it such as labels, text fields, buttons
root = tk.Tk()
root.title('Greeter')

user_name = tk.StringVar()

def greet():
    print(f'UserName :: {user_name.get() or 'Hello World!'}')

# Primary UI Components such as buttons, labels, entry fields are created inside
# the root container, when we provide root as the parameter to any UI component
# it indicates that the UI component is a child of root - meaning it will be 
# placed inside the root component
# There are two steps to setting up a UI Component inside root
#	a. Creation of UI Component:
#		1. Here we define the UI component whose child this component will be
#		2. Name of the UI Component, (key = text)
#		3. Any Command, width, padding for this UI Component, ( key = command )
# 	b. Pack the UI Component: (Place the component on the GUI Container)
#		1. Side on which to pack the component - left/right, ( key = side )
#		2. Fill: x/y - the axis on which this component will fill if expanded, ( key = fill )
#		3. expand: true/false - if we enlarge the container, will this UI component, ( key = expand )
#		   expand and along which axis

label = ttk.Label(root, text='Username')
# A label must be packed to a side and there should be padding along X-axis
label.pack(side='left', padx=(0, 10))

# An input field is defined as an Entry, we must specify its width and a variable to hold the
# data input by user
entry = ttk.Entry(root, width=15, textvariable=user_name)
entry.pack(side='left')
entry.focus()

# A button must have some text to identify it and a command to execute when it is clicked
# The button shall fill along x/y direction and if the root container is enlarged, it can
# possibly expand or not
button = ttk.Button(root, text='Greet', command=greet)
button.pack(side="left", fill='x', expand=True)

quit_button = ttk.Button(root, text='Quit', command=root.destroy)
quit_button.pack(side='left')

# This will run the GUI application until it is closed or root.destroy is called through
# a button
root.mainloop()
