import pandas as pd

# Specify the correct path to your Excel file
excel_file = r'C:\Users\oas1sgh\Desktop\max\Copy of Max ZHAO_Onboarding checklist_230721.xlsx'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file)

# Print the contents of the DataFrame
print(df)

# Check for missing values in df
missing_values = df.isnull().sum()
print(missing_values)
