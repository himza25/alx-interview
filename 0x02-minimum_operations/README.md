#0x02-minimum_operations
# Minimum Operations to Reach `n` 'H' Characters

## Description
This Python script calculates the minimum number of "Copy All" and "Paste" operations needed to produce exactly `n` 'H' characters from a single initial 'H'. It is designed to determine the fewest number of operations using a method that intelligently decides when to copy and paste based on the current total of 'H' characters and their factors relative to `n`.

## How It Works
The `minOperations(n)` function receives an integer `n` and calculates the necessary operations to achieve `n` 'H' characters using the most efficient method of copying and pasting.

## Requirements
- Python 3.4.3 or later
- Tested on Ubuntu 20.04 LTS

## Usage
To run the script, follow these steps in your command line:
```bash
# Give execute permission to the script
chmod +x 0-minoperations.py

# Run the script
./0-minoperations.py
