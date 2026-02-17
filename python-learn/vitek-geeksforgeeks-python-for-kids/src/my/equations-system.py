#!/usr/bin/env python3
from samba.dcerpc.spoolss import kLogJobPrinted

num_unknowns = 2

def parse_equation(line_str):
    out = [ float(s) for s in line_str.split() ]
    if len(out) != num_unknowns + 1:
        raise ValueError(f"Expected three numbers, got {len(out)}")
    return out

first_str = input("Enter first equation coefficients: ")
first = parse_equation(first_str)
second_str = input("Enter second equation coefficients: ")
second = parse_equation(second_str)

print(first)
print(second)



print(f"{first - second}")
