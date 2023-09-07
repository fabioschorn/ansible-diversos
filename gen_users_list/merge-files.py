import os
import csv

directory = '/tmp/seu_diretorio'
output_file = 'atv_final_text_file_uniq.csv'

# Get all .txt files in directory
txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]

# Open output file for writing
with open(output_file, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write header row to output file
    writer.writerow(['IP', 'User'])

    # Loop through each .txt file
    for txt_file in txt_files:
        file_path = os.path.join(directory, txt_file)

        # Open and read the file
        with open(file_path, 'r') as f:
            content = f.read().splitlines()

        # Get the IP address and users
        ip = content[0]
        users = content[1:]

        # Write the data to the output file
        for user in users:
            writer.writerow([ip, user])

print(f'Successfully wrote data to {output_file}')