import tkinter as tk
2	from tkinter import messagebox
3	
4	# Store all lost items in a list
5	items = []
6	
7	# Function to add an item
8	def add_item():
9	    name = item_entry.get()
10	    location = location_entry.get()
11	
12	    if name == "" or location == "":
13	        messagebox.showwarning("Warning", "Fill all details!")
14	    else:
15	        items.append((name, location))
16	        item_list.insert(tk.END, name + " - " + location)
17	        item_entry.delete(0, tk.END)
18	        location_entry.delete(0, tk.END)
19	        messagebox.showinfo("Success", "Item added!")
20	
21	# Function to search for an item
22	def search_item():
23	    search_name = search_entry.get().lower()
24	    found = False
25	
26	    for name, location in items:
27	        if search_name in name.lower():
28	            messagebox.showinfo(
29	                "Item Found",
30	                name + " was lost at " + location
31	            )
32	            found = True
33	
34	    if not found:
35	        messagebox.showinfo("Result", "No matching item found!")
36	
37	# Create the main app window
38	app = tk.Tk()
39	app.title("Campus Lost & Found")
40	app.geometry("400x500")
41	
42	tk.Label(
43	    app, text="CAMPUS LOST & FOUND",
44	    font=("Arial", 16, "bold")
45	).pack(pady=15)
46	
47	tk.Label(app, text="Lost item name").pack()
48	item_entry = tk.Entry(app)
49	item_entry.pack(pady=5)
50	
51	tk.Label(app, text="Where was it lost?").pack()
52	location_entry = tk.Entry(app)
53	location_entry.pack(pady=5)
54	
55	tk.Button(
56	    app, text="Add Item", command=add_item
57	).pack(pady=10)
58	
59	tk.Label(app, text="Lost Items List").pack()
60	item_list = tk.Listbox(app, width=40, height=8)
61	item_list.pack(pady=5)
62	
63	tk.Label(app, text="Search for an item").pack()
64	search_entry = tk.Entry(app)
65	search_entry.pack(pady=5)
66	
67	tk.Button(
68	    app, text="Search Item", command=search_item
69	).pack(pady=10)
70	
71	# Keep the app running
72	app.mainloop()
