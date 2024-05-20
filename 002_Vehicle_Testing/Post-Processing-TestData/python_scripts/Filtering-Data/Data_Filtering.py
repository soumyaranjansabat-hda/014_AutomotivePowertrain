# -*- coding: utf-8 -*-
"""
Created on Sat May 17 20:40:52 2024

@author: HP
"""

import pandas as pd

# Paths to the Excel files
metadata_file_path = r'E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\helper_data\Signals_Filtered_ForAnalysis.xlsx'
# run1_file_path = r'E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\test_data\Run1\Run1_CleanData.xlsx'
run2_file_path = r'E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\test_data\Run3\Run3_ExportData.xlsx'
# run3_file_path = ''

# Function to filter data based on parameters
def filter_data(file_path, params_list, output_path):
    # Load data
    data = pd.read_excel(file_path)
    
    # Filter data to keep only required columns
    filtered_data = data[data.columns.intersection(params_list)]
    
    # Save the filtered data to a new Excel file
    filtered_data.to_excel(output_path, index=False)

# Extracting parameters from the 'Updated' sheet of the metadata file
params_data = pd.read_excel(metadata_file_path, sheet_name='Updated')
params_list = params_data['Parameter'].tolist()

# File paths for output
output_paths = {
    # run1_file_path: r'E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\test_data\Run1\Run1_FilterData.xlsx'
    run2_file_path: r'E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\test_data\Run3\Run3_FilterData.xlsx',
    # run3_file_path: ''
}

# Apply filtering to each file
for file_path, output_path in output_paths.items():
    filter_data(file_path, params_list, output_path)

print("Filtering complete and files have been saved.")
