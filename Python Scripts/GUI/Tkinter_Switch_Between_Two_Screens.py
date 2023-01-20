import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.frame = tk.Frame(self)
        self.frame.pack()

        self.current_frame = 0
        self.frames = [Screen1(self.frame, self), Screen2(self.frame, self)]

        self.show_frame()

    def show_frame(self):
        self.frames[self.current_frame].pack()

    def next_frame(self):
        self.frames[self.current_frame].pack_forget()
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.show_frame()

class Screen1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.label = tk.Label(self, text="This is screen 1")
        self.label.pack()

        self.button = tk.Button(self, text="Next", command=self.controller.next_frame)
        self.button.pack()

class Screen2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.label = tk.Label(self, text="This is screen 2")
        self.label.pack()

        self.button = tk.Button(self, text="Back", command=self.controller.next_frame)
        self.button.pack()

app = App()
app.mainloop()
