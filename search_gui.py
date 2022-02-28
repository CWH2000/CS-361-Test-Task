import tkinter

import requests, json
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from tkinter.ttk import Treeview

from PIL import Image, ImageTk


class home():
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title('Express Pack')
        self.root.geometry('320x250')
        img = Image.open('color_box.png')
        self.photo = ImageTk.PhotoImage(img)
        main_menu(self.root, self.photo)


class main_menu():
    def __init__(self, master, photo):
        self.master = master
        self.master.config(bg='white')
        # main interface
        self.main_menu = tk.Frame(self.master, bg='white')
        self.main_menu.pack()
        self.photo = photo
        photo_label = Label(self.main_menu, image=self.photo, height=32, width=32, bg='white')
        photo_label.grid(row=0, column=0, sticky=N + S, columnspan=1)
        title_label = Label(self.main_menu, text="Express Track", height=3, width=13, bg='white')
        title_label.config(font=("Helvetica", 16))
        title_label.grid(row=0, column=1, columnspan=4, sticky=N + S)
        quick_search_btn = tk.Button(self.main_menu, text='Quick Search', command=self.quick_search, width=20, height=2,
                                     bg='white')
        quick_search_btn.grid(row=1, columnspan=5, pady=10, sticky=N)
        quick_search_btn = tk.Button(self.main_menu, text='Advanced Search', command=self.advanced_search, width=20,
                                     height=2, bg='white')
        quick_search_btn.grid(row=2, columnspan=5, pady=10, sticky=N)

    def quick_search(self):
        self.main_menu.destroy()
        quick_search(self.master, self.photo)

    def advanced_search(self):
        self.main_menu.destroy()
        advanced_search(self.master, self.photo)


class quick_search():
    def __init__(self, master, photo):
        self.master = master
        self.master.config(bg='white')
        self.quick_search_frame = tk.Frame(self.master, bg='white')
        self.quick_search_frame.pack()
        self.photo = photo
        self.data = {}
        photo_label = Label(self.quick_search_frame, image=self.photo, height=32, width=32, bg='white')
        photo_label.grid(row=0, column=0, sticky=N + S + E)
        title_label = Label(self.quick_search_frame, text="Quick Search", height=3, width=13, bg='white')
        title_label.config(font=("Helvetica", 16))
        title_label.grid(row=0, column=1, columnspan=2, sticky=N + S)

        Label(self.quick_search_frame, text="Express Number", bg='white').grid(row=1, column=0, sticky=N + E, padx=10,
                                                                               pady=10)
        self.number_entry = Entry(self.quick_search_frame)
        self.number_entry.grid(row=1, column=1, sticky=N + E, pady=10)
        back_btn = tk.Button(self.quick_search_frame, text='Back', command=self.back,
                             bg='white')
        back_btn.grid(row=2, column=0, columnspan=1, pady=10, sticky=E)
        quick_search_btn = tk.Button(self.quick_search_frame, text='Search', command=self.search, bg='white')
        quick_search_btn.grid(row=2, column=1, columnspan=1, pady=10, sticky=E)

    def back(self):
        self.quick_search_frame.destroy()
        main_menu(self.master, self.photo)

    def search(self):
        if str.isdigit(self.number_entry.get()):
            self.data['number'] = int(self.number_entry.get())
            self.quick_search_frame.destroy()
            select_time_zone(self.master, self.photo, self.data)
        else:
            tk.messagebox.askquestion('INFO', 'You should input the number!')


class select_time_zone():
    def __init__(self, master, photo, data={}):
        self.master = master
        self.master.config(bg='white')
        self.quick_search_frame = tk.Frame(self.master, bg='white')
        self.quick_search_frame.pack()
        self.photo = photo
        self.data = data
        photo_label = Label(self.quick_search_frame, image=self.photo, height=32, width=32, bg='white')
        photo_label.grid(row=0, column=0, sticky=N + S + E)
        title_label = Label(self.quick_search_frame, text="Select Time Zone", height=3, width=13, bg='white')
        title_label.config(font=("Helvetica", 16))
        title_label.grid(row=0, column=1, columnspan=2, sticky=N + S)

        Label(self.quick_search_frame, text="Time Zone", bg='white').grid(row=1, column=0, sticky=N + E, padx=10,
                                                                          pady=10)
        self.time_zone = Entry(self.quick_search_frame)
        self.time_zone.grid(row=1, column=1, sticky=N + E, pady=10)
        back_btn = tk.Button(self.quick_search_frame, text='Main', command=self.main,
                             bg='white')
        back_btn.grid(row=2, column=0, columnspan=1, pady=10, sticky=E)
        quick_search_btn = tk.Button(self.quick_search_frame, text='Search', command=self.search, bg='white')
        quick_search_btn.grid(row=2, column=1, columnspan=1, pady=10, sticky=E)

    def main(self):
        if tkinter.messagebox.askyesno('Question', 'Your progress would be lost\nAre you Sure?'):
            self.quick_search_frame.destroy()
            main_menu(self.master, self.photo)

    def search(self):
        self.data['time_zone'] = self.time_zone.get()
        self.quick_search_frame.destroy()
        result_gui(self.master, self.photo, self.data)


