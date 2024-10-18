import tkinter as tk
import tkinter.ttk as ttk


class WindowWidget:
    def __init__(self, width, height, name, isTopLevel=False):
        if isTopLevel:
            self.window = tk.Toplevel()
        else:
            self.window = tk.Tk()
        self.width = width
        self.height = height
        self.window.geometry(
            f'{width}x{height}+'
            f'{round((self.window.winfo_screenwidth() - width) / 2)}+'
            f'{round((self.window.winfo_screenheight() - height) / 2)}')
        self.window.title(name)
        self.window.resizable(False, False)

    def makeButton(self, place, text=None, command=None, color='lightblue'):
        button = tk.Button(self.window, text=text, bg=color, command=command)
        button.place(x=place[0], y=place[1], width=place[2], height=place[3])
        return button

    def makeEntry(self, place, color='lightgreen'):
        entry = tk.Entry(self.window, bg=color)
        entry.place(x=place[0], y=place[1], width=place[2], height=place[3])
        return entry

    def makeLabel(self, place, text=None, color='lightpink', image=None, command=None):
        if image:
            label = tk.Label(self.window, image=image, bg=color)
        else:
            label = tk.Label(self.window, text=text, bg=color)
        label.place(x=place[0], y=place[1], width=place[2], height=place[3])
        if command:
            label.bind('<Button-1>', command)
        return label

    def makeListbox(self, place, command=None, color='moccasin'):
        listbox = tk.Listbox(self.window, bg=color)
        listbox.place(x=place[0], y=place[1], width=place[2], height=place[3])
        if command:
            listbox.bind('<Button-1>', command)
        return listbox

    def makeText(self, place, data=None, color='wheat'):
        text = tk.Text(self.window, bg=color)
        text.place(x=place[0], y=place[1], width=place[2], height=place[3])
        if data:
            text.insert('end', data)
        return text

    def makeCombobox(self, place, value=None, color='lightblue'):
        combobox = ttk.Combobox(self.window, background=color)
        combobox.place(x=place[0], y=place[1], width=place[2], height=place[3])
        if value:
            combobox.config(values=value)
            combobox.current(0)
        return combobox
