#!/usr/bin/env python3

import re
import csv
import sys
from datetime import datetime

# Check if the input file is provided
if len(sys.argv) != 2:
    print("Usage: ./convert.py <input_log_file>")
    sys.exit(1)

# Get the input file
log_file = sys.argv[1]
csv_file = f"{log_file}_converted.csv"

# Regular expression to match the log lines
log_pattern = re.compile(
    r'(?P<date>\d{2}-\w{3}-\d{4} \d{2}:\d{2}:\d{2}\.\d{3}) queries: info: client [^ ]+ (?P<clientip>[^#]+)#\d+ \((?P<query>[^\)]+)\): query: \S+ IN (?P<query_type>[A-Z]+) .*'
)

try:
    # Open the log file and the CSV file
    with open(log_file, 'r') as log, open(csv_file, 'w', newline='') as csvfile:
        # Define the CSV writer
        csv_writer = csv.writer(csvfile)
        # Write the header
        csv_writer.writerow(["date", "clientip", "query type", "query"])

        # Process each line in the log file
        for line in log:
            match = log_pattern.match(line)
            if match:
                date_str = match.group('date')
                clientip = match.group('clientip')
                query_type = match.group('query_type')
                query = match.group('query')

                # Convert the date to the required format
                date = datetime.strptime(date_str, '%d-%b-%Y %H:%M:%S.%f')
                date_iso = date.isoformat(sep=' ', timespec='seconds')

                # Write the row to the CSV file
                csv_writer.writerow([date_iso, clientip, query_type, query])
            elif line.strip():  # Print non-matching lines except blank lines
                print(f"Line didn't match: {line.strip()}")

    print(f"Log file '{log_file}' has been converted to CSV format and saved as '{csv_file}'.")
except FileNotFoundError:
    print(f"Error: The file '{log_file}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
