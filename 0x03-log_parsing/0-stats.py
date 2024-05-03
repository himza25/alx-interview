#!/usr/bin/python3
"""
Parse logs from stdin, count status codes, and sum file sizes.
"""
import re
import sys

# Regular expression to validate input format
regex = (r'^(\d{1,3}\.){3}\d{1,3} - \[\S+ \S+\] '
         r'"GET /projects/260 HTTP/1\.1" [2-5]0[0,1,3,4,5] \d+$')

# Mapping of valid status codes and their counts
valid_status_codes = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}

# Total size of processed files
total_file_size = 0

def print_stats():
    """Print the total file size and status code frequencies."""
    print(f"File size: {total_file_size}")
    for code, count in sorted(valid_status_codes.items()):
        if count:
            print(f"{code}: {count}")

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        if re.match(regex, line):
            parts = line.split()
            status_code = parts[-2]
            file_size = int(parts[-1])
            if status_code in valid_status_codes:
                valid_status_codes[status_code] += 1
                total_file_size += file_size
        else:
            continue  # Explicitly skip lines that do not match the format
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
finally:
    print_stats()
