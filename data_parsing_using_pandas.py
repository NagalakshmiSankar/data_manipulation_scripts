import pandas as pd

# Input Excel file path
input_file = "forParsing_task.xlsx"

# Output CSV file path
output_file = "parsed_data_using_pandas.csv"

# Load the Excel file into a pandas DataFrame
try:
    df = pd.read_excel(input_file,header=None)
except Exception as e:
    print(f"Error loading Excel file: {e}")
    exit(1)
    
# Data Manipulation

df.dropna(inplace=True) # removes the empty rows
df.drop_duplicates(inplace=True,keep=False) # removes the duplicate rows
df = df[0].str.split("|",expand=True).iloc[:,:-1].iloc[:,1:] # used iloc for excluding the first and last empty columns that arises after splitting
columns = ["Stat","Account","No","Date","Net due dt","LC amt","DD","CCAr","PayT","Type"]
df.columns = columns
df["LC amt"] = df["LC amt"].str.replace(',','')
for index in df.index:
    df.loc[index]=df.loc[index].str.strip()

# Save the DataFrame to a CSV file
try:
    df.to_csv(output_file, index=False,sep=';')
    print(f"CSV file '{output_file}' has been created.")
except Exception as e:
    print(f"Error saving CSV file: {e}")
    exit(1)