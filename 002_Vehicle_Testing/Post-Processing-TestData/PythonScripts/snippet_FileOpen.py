# -*- coding: utf-8 -*-
"""
Created on Sun May 12 18:33:19 2024

@author: HP
"""

from openpyxl import load_workbook

try:
    workbook_path = 'E:/HDA_Lectures/001_Repository/014_AutomotivePowertrain/002_Vehicle_Testing/Post-Processing-TestData/PythonScripts/CAN-Frames.xlsx'
    book = load_workbook(workbook_path)
    print("Workbook loaded successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
