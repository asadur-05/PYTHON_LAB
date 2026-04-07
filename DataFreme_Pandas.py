import pandas as pd
data1 = {
    "Name":["Asadur", "Sayan", "Munshi"],
    "Roll": [131,163, 165],
    "Marks": [50,45,55]
}
data2 = {
    "Name":["Ankur", "Rahit","Taufique" ],
    "Roll": [68, 78, 65],
    "Attendance": [6,10,20]
}

student_df = pd.DataFrame(data1)
student_df2 = pd.DataFrame(data2)
merge = pd.merge(student_df,student_df2, on=["Name","Roll"], how="outer")
print(merge)
