import pandas as pd
import sys

# Assuming the script receives a string of comma-separated values representing the data for one row
data = sys.argv[1].split(',')

# Convert the data into a DataFrame
df = pd.DataFrame([data], columns=["Hostname", "IP", "Distro", "Version", "Uptime", "CrowdStrike Version", "Splunk Version", "Qualys Version", "Qualys Repo", "Pending Updates"])

# Append data to an existing Excel file or create a new one
excel_file = 'report.xlsx'
with pd.ExcelWriter(excel_file, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
    df.to_excel(writer, sheet_name='Report', index=False, header=not writer.sheets)