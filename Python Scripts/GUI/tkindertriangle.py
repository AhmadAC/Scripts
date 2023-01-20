import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x200")
        self.root.title("Tkinter App")

        # Create the first screen
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack()
        self.label1 = tk.Label(self.frame1, text="Enter Token:")
        self.label1.pack()
        self.entry1 = tk.Entry(self.frame1)
        self.entry1.pack()
        self.label2 = tk.Label(self.frame1, text="Enter Chat:")
        self.label2.pack()
        self.entry2 = tk.Entry(self.frame1)
        self.entry2.pack()
        



        # Create the vector triangle button
        self.canvas = tk.Canvas(self.frame1, width=50, height=50)
        self.canvas.pack()
        self.canvas.create_polygon([(0,0), (50,0), (25,50)], fill='black')
        self.canvas.bind('<Button-1>', self.on_button1_clicked)

        # Create the second screen
        self.frame2 = tk.Frame(self.root)
        self.label3 = tk.Label(self.frame2, text="Token:")
        self.label3.pack()
        self.label4 = tk.Label(self.frame2, text="Chat:")
        self.label4.pack()
        self.button2 = tk.Button(self.frame2, text="Back", command=self.on_button2_clicked)
        self.button2.pack()
        self.root.bind('<Return>', self.on_button2_clicked)
        
    def on_button1_clicked(self, event=None):
        self.token = self.entry1.get()
        self.chat = self.entry2.get()
        self.label3.config(text="Token: " + self.token)
        self.label4.config(text="Chat: " + self.chat)
        self.frame1.pack_forget()
        self.frame2.pack()


    def on_button2_clicked(self, event=None):
        self.frame2.pack_forget()
        self.frame1.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
