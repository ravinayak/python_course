import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Packing Demo") # Added a title for clarity

# The ttk.Label you are using is a "themed" widget. Its primary goal is to look
# "native" on whatever operating system it's running on (Windows, macOS, Linux).
# On some systems, particularly macOS, the native theme dictates that labels should
# be transparent and not have a background color. The ttk theming engine prioritizes
# this native look, often ignoring style settings like background='green'.

# For ttk widgets, styling is best handled with a Style object.
# This ensures a more consistent appearance across different operating systems.
style = ttk.Style(root)

# When you define a custom style like 'Green.Tlabel', you're essentially telling
# Tkinter to create a new style that inherits properties from an existing base style.
# For a ttk.Label widget, the correct base style name is TLabel (with a capital 'L').

# Because you used Tlabel (lowercase 'l'), Tkinter couldn't find a predefined base
# style with that exact name, leading to the "Layout ... not found" error you encountered.

# So, to make your custom style work for ttk.Label widgets, you must use Green.TLabel
# (with a capital 'L').

# 1. Configure a new custom style named 'Green.TLabel'.
#    It inherits the properties of the default 'TLabel' style.
#    We also set the text color to white for better contrast.
style.configure('Green.TLabel', background='green', foreground='white')

# 2. Create the labels and apply the custom style using the 'style' option.
label_one = ttk.Label(root, text='Label One', style='Green.TLabel')
label_two = ttk.Label(root, text='Label Two', style='Green.TLabel')
label_three = ttk.Label(root, text='Label Three') # This one keeps the default style

# Pack all three labels to make them visible on the window.
label_one.pack(side='left', fill='x', expand=True)
label_two.pack(side='left', fill='y', expand=True)
# This label was missing its pack() call, so it was never displayed.
# label_three.pack(side='left', fill='both', expand=True)

# 3. Start the main event loop by calling the method with parentheses.
root.mainloop()
