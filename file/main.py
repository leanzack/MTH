import pandas as pd
import pyreadstat
import matplotlib.pyplot as plt  # Importing matplotlib

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
df['AverageGrade'] = df['AverageGrade'].astype(int)
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

#df = df.dropna(subset=['Program'])

# Print the unique values of Gender to ensure it's correctly mapped
#print("Unique Gender Values:")
#print(df['Program'].unique())

# Create a histogram (bar chart) for Gender
#plt.figure(figsize=(8, 6))
#gender_counts = df['Program'].value_counts()  # Count occurrences of each gender
#gender_counts.plot(kind='bar', color=['lightblue', 'salmon'])

# Add titles and labels
#plt.title('Distribution of Gender')
#plt.xlabel('Program')
#plt.ylabel('Count')
#plt.xticks(rotation=0)  # Keep the x labels horizontal
#plt.grid(axis='y', linestyle='--')
#plt.tight_layout()
#plt.show()

#df['AverageGrade'] = pd.to_numeric(df['AverageGrade'], errors='coerce')

# Check for any missing values in averagegrade and drop if necessary
#df = df.dropna(subset=['AverageGrade'])

# Sort the DataFrame by average grade for better visualization
#df_sorted = df.sort_values(by='AverageGrade')

# Plot the area graph for average grades
#plt.figure(figsize=(12, 6))
#plt.fill_between(df_sorted.index, df_sorted['AverageGrade'], color="skyblue", alpha=0.4)
#plt.plot(df_sorted['AverageGrade'], color="Slateblue", alpha=0.6, linewidth=2)

# Add titles and labels
#plt.title('Area Graph of Average Grades')
#plt.xlabel('Index of Students')
#plt.ylabel('Average Grade')
#plt.grid(axis='y', linestyle='--')
#plt.tight_layout()
#plt.show()


# Create the line graph
#plt.figure(figsize=(10, 5))  # Set the figure size
#plt.plot(df['Program'], df['Question03'], marker='o', linestyle='-', label='Question 03')  # Use Program vs Question 03
#plt.title('Program vs Question 03')  # Set title
#plt.xlabel('Program')  # Set x-axis label
#plt.ylabel('Question 03')  # Set y-axis label
#plt.xticks(rotation=45)  # Rotate x-axis labels if needed
#plt.grid(True)  # Add a grid for easier reading
#plt.legend()  # Show the legend
#plt.tight_layout()  # Adjust layout to prevent clipping
#plt.show()  # Display the plot

#summary = df.groupby(['Program', 'Question03']).size().unstack(fill_value=0)
#print(summary)
# Create a bar graph for the summary data
#summary.plot(kind='bar', figsize=(10, 6))
# Add titles and labels
#plt.title('Distribution of Question 03 Responses by Program')
#plt.xlabel('Program')
#plt.ylabel('Count of Responses')
#plt.xticks(rotation=0)  # Rotate x-axis labels if needed
#plt.legend(title='Question 03')  # Legend for the different response categories
# Display the plot
#plt.tight_layout()  # Adjust layout for readability
#plt.show()


#computer_science_data = [5, 2, 2, 3, 6]  # Agree, Disagree, Neutral, Strongly Agree, Strongly Disagree
#it_data = [0, 1, 3, 0, 8]  # Agree, Disagree, Neutral, Strongly Agree, Strongly Disagree
# Define labels for each slice
#labels = ['Agree', 'Disagree', 'Neutral', 'Strongly Agree', 'Strongly Disagree']
# Colors for each category
#colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99', '#c2c2f0']
### Step 2: Create Pie Charts
# Create a subplot with 1 row and 2 columns for side-by-side comparison
#fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
# Plot Computer Science data
#ax1.pie(computer_science_data, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
#ax1.set_title('Question03 Responses - Computer Science')
# Plot IT data
#ax2.pie(it_data, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
#ax2.set_title('Question03 Responses - IT')
# Display the pie charts
#plt.tight_layout()
#plt.show()


# Filter for specific programs: "IT" and "Computer Science"
# programs = ['IT']
# for program in programs:
#     filtered_df = df[df['Program'] == program]

#     # Create summary data for Question01, Question02, and Question03 grouped by Program
#     question1_summary = filtered_df.groupby('Question01').size()
#     question2_summary = filtered_df.groupby('Question02').size()
#     question3_summary = filtered_df.groupby('Question03').size()

#     # Combine the summaries into a single DataFrame for plotting
#     combined_summary = pd.DataFrame({
#         'Question 1': question1_summary,
#         'Question 2': question2_summary,
#         'Question 3': question3_summary
#     }).fillna(0)

#     # Print the summary DataFrame for the current program
#     print(f"\nCombined Summary for {program}:")
#     print(combined_summary)

#     # Check if the combined summary has data to plot
#     if not combined_summary.empty:
#         # Plot the clustered bar graph for the current program
#         ax = combined_summary.plot(kind='bar', figsize=(8, 6))
#         plt.title(f'Responses for Questions 1, 2, and 3 - {program}')
#         plt.xlabel('Responses')
#         plt.ylabel('Count of Responses')
#         plt.xticks(rotation=45)
#         plt.legend(title='Questions')

#         # Label each bar with the count
#         for p in ax.patches:
#             ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()),
#                         ha='center', va='bottom', fontsize=10)

#         plt.tight_layout()
#         plt.show()


