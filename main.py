import ttkbootstrap as tb
from ttkbootstrap.constants import *

root = tb.Window(
  themename="superhero",
  title="TTK Bootstrap!"
  )
root.geometry("500x500")

# create a function for the button
counter = 0
def changer():
    global counter
    counter += 1
    # if counter % 2 == 0:
    #     my_label.config(text="Hello World!")
    # else:
    #     my_label.config(text="Goodbye World!")
    my_label.config(text=f"{counter}")


# create a label
my_label = tb.Label(
    text="Hello World!", font=("Helvetica, 28"), bootstyle="danger, inverse")

# create a button
my_button = tb.Button(
    text="Click Me!", bootstyle="success, outline", command=changer)

# put all the components together
my_label.pack(pady=50)
my_button.pack(pady=20)

# b1 = tb.Button(root, text="Button 1", bootstyle=SUCCESS)
# b1.pack(side=LEFT, padx=5, pady=10)

# b2 = tb.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE))
# b2.pack(side=RIGHT, padx=5, pady=10)

root.mainloop()