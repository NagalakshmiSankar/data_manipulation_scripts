# data_manipulation_scripts

Overview
    This repository contains two Python scripts for parsing an Excel file and converting it into a delimited format (CSV). The first script, "Script 1," uses open-source libraries, particularly the pandas library, for data processing. The second script, "Script 2," aims to achieve better performance by utilizing only standard Python libraries, such as openpyxl and csv.

Script 1: Using Open-Source Libraries
    Purpose
        The goal of this script is to read the "forParsing_task.xls" file, clean the data, and save it in a delimited format, like CSV. This script demonstrates the use of the pandas library for efficient data manipulation.

    Script Structure
        The script is structured as follows:

            Import necessary libraries, including pandas.
            Read the "forParsing_task.xls" Excel file into a pandas DataFrame.
            Perform data cleaning and transformation as required.
            Save the cleaned data to a CSV file.
    Choice of Libraries
        We chose to use the pandas library for this script because of its efficiency in handling tabular data and ease of use. Pandas offers a wide range of data manipulation functions, making it well-suited for tasks like data cleaning and transformation. Furthermore, pandas allows us to work with Excel files seamlessly, providing a versatile solution for our data parsing needs.

Script 2: Using Standard Python Libraries
    Purpose
        The second script focuses on achieving better performance using standard Python libraries, reducing the reliance on external dependencies. It uses the openpyxl library for Excel file parsing and the built-in csv module for CSV output.

    Script Structure
        The script is structured as follows:

            Import the required standard Python libraries, such as openpyxl and csv.
            Read the "forParsing_task.xls" Excel file using openpyxl.
            Implement a custom algorithm for data cleaning and transformation.
            Save the cleaned data to a CSV file using the csv module.
    Performance Improvement
        In Script 2, we aim to improve performance by minimizing external library dependencies. This script showcases a more efficient algorithm for parsing the Excel file while maintaining a high level of control over the process.

Running the Scripts
To run these scripts, make sure you have Python installed on your system. Additionally, you may need to install the pandas library for Script 1 and the openpyxl library for Script 2. You can install these dependencies using pip:

For pandas (Script 1):
    pip install pandas

For openpyxl (Script 2):
    pip install openpyxl

To execute the scripts, run the following commands:

For Script 1:
    python data_parsing_using_pandas.py

For Script 2:
    python data_parsing_using_standard_libraries.py

These commands assume that the "forParsing_task.xls" file is present in the same directory as the scripts.

Conclusion
    These two scripts offer different approaches to parsing Excel files and converting them to CSV. Script 1 emphasizes ease of use and data manipulation capabilities through the pandas library, while Script 2 prioritizes performance by using only standard Python libraries. Choose the script that best suits your requirements based on your priorities for data parsing tasks.