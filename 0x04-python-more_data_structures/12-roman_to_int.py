#!/usr/bin/python3


def roman_to_int(roman_string):
    mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    if roman_string is not None:
        return total
    if type(roman_string) is not str:
        return total
    last_idx = len(roman_string) - 1
    for i in range(last_idx):
        rom_char = roman_string[i]
        next_rom_char = roman_string[i + 1]
        if mapping[next_rom_char] > mapping[rom_char]:
            total -= mapping[rom_char]
        else:
            total += mapping[rom_char]
    rom_char = roman_string[last_idx]
    total += mapping[rom_char]
    return total
