import pandas as pd

df = pd.read_excel(r'C:\Users\Joshua Stoner\Desktop\Project for CS Club\Book.xlsx')
def get_days(code):
    column_name4 = 'Code'  # Replace with the name of your column
    df[column_name4].fillna('', inplace=True)
    result4 = df[df[column_name4].str.contains(code)]
    matching_row_numbers4 = result4.index.tolist()
    Day_for_course = []
    for i in range(len(matching_row_numbers4)):
        cell4 = df.at[matching_row_numbers4[i], 'Day']  # Note that Excel uses 1-based indexing for rows, 0-based for columns
        if not pd.isna(cell4):
            
            Day_for_course.append(cell4)
    return Day_for_course

def get_time_slots(code):
    column_name = 'Code'  # Replace with the name of your column
    df[column_name].fillna('', inplace=True)
    result = df[df[column_name].str.contains(code)]
    matching_row_numbers = result.index.tolist()
    time_list_for_course = []
    for i in range(len(matching_row_numbers)):
        cell = df.at[matching_row_numbers[i], 'Time']  # Note that Excel uses 1-based indexing for rows, 0-based for columns
        if not pd.isna(cell):
            
            time_list_for_course.append(cell)
    return time_list_for_course
def get_credit_amount(code):
    column_name2 = 'Code'  # Replace with the name of your column
    df[column_name2].fillna('', inplace=True)
    result3 = df[df[column_name2].str.contains(code)]
    matching_row_numbers1 = result3.index.tolist()
    credit = []
    for i in range(len(matching_row_numbers1)):
        cell1 = df.at[matching_row_numbers1[i], 'Credits']  # Note that Excel uses 1-based indexing for rows, 0-based for columns
        if not pd.isna(cell1):
            if cell1 not in credit:
                credit.append(cell1)
    return credit[0]
def time_string_to_minutes(time_str):
    # Split the time string into start and end times
    start_time, end_time = time_str.split('-')

    # Function to convert HH:MM[am/pm] to minutes since midnight
    def time_to_minutes(time):
        hh, mm, ampm = time[:2], time[-4:-2], time[-2:]

        hh = int(hh)
        mm = int(mm)
        if ampm == 'pm' and hh != 12:
            hh += 12
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
    days1 = dts1[0]
    time1 = dts1[1]
    days2 = dts2[0]
    time2 = dts2[1]
    if have_common_letter(days1, days2):
        if have_common_time(time1, time2):
            return True
        else:
            return False
    else:
        return False
def have_common_time(time1, time2):
    return max(time1) >= min(time2) and max(time1) >= min(time2)



def have_common_letter(string1, string2):
    # Create sets of characters for both strings
    set1 = set(string1)
    set2 = set(string2)
    
    # Use the any function to check for common elements
    return any(char in set1 for char in set2)

class Course:
    def __init__(self, code):
        # Instance attributes (unique to each instance)
        self.code = code
        self.time_slots = get_time_slots(code)
        #self.time_slots_mins = time_string_to_minutes(self.time_slots)
        self.credits = get_credit_amount(code)
        self.days = get_days(code)

#course1 = Course('EGR192')
#print(course1.time_slots)
#print(course1.credits)
#print(course1.days)
instances = []
while True:
    name = input("Enter a course: ").upper()
    
    # Create an instance of MyClass
    instance = Course(name)
    
    # Add the instance to the list
    instances.append(instance)
    
    another = input("Do you want to add another course? (yes/no): ")
    if another.lower() != 'yes':
        break
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
    print(list(combo))
    result = has_shared_property(list(combo), conflict)
    if result==False:
        x=0
        print('nope')
    else:
        print("Here is a Schudule that works:" f'{combo}')
        break




# Example usage


# Check if any two items in the list are equal


