import pandas as pd
import pyreadstat

# Load the SPSS file with the correct path
file_path = r"C:\Users\leyan\PycharmProjects\MTH\data\Student.sav"  # Change to your actual file name

# Read SPSS file into a DataFrame
df, meta = pyreadstat.read_sav(file_path)

# Convert categorical columns to integer
df['Gender'] = df['Gender'].astype(int)
df['Program'] = df['Program'].astype(int)
df['Question01'] = df['Question01'].astype(int)
df['Question02'] = df['Question02'].astype(int)
df['Question03'] = df['Question03'].astype(int)
df['YearLevel'] = df['YearLevel'].astype(int)
df['BirthDay'] = df['BirthDay'].astype(int)
df['BirthMonth'] = df['BirthMonth'].astype(int)
df['BirthYear'] = df['BirthYear'].astype(int)

# Access the value labels for categorical variables
value_labels = meta.value_labels
# Set display options to show all rows and columns
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.expand_frame_repr', False)  # Do not wrap the DataFrame

print("\nAll Value Labels:")
for key, labels in value_labels.items():
    # Create a single line string of all labels for the current key
    label_str = ', '.join([f"{k}: {v}" for k, v in labels.items()])
    print(f"Key: {key} | Labels: {label_str}")

# Display the entire DataFrame
print("\nStudent DataFrame Without Values:")
print(df)


# Renaming labels and converting keys to int
value_labels['Gender'] = {int(k): v for k, v in value_labels.pop('labels0').items()}
value_labels['Program'] = {int(k): v for k, v in value_labels.pop('labels1').items()}
value_labels['YearLevel'] = {int(k): v for k, v in value_labels.pop('labels2').items()}

# Use the same labels for Question01, Question02, and Question03
value_labels['Question01'] = {int(k): v for k, v in value_labels.pop('labels3').items()}
value_labels['Question02'] = value_labels['Question01']  # Same labels as Question01
value_labels['Question03'] = value_labels['Question01']  # Same labels as Question01

# Map numeric values to their corresponding labels
df['Gender'] = df['Gender'].map(value_labels['Gender'])
df['Program'] = df['Program'].map(value_labels['Program'])
df['YearLevel'] = df['YearLevel'].map(value_labels['YearLevel'])
df['Question01'] = df['Question01'].map(value_labels['Question01'])
df['Question02'] = df['Question02'].map(value_labels['Question02'])
df['Question03'] = df['Question03'].map(value_labels['Question03'])


# Display the updated DataFrame with labels
print("\nStudent DataFrame with Labels:")
print(df)
