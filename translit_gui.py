from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from translit import *


class Interface(tk.Tk):
    """Class for GUI in tkinter"""

    def __init__(self):
        """Initializing methods proper to the class Interface"""

        tk.Tk.__init__(self)
        self.create_widgets()
        self.images()
        self.translit_text(self)
        self.clear()

    def create_widgets(self):
        """Function creating widgets fo the GUI"""

        # Label for Russian text
        self.label_input = tk.Label(self, text="Put here the original text", fg="SlateBlue2",
                                    bg="snow", font=("Annabelle 15", 20))
        # Text field for Russian text
        self.text_input = tk.Text(self, width=110, height=20, bd=5, wrap=tk.WORD, bg="light yellow", state=NORMAL,
                                  cursor="mouse", insertbackground="IndianRed2")
        # Mouse activation in the field for Russian text
        self.text_input.insert(tk.INSERT, 1.0)
        # Scroll in the field for Russian text
        self.scroll_input = tk.Scrollbar(orient="vertical", command=self.text_input.yview)
        # Button for transliterating
        self.button_tr = tk.Button(self, text="Transliterate", width=15, bg='brown1',
                                   fg='black', font=('Lobster 15 bold', 20),
                                   command=lambda: self.translit_text(self.text_input))
        # Button for saving in file the transliterated text
        self.button_save_file = tk.Button(self, text="Save in file", width=15, bg='brown1',
                                          fg='black', font=('Lobster 15 bold', 20), command=self.save_in_file)
        # Label for transliterated text
        self.label_output = tk.Label(self, text="This is the translitereted text", fg="IndianRed2", bg="snow",
                                     font=("Lobster 15 bold", 20))
        # Text field for transliterated text
        self.text_output = tk.Text(self, width=110, height=20, bd=5, wrap=tk.WORD, bg="light yellow")
        # Scroll for transliterated text
        self.scroll_output = tk.Scrollbar(orient="vertical", command=self.text_output.yview)
        # Button for clearing texts in the fields
        self.button_clear = tk.Button(self, text="Clear", height=2, width=15, bg='light blue',
                                      fg='black', font=('Roboto Slab', 20), command=self.clear)
        # Button to quit the GUI
        self.button_quit = tk.Button(self, text="Quit", height=2, width=15, bg='light blue',
                                     fg='black', font=('Roboto Slab', 20), command=self.quit)
        # Positioning widgets with built-in layout manager grid
        self.label_input.grid(column=1, row=0, sticky=tk.N)
        self.text_input.grid(column=1, row=0, sticky=tk.SW)
        self.scroll_input.grid(column=1, row=0, sticky=tk.E)
        self.text_input.config(yscrollcommand=self.scroll_output.set)
        self.button_tr.grid(column=1, row=1, sticky=tk.SW)
        self.button_save_file.grid(column=1, row=1, sticky=tk.SE)
        self.label_output.grid(column=1, row=2, sticky=tk.N)
        self.text_output.grid(column=1, row=2, sticky=tk.SW)
        self.scroll_output.grid(column=1, row=2, sticky=tk.E)
        self.text_output.config(yscrollcommand=self.scroll_output.set)
        self.button_clear.grid(column=2, row=0)
        self.button_quit.grid(column=2, row=2)
        # Adjusting the GUI to screen format
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.attributes("-fullscreen", False)
        # self.geometry("600x300")

    def images(self):
        """Illustrations in the GUI and their positioning"""

        self.image_1 = Image.open("ru_1.jpg")
        self.photo_1 = ImageTk.PhotoImage(self.image_1)
        self.img_1 = tk.Label(image=self.photo_1, width=450, height=450)
        self.img_1.image = self.photo_1
        self.img_1.grid(rowspan=2, column=0, row=0)
        self.image_2 = Image.open("lat_1.jpg")
        self.photo_2 = ImageTk.PhotoImage(self.image_2)
        self.img_2 = tk.Label(image=self.photo_2, width=450, height=450)
        self.img_2.image = self.photo_2
        self.img_2.grid(rowspan=2, column=0, row=2)

    def translit_text(self, text):
        """Transliterating function going with the imported module translit """

        try:
            t = Translitteration()
            text = self.text_input.get(1.0, END)
            translit_text = self.text_output.insert(END, t.translit_file_cy_lt(text))
            return translit_text
        except Exception as e:
            messagebox.showerror(e)

    def save_in_file(self):
        """Function for saving transliterated text into file"""

        file_path = fd.asksaveasfilename(title="Choose your filename", defaultextension='txt')
        file_type = [('File .txt', '*.txt'), ('File word', '.doc')]
        if not file_type:
            return
        t = Translitteration()
        text = self.text_input.get(1.0, END)
        with open(file_path, "a", encoding='utf-8') as output_file:
            translit_text = t.translit_file_cy_lt(text)
            output_file.write(f'NOTE : IF YOU HAVE THE SYMBOL " IN A TRANSLITERATED WORD, READ TWO PARTS OF THIS WORD \
SEPARATELY !!!\n\n{str(translit_text)}')

    def clear(self):
        """Function for clearing text fields of the GUI"""
        self.text_input.delete(1.0, END)
        self.text_output.delete(1.0, END)


app = Interface()
# Label for GUI
app.title("GUI for transliteration")
# Activation of the GUI
app.mainloop()