class search_by_time():
    def __init__(self, master, photo, data={}):
        self.master = master
        self.master.config(bg='white')
        self.search_frame = tk.Frame(self.master, bg='white')
        self.search_frame.pack()
        self.photo = photo
        self.data = data
        photo_label = Label(self.search_frame, image=self.photo, height=32, width=32, bg='white')
        photo_label.grid(row=0, column=0, sticky=N + S + E)
        title_label = Label(self.search_frame, text="Time Search", height=3, width=13, bg='white')
        title_label.config(font=("Helvetica", 16))
        title_label.grid(row=0, column=1, columnspan=2, sticky=N + S)

        Label(self.search_frame, text="Dispatch time", bg='white').grid(row=1, column=0, sticky=N + E, padx=10,
                                                                        pady=10)
        self.time_zone = Entry(self.search_frame)
        self.time_zone.grid(row=1, column=1, sticky=N + E, pady=10)
        back_btn = tk.Button(self.search_frame, text='Back', command=self.back,
                             bg='white')
        back_btn.grid(row=2, column=0, columnspan=1, pady=10, sticky=E)
        quick_search_btn = tk.Button(self.search_frame, text='Search', command=self.search, bg='white')
        quick_search_btn.grid(row=2, column=1, columnspan=1, pady=10, sticky=E)

    def back(self):
        self.search_frame.destroy()
        advanced_search(self.master, self.photo)

    def search(self):
        self.data['time'] = self.time_zone.get()
        self.search_frame.destroy()
        select_time_zone(self.master, self.photo, self.data)


class search_by_number():
    def __init__(self, master, photo, data={}):
        self.master = master
        self.master.config(bg='white')
        self.search_frame = tk.Frame(self.master, bg='white')
        self.search_frame.pack()
        self.photo = photo
        self.data = data
        photo_label = Label(self.search_frame, image=self.photo, height=32, width=32, bg='white')
        photo_label.grid(row=0, column=0, sticky=N + S + E)
        title_label = Label(self.search_frame, text="Number Search", height=3, width=13, bg='white')
        title_label.config(font=("Helvetica", 16))
        title_label.grid(row=0, column=1, columnspan=2, sticky=N + S)

        Label(self.search_frame, text="Express Number", bg='white').grid(row=1, column=0, sticky=N + E, padx=10,
                                                                         pady=10)
        self.number_entry = Entry(self.search_frame)
        self.number_entry.grid(row=1, column=1, sticky=N + E, pady=10)
        back_btn = tk.Button(self.search_frame, text='Back', command=self.back,
                             bg='white')
        back_btn.grid(row=2, column=0, columnspan=1, pady=10, sticky=E)
        quick_search_btn = tk.Button(self.search_frame, text='Search', command=self.search, bg='white')
        quick_search_btn.grid(row=2, column=1, columnspan=1, pady=10, sticky=E)

    def back(self):
        self.search_frame.destroy()
        advanced_search(self.master, self.photo)

    def search(self):
        if str.isdigit(self.number_entry.get()):
            self.data['number'] = int(self.number_entry.get())
            self.search_frame.destroy()
            select_time_zone(self.master, self.photo, self.data)
        else:
            tk.messagebox.askquestion('INFO', 'You should input the number!')


