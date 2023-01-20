import tkinter as tk

def draw_triangle():
    canvas.create_polygon(
        [device_width / 2 + 80, device_height / 2, 
         device_width / 2, device_height / 2 - 50, 
         device_width / 2, device_height / 2 + 50],
        outline='black', fill='black', width=2
    )

root = tk.Tk()
root.title("Triangle")

device_width = root.winfo_screenwidth()
device_height = root.winfo_screenheight()

canvas = tk.Canvas(root, width=device_width, height=device_height)
canvas.pack()

draw_triangle()

root.mainloop()
