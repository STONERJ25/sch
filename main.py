import tkinter as tk
import pandas as pd
from excelread import Course
import sys


df = pd.read_excel(r'C:\Users\Joshua Stoner\Desktop\Project for CS Club\Book.xlsx')
instances = []

column_list1 = df['Code List'].dropna().tolist()
column_list2 = df['Course Title'].dropna().tolist()
def time_string_to_minutes(time_str):
    # Split the time string into start and end times
    times1111 = time_str.split('-')
    start_time =times1111[0]
    end_time =times1111[1]
    # Function to convert HH:MM[am/pm] to minutes since midnight
    def time_to_minutes(time):
      #  print(time)
        hh, mm, ampm = time[:2], time[-4:-2], time[-2:]

        hh = int(hh)
        mm = int(mm)
        if ampm == 'pm' and hh != 12:
            hh += 12
       # print(hh * 60 + mm)
        return hh * 60 + mm

    # Convert start and end times to minutes
    start_minutes = time_to_minutes(start_time)
    end_minutes = time_to_minutes(end_time)

    # Format the result
    result_str = f'{start_minutes}-{end_minutes}'

    return result_str    
def string_to_tuple(input_string):
    start_str, end_str = input_string.split("-")
    start = int(start_str)
    end = int(end_str)
    return (start, end)

def conflict(dt1,dt2):
    dts1 = dt1.split(" ")
    dts2 = dt2.split(" ")
    days1 = dts1[1]
    time1 = dts1[0]
    days2 = dts2[1]
    time2 = dts2[0]
   # print(time1)
    time11 = string_to_tuple(time_string_to_minutes(time1))
    time22 = string_to_tuple(time_string_to_minutes(time2))
    if have_common_letter(days1, days2):
        if have_common_time(time11, time22):
           # print("We have a common time")
            return True
        else:
            #print("Pass conflict")
            return False
            
    else:
        #print("Pass days")
        return False

def have_common_time(time1, time2):
    return min(time1) <= max(time2) and min(time2) <= max(time1)



def have_common_letter(string1, string2):
    # Create sets of characters for both strings
    set1 = set(string1)
    set2 = set(string2)

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
        instance = Course(item)
    
    # Add the instance to the list
        instances.append(instance)
    mainlogi(instances)
def mainlogi(list_course):
    total_credits=0
    # Print the instances
    for i, instance in enumerate(instances):
        print(f"Course {i + 1}: Name: {instance.code} Time Slots: {instance.time_slots} Credits: {instance.credits} Days: {instance.days}")
    for i, instance in enumerate(instances):
        total_credits +=instance.credits
    if total_credits>20:
        print("Credit total of "+str(total_credits)+ "higher than 20.0, please drop some classes")
    elif total_credits>18:
        print("Credit total of "+str(total_credits)+" requires an override")
    elif total_credits<12:
        print("Credit total of " +str(total_credits)+ " is less than the 12.0 required to be a full time student")
    else:
        print("Credit total of " + str(total_credits))

    master_list = []

    # Initialize master_list with empty lists
    # Determine the dimensions of the 2D list
    num_instances = len(instances)
    max_time_slots = max(len(instance.time_slots) for instance in instances)

    # Initialize master_list as a 2D list
    master_list = [[0] * max_time_slots for _ in range(num_instances)]

    for i, instance in enumerate(instances):
        for j in range(len(instance.time_slots)):
            master_list[i][j] += 1  # Increment the value at index [i][j]



    # Count the number of 1s in each sub-list and store the counts in a new list
    count_of_ones = [sum(1 for element in sublist if element == 1) for sublist in master_list]
    # Print the counts
    #print(count_of_ones)
    course_lister = []
    for r in range(len(count_of_ones)):
        temp_course = []
        for q in range(count_of_ones[r]):
            
            temp_course.append(f'{instances[r].time_slots[q]}'+' '+f'{instances[r].days[q]}')
        course_lister.append(temp_course)
    #print(course_lister)
    from itertools import product
    #print(course_lister)
    def all_combinations(lst):
        if not lst:
            return [()]
        
        first_list = lst[0]
        rest_lists = lst[1:]
        
        # Recursively get all combinations of the rest of the lists
        rest_combinations = all_combinations(rest_lists)
        
        # For each element in the first list, combine it with all combinations of the rest
        result = []
        for element in first_list:
            result.extend((element, *comb) for comb in rest_combinations)
        
        return result

    # Example usage:

    combinations = all_combinations(course_lister)

    def has_shared_property(lst, property_check_func):
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if property_check_func(lst[i], lst[j]):

                    return True
        return False

    for combo in combinations:
        #print(list(combo))
        result = has_shared_property(list(combo), conflict)
        if result==False:
            print("Here is a Schudule that works:" f'{combo}')
            final_schdule = list(combo)
            for i in range(len(final_schdule)):
                print(f'{instances[i].code}: {final_schdule[i]}')
            sys.exit()
            
        else:
            pass
            #print('nope')
    print("No possible Schdule found")

    
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
