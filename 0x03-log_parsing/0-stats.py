#!/usr/bin/python3
import sys
import signal


def signal_handler(sig, frame):
    """Handle SIGINT to print statistics and exit."""
    print_statistics()
    sys.exit(0)


def print_statistics():
    """Print accumulated file size and status code counts."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


signal.signal(signal.SIGINT, signal_handler)

status_codes = {}  # Dictionary to store status code counts
total_size = 0     # Total size of processed files
line_count = 0     # Count of processed lines

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.strip().split()
        if (len(parts) < 2 or parts[0].count('.') != 3 or
                not parts[1].startswith('[')):
            continue  # Skip lines not matching the format

        # Parse components ensuring the line is properly formatted
        ip, datetime_info, method, url, protocol, status, size = parts
        status, size = int(status), int(size)

        # Update metrics if status is valid
        if status in [200, 301, 400, 401, 403, 404, 405, 500]:
            status_codes[status] = status_codes.get(status, 0) + 1
            total_size += size

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()  # Print stats on keyboard interrupt before exiting
    sys.exit(0)
