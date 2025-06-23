import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Label Packing')

main = tk.Frame(root)
main.pack(side = 'left', fill = 'both', expand = True )
label_one = tk.Label(main, text = 'Label One', bg = 'green' )
label_two = tk.Label(main, text = 'Label Two', bg = 'green' )

# label_one = tk.Label(root, text = 'Label One', bg = 'green' )
# label_two = tk.Label(root, text = 'Label Two', bg = 'green' )

label_two.pack(side = 'top', fill = 'both', expand = True )
label_one.pack(side = 'top', fill = 'both', expand = True )

label_three = tk.Label(root, text='Label Three', bg='red')
label_three.pack(side = 'top', fill = 'y', expand = True )

root.mainloop()
