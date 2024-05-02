#!/usr/bin/python3
import sys
import signal


def signal_handler(sig, frame):
    """Handle SIGINT."""
    print_stats()
    sys.exit(0)


def print_stats():
    """Print file size and status counts."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")


signal.signal(signal.SIGINT, signal_handler)

status_codes = {}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.strip().split()
        if (len(parts) < 2 or parts[0].count('.') != 3 or
                not parts[1].startswith('[')):
            continue
        _, _, _, _, _, status, size = parts
        status, size = int(status), int(size)
        if status in [200, 301, 400, 401, 403, 404, 405, 500]:
            status_codes[status] = status_codes.get(status, 0) + 1
            total_size += size
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
