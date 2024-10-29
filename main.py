import tkinter as tk
from tkinter import ttk, messagebox, filedialog, StringVar
import customtkinter as ctk
import shutil, os
from splitmethod import split_method


root = ctk.CTk()
root.title("Imaging Master")
root.geometry("1080x440")

filter_open = False
inserted_ids = set()
folder_path = StringVar()

def open_filter():
    global filter_window_entry, filter_window, filter_open
    if not filter_open:
        filter_open = True
        filter_window = ctk.CTkToplevel(root)
        filter_window.attributes("-topmost", True)
        filter_window.title("ID filter")
        filter_window.geometry("250x500")
        ctk.CTkLabel(filter_window, text="Paste product IDs as column").pack(pady=10)
        filter_window_entry = tk.Text(filter_window, width=10)
        filter_window_entry.pack(pady=10)
        ctk.CTkButton(filter_window, text="Filter", command=execute_id_filter).pack(pady=(5, 5))
        filter_window.protocol("WM_DELETE_WINDOW", close_filter)


def close_filter():
    global filter_open
    filter_window.destroy()
    filter_open = False


def clear_records():
    global inserted_ids
    for i in tree.get_children():
        tree.delete(i)
    inserted_ids.clear()


#Frames START
top_frame = ctk.CTkFrame(root)
top_frame.grid(row=0, column=0, pady=5, padx=5)
product_frame = ctk.CTkFrame(root)
product_frame.grid(row=1, column=0, pady=5, padx=5)
panel_frame = ctk.CTkFrame(root)
panel_frame.grid(row=0, column=1, rowspan=2, pady=5, padx=5)
#Frames END

# PANEL WIDGETS START
id_filter_button = ctk.CTkButton(top_frame, text="ID Filter", command=open_filter)
clear_button = ctk.CTkButton(top_frame, text="Clear", fg_color='firebrick1', hover_color='firebrick3', command=clear_records)
bucket_images_button = ctk.CTkButton(panel_frame, text="Move to ID folder", command=to_id_folder)
id_to_upc_button = ctk.CTkButton(panel_frame, text="Move to UPC folder", command=to_upc_folder)
remove_images_button = ctk.CTkButton(panel_frame, text="Remove images")

file_editing_label = ctk.CTkLabel(panel_frame, text='File editing')

resize_value_entry = ctk.CTkEntry(panel_frame, width=70)
resize_button = ctk.CTkButton(panel_frame, text="Resize", width=60, command=export_treeview)
convert_sp_button = ctk.CTkButton(panel_frame, text="Convert to SP")
convert_png_button = ctk.CTkButton(panel_frame, text="Convert to PNG")

id_filter_button.grid(row=0, column=0, padx=5, pady=5)
clear_button.grid(row=0, column=1, padx=5, pady=5)
bucket_images_button.grid(row=1, column=0, pady=(0, 10), columnspan=2)
id_to_upc_button.grid(row=2, column=0, pady=5, columnspan=2)
remove_images_button.grid(row=3, column=0, pady=5, columnspan=2)
file_editing_label.grid(row=4, column=0, pady=(15, 0), columnspan=2)

resize_value_entry.grid(row=5, column=0, pady=5, padx=5)
resize_button.grid(row=5, column=1, pady=5, padx=5)
convert_sp_button.grid(row=6, column=0, pady=5, columnspan=2)
convert_png_button.grid(row=7, column=0, pady=5, columnspan=2)

tree = ttk.Treeview(product_frame, show="headings", height=14)
tree["columns"] = ("Status", "ID", "MC UPC", "Name", "Folder", "File")
tree.heading("Status", text="Status")
tree.heading("ID", text="ID")
tree.heading("MC UPC", text="MC UPC")
tree.heading("Name", text="Name")
tree.heading("Folder", text="Folder")
tree.heading("File", text="File")

tree.column("Status", width=70)
tree.column("ID", width=70)
tree.column("MC UPC", width=120)
tree.column("Name", width=400)
tree.column("Folder", width=70)
tree.column("File", width=70)
tree.pack()
# PANEL WIDGETS END

root.mainloop()