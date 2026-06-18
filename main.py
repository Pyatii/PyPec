import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os
from hashlib import sha256
from test import Database


db = Database()

root = tk.Tk()
root.title("СУБД")
root.geometry("720x480")
root.resizable(False, False)

def Run():
    query = txt_input.get("1.0", "end")
    data=db.read(query)
    spawn_new_window(data, len(data[0])*[""])

def Clr():
    txt_input.delete("1.0", "end")

def spawn_new_window(columns, headings):
    root_n = tk.Toplevel(root)
    root_n.title("Окно вывода")
    root_n.grab_set()
    root_n.focus_set()

    table = ttk.Treeview(root_n, columns=headings, show="headings")
    table.pack(fill=tk.BOTH, expand = 1)
    for i in headings:
        table.heading(i, text = i)

    for i in columns:
        table.insert("", tk.END, values=i)






frame_buttons = tk.Frame(root)
btn_run = tk.Button(frame_buttons, text = "Run", command = Run)
btn_run.pack(side = tk.LEFT, padx=5)
btn_clear = tk.Button(frame_buttons, text = "Clear", command = Clr)
btn_clear.pack(side = tk.LEFT, padx=5)
frame_buttons.pack()

txt_input = tk.Text(root)
txt_input.pack()

root.mainloop()
