from shuffle_2_pdf import *
import tkinter as tk

def create_gui():
    root = tk.Tk()

    # Create message label
    message_label = tk.Label(root, text='')
    message_label.pack()

    # Create button
    def shuffle_and_update():
        pdf_file_name = shuffle_pdf()
        message_label.config(text=f"Shuffled PDF saved {pdf_file_name}")
    
    shuffle_button = tk.Button(root, text='Shuffle PDF', command=shuffle_and_update)
    shuffle_button.pack()

    #bind Enter key with button
    root.bind('<Return>', lambda event: shuffle_button.invoke())

    #bind Esc key with closing the window
    root.bind('<Escape>', lambda event: root.destroy())

    root.mainloop()

if __name__ == '__main__':
    create_gui()
