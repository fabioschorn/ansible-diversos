import os
import csv
import datetime

# Define the directory where the CSV files are stored
csv_directory = '/local/path/on/control/machine/reports/'
# Generate output file name with the current date and time
current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
output_file = f'merged_report_{current_time}.csv'

# Define the header row based on the collected information
header = [
    'Hostname',
    'IP Address',
    'Distribution',
    'Version',
    'Uptime (Days)',
    'CrowdStrike Version',
    'Splunk Version',
    'Qualys Version',
    'Qualys Repo Status',
    'Pending Updates'
]

# Initialize a list to hold all rows of data
all_rows = []

# Iterate over each file in the directory
for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        with open(os.path.join(csv_directory, filename), 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                all_rows.append(row)
        # Delete the file after processing
        os.remove(os.path.join(csv_directory, filename))

# Write the header and all rows to the output file
with open(os.path.join(csv_directory, output_file), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)  # Write the header row
    writer.writerows(all_rows)  # Write all data rows

print(f'Merged CSV report has been created: {output_file}')