import openpyxl
import csv

# Input Excel file path
input_file_path = "forParsing_task.xlsx"

# Output CSV file path
output_file_path = "parsed_data_using_standard_libraries.csv"

# Open the Excel file
try:
    workbook = openpyxl.load_workbook(input_file_path)
    sheet = workbook.active
except Exception as e:
    print(f"Error loading Excel file: {e}")
    exit(1)

# Function to parse each line and extract columns
def parse_line(line):
    if line.startswith('|'):
        columns = line.strip().replace('|',';').split(';')
        columns[6] = columns[6].replace(",","")
        columns = [column.strip() for column in columns]
        return columns[1:11]  # Select columns 2 to 11 (1-indexed)
    return None

# Extract structured data from the Excel sheet
structured_data = []
current_row = ""
for row in sheet.iter_rows(values_only=True):
    if row and isinstance(row[0], str) and row[0].startswith('|') and "--" not in row[0]:
        if current_row:
            parsed_data = parse_line(current_row)
            if parsed_data and parsed_data not in structured_data:
                structured_data.append(parsed_data)
        current_row = row[0]

# Append the last row
if current_row:
    parsed_data = parse_line(current_row)
    if parsed_data and parsed_data not in structured_data:
        structured_data.append(parsed_data)

# Write the structured data to a CSV file
try:
    with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        # Write data rows
        writer.writerows(structured_data)
except Exception as e:
    print(f"Error saving CSV file: {e}")
    exit(1)