class search_by_location():
    def __init__(self, master, photo, data={}):
        self.master = master
        self.master.config(bg='white')
        self.search_frame = tk.Frame(self.master, bg='white')
        self.search_frame.pack()
        self.photo = photo
        self.data = data
        photo_label = Label(self.search_frame, image=self.photo, height=32, width=32, bg='white')
        photo_label.grid(row=0, column=0, sticky=N + S + E)
        title_label = Label(self.search_frame, text="Location Search", height=3, width=13, bg='white')
        title_label.config(font=("Helvetica", 16))
        title_label.grid(row=0, column=1, columnspan=2, sticky=N + S)

        Label(self.search_frame, text="Dispatch Location", bg='white').grid(row=1, column=0, sticky=N + E,
                                                                            padx=10,
                                                                            pady=10)
        self.time_zone = Entry(self.search_frame)
        self.time_zone.grid(row=1, column=1, sticky=N + E, pady=10)
        back_btn = tk.Button(self.search_frame, text='Back', command=self.back,
                             bg='white')
        back_btn.grid(row=2, column=0, columnspan=1, pady=10, sticky=E)
        quick_search_btn = tk.Button(self.search_frame, text='Search', command=self.search, bg='white')
        quick_search_btn.grid(row=2, column=1, columnspan=1, pady=10, sticky=E)

    def back(self):
        self.search_frame.destroy()
        advanced_search(self.master, self.photo)

    def search(self):
        self.search_frame.destroy()
        self.data['location'] = self.time_zone.get()
        select_time_zone(self.master, self.photo, self.data)


class result_gui():
    def __init__(self, master, photo, data={}):
        self.master = master
        self.master.config(bg='white')
        self.result_frame = tk.Frame(self.master, bg='white')
        self.result_frame.pack()
        self.photo = photo

        tree_date = Treeview(self.result_frame, show="headings", selectmode=tk.BROWSE, height=5)

        # define column
        tree_date['columns'] = ('Express Number', 'Current Position', 'Expected Delivery')
        tree_date.pack()

        # Set the column width
        tree_date.column('Express Number', width=104, anchor="center")
        tree_date.column('Current Position', width=103, anchor="center")
        tree_date.column('Expected Delivery', width=103, anchor="center")

        # Add the column name
        tree_date.heading('Express Number', text='Express Number')
        tree_date.heading('Current Position', text='Current Position')
        tree_date.heading('Expected Delivery', text='Expected Delivery')

        # Add data to the table
        url = 'http://127.0.0.1:5000/search_api'
        r = requests.post(url, json=data)
        for item in r.json()['result']:
            tree_date.insert('', 0, values=(item['express_num'], item['current_pos'], item['expect_delivery']))
        tree_date.pack(expand=False)

        back_btn = tk.Button(self.result_frame, text='Main', command=self.main,
                             bg='white')
        back_btn.pack(expand=True, fill=tk.BOTH, pady=10)

    def main(self):
        if tkinter.messagebox.askyesno('Question', 'Your progress would be lost\nAre you Sure?'):
            self.result_frame.destroy()
            main_menu(self.master, self.photo)

    def search(self):
        self.result_frame.destroy()
        main_menu(self.master, self.photo)


class advanced_search():
    def __init__(self, master, photo):
        self.master = master
        self.master.config(bg='white')
        self.advanced_search_frame = tk.Frame(self.master, bg='white')
        self.advanced_search_frame.pack()
        self.photo = photo
        self.data = {}
        photo_label = Label(self.advanced_search_frame, image=self.photo, height=32, width=32, bg='white')
        photo_label.grid(row=0, column=0, sticky=N + S)
        title_label = Label(self.advanced_search_frame, text="Search Method", height=3, width=13, bg='white')
        title_label.config(font=("Helvetica", 16))
        title_label.grid(row=0, column=1, columnspan=2, sticky=N + S)

        time_search_btn = tk.Button(self.advanced_search_frame, text='Search by time', command=self.time_search,
                                    bg='white',
                                    width=20)
        time_search_btn.grid(row=1, column=0, columnspan=1, pady=10, sticky=E)
        number_search_btn = tk.Button(self.advanced_search_frame, text='Search by number', command=self.number_search,
                                      bg='white', width=20)
        number_search_btn.grid(row=2, column=0, columnspan=1, pady=10, sticky=E)

        quick_search_btn = tk.Button(self.advanced_search_frame, text='Search by location',
                                     command=self.location_search,
                                     bg='white', width=20)
        quick_search_btn.grid(row=3, column=0, columnspan=1, pady=10, sticky=E)
        back_btn = tk.Button(self.advanced_search_frame, text='Back', command=self.back,
                             bg='white')
        back_btn.grid(row=3, column=1, columnspan=1, pady=10, sticky=E)

    def back(self):
        self.advanced_search_frame.destroy()
        main_menu(self.master, self.photo)

    def time_search(self):
        self.advanced_search_frame.destroy()
        search_by_time(self.master, self.photo, self.data)

    def number_search(self):
        self.advanced_search_frame.destroy()
        search_by_number(self.master, self.photo, self.data)

    def location_search(self):
        self.advanced_search_frame.destroy()
        search_by_location(self.master, self.photo, self.data)


if __name__ == '__main__':
    root = tk.Tk()
    home(root)
    root.mainloop()
