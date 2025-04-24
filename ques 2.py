import pandas as pd
file_name = 'student_data.xlsx'
df = pd.read_excel(file_name)
print("Excel Data (before conversion to dictionary):")
print(df)
student_data_dict = {}
for index, row in df.iterrows():
    rollno = row['RollNo']
    name = row['Name']
    marks = {'Subject1': row['Subject1'], 'Subject2': row['Subject2'], 'Subject3': row['Subject3']}
    total = marks['Subject1'] + marks['Subject2'] + marks['Subject3']
    student_data_dict[rollno] = {
        'Name': name,
        'Marks': marks,
        'Total': total
    }
print("\nConverted Dictionary Data:")
print(student_data_dict)
