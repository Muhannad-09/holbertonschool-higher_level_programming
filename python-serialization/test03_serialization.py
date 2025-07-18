#!/usr/bin/env python3
from task_02_csv import convert_csv_to_json

csv_file = "data.csv"
success = convert_csv_to_json(csv_file)
if success:
    print(f"Data from {csv_file} has been converted to data.json")
else:
    print(f"Failed to convert data from {csv_file}")
