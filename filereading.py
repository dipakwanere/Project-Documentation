import os
import pandas as pd

def read_excel_data(file_path):
    """
    Reads data from an Excel file and returns a pandas DataFrame.
    """
    df = pd.read_excel(file_path)
    return df

def read_data_from_subfolders(main_folder):
    """
    Reads data from Excel files in subfolders of a main data folder.
    Returns two pandas DataFrames.
    """
    data_frames = []

    for root, dirs, files in os.walk(main_folder):
        for file in files:
            if file.endswith(".xlsx"):
                file_path = os.path.join(root, file)
                data_frame = read_excel_data(file_path)
                data_frames.append(data_frame)

    if len(data_frames) < 2:
        raise ValueError("At least two Excel files are required.")

    return data_frames[0], data_frames[1]

# Specify the main data folder path
main_folder_path = "/path/to/main/folder"

# Call the function to read data from subfolders
try:
    df1, df2 = read_data_from_subfolders(main_folder_path)
    print("Data from Excel File 1:")
    print(df1.head())
    print("\nData from Excel File 2:")
    print(df2.head())
except ValueError as e:
    print(e)
