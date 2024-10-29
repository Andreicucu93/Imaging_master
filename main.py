import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pyodbc, shutil, os
import customtkinter as ctk
from splitmethod import split_method


#Database connection START
conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Space\\Database\\MC_Productlibrary.accdb;'
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("SELECT ID, Desc20, Name FROM MC_Products")

#Database connection END

root = ctk.CTk()
root.title("Imaging mothership")
root.geometry("1080x520")

filter_open = False
inserted_ids = set()

def open_filter():
    global filter_window_entry, filter_window, filter_open
    if not filter_open:
        filter_open = True
        filter_window = ctk.CTkToplevel(root)
        filter_window.attributes("-topmost", True)
        filter_window.title("ID filter")
        filter_window.geometry("250x520")
        ctk.CTkLabel(filter_window, text="Paste product IDs as column").pack(pady=10)
        filter_window_entry = tk.Text(filter_window, width=10)
        filter_window_entry.pack(pady=10)
        ctk.CTkButton(filter_window, text="Filter", command=execute_id_filter).pack(pady=(5, 5))
        filter_window.protocol("WM_DELETE_WINDOW", close_filter)


#1/2 GUI - WIP
#2/2 Database - TBD
def execute_id_filter():
    global filter_window_entry, filter_open, inserted_ids
    input_text = filter_window_entry.get("1.0", "end-1c")
    if input_text:
        items = [item.strip() for item in input_text.split('\n') if item.strip()]
        query = f"SELECT ID, Desc20, Name FROM MC_Products WHERE ID IN ({','.join('?' * len(items))})"
        try:
            cursor.execute(query, *items)
            rows = cursor.fetchall()
            for row in rows:
                id_value = row[0]
                desc_value = row[1]
                name_value = row[2]
                method_result = method_1(desc_value)
                if method_result and len(method_result) >= 2:
                    folder_value = method_result[0]
                    file_value = method_result[1]
                    if id_value not in inserted_ids:
                        tree.insert("", tk.END, values=("", id_value, desc_value, name_value, folder_value, file_value))
                        inserted_ids.add(id_value)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to execute query: {e}")
    filter_window.destroy()
    filter_open = False

#GUI - Completed
def close_filter():
    global filter_open
    filter_window.destroy()
    filter_open = False

#GUI - Completed
def clear_records():
    global inserted_ids
    for i in tree.get_children():
        tree.delete(i)
    inserted_ids.clear()


#1/3 GUI - WIP
#2/3 Database - TBD
#3/3 File_operations - TBD
def to_id_folder():
    if inserted_ids:
        selected_files = os.path.normpath(filedialog.askdirectory())
        if selected_files:
            for row_id in tree.get_children():
                row_data = tree.item(row_id, "values")
                row_data_id = row_data[1]  # ID
                row_data_file = row_data[5]  # File name
                images_loaded = os.listdir(selected_files)
                for image in images_loaded:
                    image_name = os.path.splitext(image)[0]
                    print(f"Processing image: {image_name}")
                    if image_name.startswith(row_data_file):
                        new_folder_path = os.path.join(selected_files, row_data_id)
                        if not os.path.exists(new_folder_path):
                            os.mkdir(new_folder_path)
                        shutil.move(os.path.join(selected_files, image), new_folder_path)
                        print(f"Created {new_folder_path}")
                        print(f"Moved {image}")
                        updated_row_data = ("📦→🆔", row_data[1], row_data[2], row_data[3], row_data[4], row_data[5])
                        tree.item(row_id, values=updated_row_data)
                    else:
                        print(f"{image_name} does not match {row_data_file}")
        else:
            messagebox.showwarning("No Folder Selected", "Please select a valid directory.")
    else:
        messagebox.showinfo(title='Warning', message="Please filter the product ID's.")


#1/3 GUI - WIP
#2/3 Database - TBD
#3/3 File_operations - TBD
def to_upc_folder():
    selected_files = os.path.normpath(filedialog.askdirectory())
    if selected_files:
        all_items = os.listdir(selected_files)
        folders = [item for item in all_items if os.path.isdir(os.path.join(selected_files, item))]
        for folder in folders:
            containing_images = os.listdir(os.path.join(selected_files, folder))
            id_folders_query = f"SELECT ID, Desc20, Name FROM MC_Products WHERE ID = ?"
            try:
                cursor.execute(id_folders_query, (folder,))
                rows = cursor.fetchall()
                for row in rows:
                    id_value = row[0]
                    desc_value = row[1]
                    name_value = row[2]
                    method_result = method_1(desc_value)
                    if method_result and len(method_result) >= 2:
                        folder_value = method_result[0]
                        file_value = method_result[1]
                        print(f'ID: {folder}; Files: {containing_images} UPC_Folder: {folder_value}') #ADD HERE

                        if id_value not in inserted_ids:
                            tree.insert("", tk.END,
                                        values=("", id_value, desc_value, name_value, folder_value, file_value))
                            inserted_ids.add(id_value)
                        destination_folder = os.path.join(selected_files, folder_value)
                        if not os.path.exists(destination_folder):
                            os.mkdir(destination_folder)
                        for file in containing_images:
                            src_file = os.path.join(selected_files, folder, file)
                            dest_file = os.path.join(destination_folder, file)
                            if os.path.exists(dest_file):
                                file_name, file_extension = os.path.splitext(file)
                                new_file_name = f"{file_name}_new{file_extension}"
                                dest_file = os.path.join(destination_folder, new_file_name)
                                print(f"File exists, renaming {file} to {new_file_name}")

                            shutil.move(src_file, dest_file)
                            print(f"Moved {file} to {destination_folder}")
            except Exception as e:
                print(f"Error executing query for folder {folder}: {e}")

    else:
        messagebox.showwarning("No Folder Selected", "Please select a valid directory.")


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
resize_button = ctk.CTkButton(panel_frame, text="Resize", width=60)
convert_sp_button = ctk.CTkButton(panel_frame, text="Convert to SP")
convert_png_button = ctk.CTkButton(panel_frame, text="Convert to PNG")

id_filter_button.grid(row=0, column=0, padx=5)
clear_button.grid(row=0, column=1, padx=5)
bucket_images_button.grid(row=1, column=0, pady=(0, 10), columnspan=2)
id_to_upc_button.grid(row=2, column=0, pady=5, columnspan=2)
remove_images_button.grid(row=3, column=0, pady=5, columnspan=2)

file_editing_label.grid(row=4, column=0, pady=(15, 0), columnspan=2)

resize_value_entry.grid(row=5, column=0, pady=5, padx=5)
resize_button.grid(row=5, column=1, pady=5, padx=5)
convert_sp_button.grid(row=6, column=0, pady=5, columnspan=2)
convert_png_button.grid(row=7, column=0, pady=5, columnspan=2)

tree = ttk.Treeview(product_frame, show="headings")
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