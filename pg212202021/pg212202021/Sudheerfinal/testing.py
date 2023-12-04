import tkinter as tk

window = tk.Tk()

img = tk.PhotoImage(file='image_output.png')  # has to be `file=`

tk.Label(image=img).pack()

window.after(5000, window.destroy)     # `destroy` without `()`

window.mainloop()
