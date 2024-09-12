import subprocess
import csv
import re
import os
from datetime import datetime
import time


csv_file = 'redis_stats.csv'
TEST_DURATION = 305

stats = subprocess.run(['sh', './containers_stats.sh'], capture_output=True, text=True)
subprocess.run(['clear'])

output_lines = stats.stdout.splitlines()

csv_header = ['TIMESTAMP', 'CONTAINER ID', 'NAME', 'CPU %', 'MEM USAGE', 'MEM LIMIT', 
              'MEM %', 'NET IN', 'NET OUT', 'BLOCK I', 'BLOCK O', 'PIDS']

file_exists = os.path.isfile(csv_file)

with open(csv_file, 'a', newline='') as file:
    content_csv = csv.writer(file)

    content_csv.writerow(csv_header)
    for i in range(TEST_DURATION):
        subprocess.run(['clear'])
        print(f"Timer: {i} / {TEST_DURATION}")

        # Write the rest of the data, skipping the first line (header)
        for line in output_lines[1:]:
            # Use regex to split by 2 or more spaces
            content = re.split(r'\s{2,}', line)

            # Remove '%' from each column
            content = [col.replace('%', '') for col in content]

            # Split on '/' where applicable, to handle MEM USAGE / LIMIT
            split_content = []
            for col in content:
                # Split by '/' and extend the list to include both parts
                split_content.extend(col.split('/'))

            # Ensure the processed content has the correct number of columns (10)
            if len(split_content) == len(csv_header) - 1:  # Exclude TIMESTAMP column
                # Prepend a timestamp to the row
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                split_content.insert(0, timestamp)

                # Write the row to the CSV file
                content_csv.writerow(split_content)
        time.sleep(1)