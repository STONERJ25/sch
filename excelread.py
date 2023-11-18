import pandas as pd
import sys
df = pd.read_excel(r'Book.xlsx')
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
def course_name_to_code(name):
    column_name4 = 'Course Title'  # Replace with the name of your column
    df[column_name4].fillna('', inplace=True)
    result4 = df[df[column_name4].str.contains(name)]
    matching_row_numbers4 = result4.index.tolist()
    Code_for_course = []
    for i in range(len(matching_row_numbers4)):
        cell4 = df.at[matching_row_numbers4[i], 'Code List']  # Note that Excel uses 1-based indexing for rows, 0-based for columns
        if not pd.isna(cell4):
            
            Code_for_course.append(cell4)
    return Code_for_course[0]
class Course:
    def __init__(self, code):
        # Instance attributes (unique to each instance)
        if len(code) > 6:
            self.code = course_name_to_code(code)
        else:
            self.code = code
        print(self.code)
        self.time_slots = get_time_slots(self.code)
        #self.time_slots_mins = time_string_to_minutes(self.time_slots)
        self.credits = get_credit_amount(self.code)
        self.days = get_days(self.code)

#course1 = Course('EGR192')
#print(course1.time_slots)
#print(course1.credits)
#print(course1.days)
