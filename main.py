import tkinter as tk
import pandas as pd
from excelread import Course
import sys


df = pd.read_excel(r'Book.xlsx')
instances = []

column_list1 = df['Code List'].dropna().tolist()
column_list2 = df['Course Title'].dropna().tolist()

def time_string_to_minutes(time_str):

    times1111 = time_str.split('-')
    start_time =times1111[0]
    end_time =times1111[1]

    def time_to_minutes(time):

        hh, mm, ampm = time[:2], time[-4:-2], time[-2:]

        hh = int(hh)
        mm = int(mm)
        if ampm == 'pm' and hh != 12:
            hh += 12

        return hh * 60 + mm


    start_minutes = time_to_minutes(start_time)
    end_minutes = time_to_minutes(end_time)

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
    time11 = string_to_tuple(time_string_to_minutes(time1))
    time22 = string_to_tuple(time_string_to_minutes(time2))
    if have_common_letter(days1, days2):

        if have_common_time(time11, time22):
            return True
        else:
            return False
            
    else:

        return False

def have_common_time(time1, time2):
    if min(time1) <= max(time2) and min(time2) <= max(time1):
        return True
    elif min(time2)==min(time1):
        return True
    elif max(time2)==max(time1):
        return True
    else:
        return False


def have_common_letter(string1, string2):

    set1 = set(string1)
    set2 = set(string2)

    # Check if there is any common letter
    common_letters = set1.intersection(set2)

    # Return True if there are common letters, otherwise False
    return len(common_letters) > 0


def on_search(entry_text):


    filtered_results = [item for item in all_results if entry_text.lower() in item.lower()]

    result_listbox.delete(0, tk.END)  
    for result in filtered_results:
        result_listbox.insert(tk.END, result)

def add_to_selected_list():

    selected_item = result_listbox.get(tk.ACTIVE)
    if selected_item:
        selected_listbox.insert(tk.END, selected_item)

def remove_selected_item():

    selected_index = selected_listbox.curselection()
    if selected_index:
        selected_listbox.delete(selected_index)

def out_put_list():

    instances = []
    selected_items = selected_listbox.get(0, tk.END)
    #print("Selected Items:")
    for item in selected_items:
      #  print(item)
        instance = Course(item)
    

        instances.append(instance)
    mainlogi(instances)
def mainlogi(list_course):
    total_credits = 0
    # Create a Text widget to display output

    def clear_text():
        # Function to clear the Text widget
        text_widget.delete(1.0, tk.END)
    def append_to_text(msg):
        # Function to append text to the Text widget
        text_widget.insert(tk.END, msg + "\n")
        text_widget.see(tk.END)
    clear_text()
    #for i, instance in enumerate(list_course):
    #    append_to_text(f"Course {i + 1}: Name: {instance.code} Time Slots: {instance.time_slots} Credits: {instance.credits} Days: {instance.days}")

    for i, instance in enumerate(list_course):
        total_credits += instance.credits

    if total_credits > 20:
        append_to_text("Credit total of " + str(total_credits) + " higher than 20.0, please drop some classes")
    elif total_credits > 18:
        append_to_text("Credit total of " + str(total_credits) + " requires an override")
    elif total_credits < 12:
        append_to_text("Credit total of " + str(total_credits) + " is less than the 12.0 required to be a full-time student")
    else:
        append_to_text("Credit total of " + str(total_credits))

    master_list = []

    num_instances = len(list_course)
    max_time_slots = max(len(instance.time_slots) for instance in list_course)

    master_list = [[0] * max_time_slots for _ in range(num_instances)]

    for i, instance in enumerate(list_course):
        for j in range(len(instance.time_slots)):
            master_list[i][j] += 1

    count_of_ones = [sum(1 for element in sublist if element == 1) for sublist in master_list]

    course_lister = []
    for r in range(len(count_of_ones)):
        temp_course = []
        for q in range(count_of_ones[r]):
            temp_course.append(f'{list_course[r].time_slots[q]}' + ' ' + f'{list_course[r].days[q]}')
        course_lister.append(temp_course)

    from itertools import product

    def all_combinations(lst):
        if not lst:
            return [()]

        first_list = lst[0]
        rest_lists = lst[1:]

        rest_combinations = all_combinations(rest_lists)

        result = []
        for element in first_list:
            result.extend((element, *comb) for comb in rest_combinations)

        return result

    combinations = all_combinations(course_lister)

    def has_shared_property(lst, property_check_func):
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):

                if property_check_func(lst[i], lst[j]):

                    return True
        return False

    flag = True
    for combo in combinations:
        result = has_shared_property(list(combo), conflict)
        if result == False:
            append_to_text("Here is a Schedule that works:" )
            final_schedule = list(combo)
            for i in range(len(final_schedule)):
                append_to_text(f'{list_course[i].name} {list_course[i].code}: {final_schedule[i]}')
            flag = False
            break
        else:
            pass

    if flag:
        append_to_text("No possible Schedule found")

    '''
    total_credits=0

    for i, instance in enumerate(list_course):
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


    num_instances = len(list_course)
    max_time_slots = max(len(instance.time_slots) for instance in list_course)


    master_list = [[0] * max_time_slots for _ in range(num_instances)]

    for i, instance in enumerate(list_course):
        for j in range(len(instance.time_slots)):
            master_list[i][j] += 1  




    count_of_ones = [sum(1 for element in sublist if element == 1) for sublist in master_list]

    course_lister = []
    for r in range(len(count_of_ones)):
        temp_course = []
        for q in range(count_of_ones[r]):
            
            temp_course.append(f'{list_course[r].time_slots[q]}'+' '+f'{list_course[r].days[q]}')
        course_lister.append(temp_course)

    from itertools import product

    def all_combinations(lst):
        if not lst:
            return [()]
        
        first_list = lst[0]
        rest_lists = lst[1:]
        

        rest_combinations = all_combinations(rest_lists)
        
    
        result = []
        for element in first_list:
            result.extend((element, *comb) for comb in rest_combinations)
        
        return result



    combinations = all_combinations(course_lister)

    def has_shared_property(lst, property_check_func):
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if property_check_func(lst[i], lst[j]):

                    return True
        return False
    flag = True
    for combo in combinations:

        result = has_shared_property(list(combo), conflict)
        if result==False:
            print("Here is a Schudule that works:" f'{combo}')
            final_schdule = list(combo)
            for i in range(len(final_schdule)):
                print(f'{list_course[i].code}: {final_schdule[i]}')
            flag = False
            break
            
        else:
            pass
    if  flag:
        print("No possible Schedule found")
    '''

l1 = list(set(column_list1))
l2 = list(set(column_list2))
l1.sort()
l2.sort()


all_results = l1+l2



root = tk.Tk()
root.title("Schedule Generator")

search_entry = tk.Entry(root, width=30)
search_entry.pack(pady=10)
result_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=30)
result_listbox.pack()


selected_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=30)
selected_listbox.pack(pady=10)


search_entry.bind("<KeyRelease>", lambda event: on_search(search_entry.get()))


result_listbox.bind("<Return>", lambda event: add_to_selected_list())
result_listbox.bind("<Double-Button-1>", lambda event: add_to_selected_list())

remove_button = tk.Button(root, text="Remove Selected", command=remove_selected_item)
remove_button.pack()

output_button = tk.Button(root, text="Generate Schedule", command=out_put_list)
output_button.pack()

text_widget = tk.Text(root, wrap=tk.WORD)
text_widget.pack()


for result in all_results:
    result_listbox.insert(tk.END, result)


root.mainloop()
