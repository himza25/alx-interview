#!/usr/bin/python3
import sys
import signal

def handle_signal(sig, frame):
    """Handle SIGINT for graceful shutdown."""
    print_stats()
    sys.exit(0)

def print_stats():
    """Output total size and status code frequencies."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")

signal.signal(signal.SIGINT, handle_signal)

status_codes = {}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if (len(parts) != 8 or parts[0].count('.') != 3 or
                not parts[1].startswith('[') or not parts[6].isdigit()):
            continue
        status, size = int(parts[6]), int(parts[7])
        if status in [200, 301, 400, 401, 403, 404, 405, 500]:
            status_codes[status] = status_codes.get(status, 0) + 1
            total_size += size
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
