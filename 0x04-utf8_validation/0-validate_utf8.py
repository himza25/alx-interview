#!/usr/bin/python3
"""
A module to validate if a given dataset represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): List of integers representing bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0
    mask_1_byte = 0b10000000
    mask_2_bytes = 0b11000000
    mask_3_bytes = 0b11100000
    mask_4_bytes = 0b11110000
    mask_cont_byte = 0b11000000

    for byte in data:
        if num_bytes == 0:
            if byte & mask_1_byte == 0:
                num_bytes = 0
            elif byte & mask_4_bytes == 0b11110000:
                num_bytes = 3
            elif byte & mask_3_bytes == 0b11100000:
                num_bytes = 2
            elif byte & mask_2_bytes == 0b11000000:
                num_bytes = 1
            else:
                return False
        else:
            if byte & mask_cont_byte != 0b10000000:
                return False
            num_bytes -= 1

    return num_bytes == 0
