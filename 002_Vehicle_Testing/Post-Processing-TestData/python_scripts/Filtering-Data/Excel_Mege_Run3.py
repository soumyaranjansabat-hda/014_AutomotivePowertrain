# -*- coding: utf-8 -*-
"""
Created on Sun May 19 17:16:18 2024

@author: HP
"""

from zipfile import ZipFile
import os
import pandas as pd

# Path to the ZIP file and extraction directory
zip_path = r'E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\test_data\Run3\Data_Export\BattBrickVoltageMaxNum332.zip'
extract_folder = r'E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\test_data\Run3\Extract'

# Extract the ZIP file
os.makedirs(extract_folder, exist_ok=True)
with ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

# List the extracted files
extracted_files = os.listdir(extract_folder)

# Load a sample Excel file to inspect the data
sample_file_path = os.path.join(extract_folder, 'BattBrickVoltageMaxNum332.xlsx')
sample_data = pd.read_excel(sample_file_path)

# Drop the first row which contains units
data_dropped_units = sample_data.drop(0)

# Identify the first non-null occurrence in each of the columns similar to 'BattBrickVoltageMaxNum332'
segregation_indices = {}
for column in sample_data.columns:
    if "BattBrickVoltageMaxNum332" in column:
        first_non_null_index = data_dropped_units[column].first_valid_index()
        segregation_indices[column] = data_dropped_units.loc[first_non_null_index, 'x'] if first_non_null_index else None

# Define a function to process each file
def process_file(file_path, cutoff_time=1255):
    data = pd.read_excel(file_path)
    data = data.drop(0)
    data['x'] = pd.to_numeric(data['x'], errors='coerce')
    filtered_data = data[data['x'] <= cutoff_time]
    columns_to_keep = [col for col in filtered_data.columns if not ('.' in col)]
    return filtered_data[columns_to_keep]

# Process each file
excel_files = [os.path.join(extract_folder, f) for f in extracted_files]
processed_data_frames = [process_file(file) for file in excel_files]

# Concatenate all the DataFrames
merged_data = pd.concat(processed_data_frames, axis=1)
merged_data = merged_data.loc[:,~merged_data.columns.duplicated()]

# Save the merged DataFrame to an Excel file
merged_excel_path = r'E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\test_data\Run3\Extract\001_Merged.xlsx'
merged_data.to_excel(merged_excel_path, index=False)
