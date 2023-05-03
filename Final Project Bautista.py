import tkinter as tk

# create a GUI window
root = tk.Tk()

# title of the GUI
root.title('Bautista Pizza Palace')

# set the size
root.geometry('500x500')

# order question
title = tk.Label(root, text='What would you like to order?', font='Inter, 20')
title.pack()

# add price label
small_label = tk.Label(root, text='Small Pizza: $8.99', font='Inter, 12')
small_label.pack()

# add price label
medium_label = tk.Label(root, text='Medium Pizza: $9.99', font='Sans, 12')
medium_label.pack()

# add price label
large_label = tk.Label(root, text='Large Pizza: $10.99', font='Helvetica, 12')
large_label.pack()

# add price label
hotdog_label = tk.Label(root, text='Hot Dog: $1.99', font='Inter, 12')
hotdog_label.pack()

# click this button to order small pizza
small_label = tk.Button(root, text='Click here to order a small pizza.', height=2, width=30)
small_label.pack()

# click this button to order medium pizza
medium_label = tk.Button(root, text='Click here to order a medium pizza.', height=2, width=30)
medium_label.pack()

# click this button to order large pizza
large_label = tk.Button(root, text='Click here to order a large pizza.', height=2, width=30)
large_label.pack()

# click this button to order hotdog
hotdog_label = tk.Button(root, text='Click here to order a hotdog.', height=2, width=30)
hotdog_label.pack()

submit_button = tk.Button(root, text='Submit your order.', height=2, width=30)
submit_button.pack()

# click this button to exit the program
exit_button = tk.Button(root, text='Exit', command=root.destroy, height=2, width=30)
exit_button.pack()

# start the GUI
root.mainloop()
