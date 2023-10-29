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
            if cell4 not in Day_for_course:
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
            if cell not in time_list_for_course:
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
def conflict(time1, days1, time2, days2):
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