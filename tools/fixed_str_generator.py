import tkinter as tk

tables_file = None
strs_file = None

def safe_exit():
	exit()

window = tk.Tk()

# creation area
lbl_tables_filename = tk.Label(text="Insert the tables file name (convention for extension is '.table'):")
ent_tables_filename = tk.Entry()

lbl_strs_filename = tk.Label(text="Insert the strings file name (convention for extension is '.bin'):")
ent_strs_filename = tk.Entry()

lbl_create_atention = tk.Label(text="Atention: If file already exists, will be deleted")

btn_create = tk.Button(text="Create")

def create(event):
	try:
		tables_file = open(ent_tables_filename.get(), "w")
		strs_file = open(ent_strs_filename.get(), "w")
	except:
		print("TODO, deu erro")

btn_create.bind("<Button-1>", create)

def open_create_frame():
	lbl_tables_filename.pack()
	ent_tables_filename.pack()
	lbl_strs_filename.pack()
	ent_strs_filename.pack()
	lbl_create_atention.pack()
	btn_create.pack()


menu = tk.Menu()
menu.add_command(label="Create", command=open_create_frame)
menu.add_command(label="Load")
menu.add_command(label="Exit", command=safe_exit)

window.configure(menu=menu)

window.mainloop()
