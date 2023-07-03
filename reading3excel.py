"""
Make sure to replace "path/to/input/folder" with the actual path to the folder containing the Excel files. 
Also, update the sheet_names list with the sheet names you want to read from each Excel file.

The script will iterate through the sheet_names list and attempt to read the corresponding sheet from each Excel file.
It will store the resulting data frames in the data_frames list. If any file is not found or encounters an error while reading,
an appropriate error message will be displayed. Finally, it will print the data frames one by one along with their corresponding sheet names.
"""

import os
import pandas as pd

def read_excel_files(folder_path):
    # Create empty DataFrames for each sheet
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    df3 = pd.DataFrame()

    # Get the list of files in the folder
    files = os.listdir(folder_path)

    # Iterate through each file
    for file in files:
        if file.endswith('.xlsx') or file.endswith('.xls'):  # Consider only Excel files
            file_path = os.path.join(folder_path, file)

            # Read the Excel file
            xl = pd.ExcelFile(file_path)

            # Iterate through each sheet in the file
            for sheet_name in xl.sheet_names:
                # Read the sheet into a DataFrame
                sheet_data = pd.read_excel(file_path, sheet_name=sheet_name)

                # Store the sheet data in the appropriate DataFrame based on the sheet name
                if sheet_name == 'Sheet1':
                    df1 = df1.append(sheet_data)
                elif sheet_name == 'Sheet2':
                    df2 = df2.append(sheet_data)
                elif sheet_name == 'Sheet3':
                    df3 = df3.append(sheet_data)

    return df1, df2, df3

# Provide the folder path where the Excel files are located
folder_path = 'path/to/source/folder'

# Call the function to read the Excel files and store the data in DataFrames
df1, df2, df3 = read_excel_files(folder_path)

# You can now use df1, df2, and df3 for further processing or analysis




++++++++++++++++++++++++++



# version0 for the sheet names
import pandas as pd

def read_excel_files(input_folder_path, sheet_names):
    data_frames = []
    
    for sheet_name in sheet_names:
        file_path = f"{input_folder_path}/{sheet_name}.xlsx"
        
        try:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            data_frames.append(df)
        except FileNotFoundError:
            print(f"Excel file '{file_path}' not found.")
        except:
            print(f"An error occurred while reading '{file_path}'.")
    
    return data_frames

# Specify the input folder path and sheet names
input_folder_path = "path/to/input/folder"
sheet_names = ["Sheet1", "Sheet2", "Sheet3"]

# Read the Excel files
data_frames = read_excel_files(input_folder_path, sheet_names)

# Print the data frames
for i, df in enumerate(data_frames):
    print(f"Data Frame {i+1} - Sheet Name: {sheet_names[i]}")
    print(df)
    print()
