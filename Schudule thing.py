import pandas as pd
import matplotlib.pyplot as plt
text = "(4S) 01/16/2024 to 05/08/2024 TH (09:15am-10:55am)"

search_word = ""
"09:15am-10:55am"
"12:30pm-01:50pm"
"02:00pm-03:20pm"
"12:25pm-01:55pm"
"09:30am-10:50am"
"11:00am-12:20pm"
"11:00am-12:15pm"




# Read the Excel file into a DataFrame
df = pd.read_excel(r'C:\Users\Joshua Stoner\Desktop\Project for CS Club\Book.xlsx')
my_list = []
print(df.columns)
num_rows = len(df)
for i in range(num_rows):

    cell = df.at[i, 'Time']  # Note that Excel uses 1-based indexing for rows, 0-based for columns
    if not pd.isna(cell):
        if cell not in my_list:
            my_list.append(cell)

print(my_list)
time_dict = {time: 0 for time in my_list}

# Now, time_dict is a dictionary with each time as a key and an initial value of 0
'''print(time_dict)
for i in range(num_rows):

    cell = df.at[i, 'Time']  # Note that Excel uses 1-based indexing for rows, 0-based for columns
    if not pd.isna(cell):
        if cell in time_dict:
            time_dict[cell] += 1
print(time_dict)'''
'''sorted_data = dict(sorted(time_dict.items(), key=lambda item: item[1], reverse=True))
categories = sorted_data.keys()
counts = sorted_data.values()

# Create a bar chart
 # Optional: Set the figure size
plt.bar(categories, counts)

# Adding labels and title
plt.xlabel('Class Time')
plt.ylabel('Counts')
plt.title('Class Time Counts')

# Show the bar chart
plt.xticks(rotation=90)  # Optional: Rotate x-axis labels for better readability
plt.show()'''
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

# Test the function with your time string
time_str = "11:25am-12:01pm"
minute_equivalent = time_string_to_minutes(time_str)
print(minute_equivalent)  # Output: '745-835'

print("ee")
minute_equivalents = [time_string_to_minutes(time_str) for time_str in my_list]

# Print the results
for minute_equivalent in minute_equivalents:
    print(minute_equivalent)
class_to_parse= input("Input Course Code:")
column_name = 'Course Catalog Number'  # Replace with the name of your column
df[column_name].fillna('', inplace=True)

# Search for rows that contain "AC 101" in the specified column
  # Replace with the class you want to search
result = df[df[column_name].str.contains(class_to_parse)]

# Display the matching rows
print(result)
matching_row_numbers = result.index.tolist()

# Display the matching rows and their row numbers

# Display just the row numbers
print(matching_row_numbers)
time_list_for_course = []
for i in range(len(matching_row_numbers)):
    cell = df.at[matching_row_numbers[i], 'Time']  # Note that Excel uses 1-based indexing for rows, 0-based for columns
    if not pd.isna(cell):
        if cell not in time_list_for_course:
            time_list_for_course.append(cell)
            print(cell)
print(time_list_for_course)