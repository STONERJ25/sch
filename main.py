import tkinter as tk
import pandas as pd


df = pd.read_excel(r'C:\Users\Joshua Stoner\Desktop\Project for CS Club\Book.xlsx')

column_list1 = df['Code List'].dropna().tolist()
column_list2 = df['Course Title'].dropna().tolist()

# Combine the two lists
course_options_d = column_list1 + column_list2
course_options = list(set(course_options_d))
def on_search(entry_text):
    # Function to handle the search logic
    # In this example, it simply filters a list based on the input
    filtered_results = [item for item in all_results if entry_text.lower() in item.lower()]

    # Update the Listbox with the filtered results
    result_listbox.delete(0, tk.END)  # Clear the current items
    for result in filtered_results:
        result_listbox.insert(tk.END, result)

def add_to_selected_list():
    # Function to add the selected item to the another list
    selected_item = result_listbox.get(tk.ACTIVE)
    if selected_item:
        selected_listbox.insert(tk.END, selected_item)

def remove_selected_item():
    # Function to remove the selected item from the second list
    selected_index = selected_listbox.curselection()
    if selected_index:
        selected_listbox.delete(selected_index)

def out_put_list():
    # Function to remove the selected item from the second list
    selected_items = selected_listbox.get(0, tk.END)
    print("Selected Items:")
    for item in selected_items:
        print(item)
# Sample data for demonstration
all_results = course_options
#["Apple", "Banana", "Orange", "Grapes", "Watermelon", "Pineapple", "Mango", "Strawberry"]

# Create the main window
root = tk.Tk()
root.title("Dynamic Search Example")

# Create an Entry widget for search input
search_entry = tk.Entry(root, width=30)
search_entry.pack(pady=10)

# Create a Listbox to display search results
result_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=30)
result_listbox.pack()

# Create a Listbox to display selected items
selected_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=30)
selected_listbox.pack(pady=10)

# Bind the search function to the Entry widget
search_entry.bind("<KeyRelease>", lambda event: on_search(search_entry.get()))

# Bind the add_to_selected_list function to the Enter key and Double-Click events
result_listbox.bind("<Return>", lambda event: add_to_selected_list())
result_listbox.bind("<Double-Button-1>", lambda event: add_to_selected_list())

# Button to remove selected item from the second list
remove_button = tk.Button(root, text="Remove Selected", command=remove_selected_item)
remove_button.pack()
# Button to remove selected item from the second list
output_button = tk.Button(root, text="Match", command=out_put_list)
output_button.pack()

# Initial display of all results
for result in all_results:
    result_listbox.insert(tk.END, result)

# Start the main event loop
root.mainloop()