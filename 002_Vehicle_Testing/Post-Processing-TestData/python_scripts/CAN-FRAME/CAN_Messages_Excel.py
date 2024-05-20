# -*- coding: utf-8 -*-
"""
For Data Manupulation of our CAN Frames and different DBC files
Version 1
"""

import pandas as pd

# Load the workbook
workbook_path = 'E:/HDA_Lectures/001_Repository/014_AutomotivePowertrain/002_Vehicle_Testing/Post-Processing-TestData/PythonScripts/CAN-Frames.xlsx'
workbook = pd.ExcelFile(workbook_path)

# Define a function to check for partial matches and capture details
def check_partial_presence_with_details(sheet_name, reference_values):
    # Load data from the given sheet
    data = pd.read_excel(workbook, sheet_name=sheet_name)
    data['Name'] = data['Name'].astype(str)  # Ensure the column is treated as string
    
    # Initialize the results list and matches details
    results = []
    matches_details = []
    
    # Loop through each reference value and check for its partial presence
    for value in reference_values:
        # Convert the value to string and check for partial match in the data
        value_str = str(value).split('_')[0]  # Consider partial ID before any underscore
        # Get partial matches
        matches = data['Name'][data['Name'].str.contains(value_str, case=False, na=False)]
        if not matches.empty:
            results.append("Present")
            matches_details.append(", ".join(matches))  # Join all matches into a single string
        else:
            results.append("Not Present")
            matches_details.append("")  # No matches found
    
    return results, matches_details

# Load the "DataCheck" sheet for reference values
data_check = pd.read_excel(workbook, sheet_name='DataCheck')

# Initialize dictionaries to store results
msgs_results_detailed = {}
signals_results_detailed = {}

# Process each sheet and apply the matching function
for sheet_name in workbook.sheet_names:
    if sheet_name.startswith("Msgs"):
        presence, details = check_partial_presence_with_details(sheet_name, data_check['Messages-from-our-testing'])
        msgs_results_detailed[sheet_name] = {"Presence": presence, "Details": details}
    elif sheet_name.startswith("Signals"):
        presence, details = check_partial_presence_with_details(sheet_name, data_check['Signal-from-our-testing'])
        signals_results_detailed[sheet_name] = {"Presence": presence, "Details": details}

# Convert results into DataFrames for Excel output
result_df_detailed = pd.DataFrame()
signals_df_detailed = pd.DataFrame()

for sheet, data in msgs_results_detailed.items():
    result_df_detailed[sheet + " Presence"] = data['Presence']
    result_df_detailed[sheet + " Details"] = data['Details']

for sheet, data in signals_results_detailed.items():
    signals_df_detailed[sheet + " Presence"] = data['Presence']
    signals_df_detailed[sheet + " Details"] = data['Details']

# Add the reference columns from "DataCheck" sheet
result_df_detailed['Messages-from-our-testing'] = data_check['Messages-from-our-testing']
signals_df_detailed['Signals-from-our-testing'] = data_check['Signal-from-our-testing']

# Move the reference columns to the first position for clarity
cols = list(result_df_detailed.columns)
cols.insert(0, cols.pop(cols.index('Messages-from-our-testing')))
result_df_detailed = result_df_detailed.loc[:, cols]

cols = list(signals_df_detailed.columns)
cols.insert(0, cols.pop(cols.index('Signals-from-our-testing')))
signals_df_detailed = signals_df_detailed.loc[:, cols]

# Save the results to an Excel file
final_file_path = 'E:/HDA_Lectures/001_Repository/014_AutomotivePowertrain/002_Vehicle_Testing/Post-Processing-TestData/PythonScripts/CAN-Frames-Results.xlsx'
with pd.ExcelWriter(final_file_path, engine='openpyxl') as writer:
    result_df_detailed.to_excel(writer, sheet_name='Messages_Results', index=False)
    signals_df_detailed.to_excel(writer, sheet_name='Signals_Results', index=False)
