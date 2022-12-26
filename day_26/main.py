import pandas as pd


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 78, 98]
}

student_df = pd.DataFrame(student_dict)

for index, row in student_df.iterrows():
    print(index, row)