#!/usr/bin/env python3.8
from pprint import pprint
import csv

file = open("./data.txt", "r")
data = []
items = []
for line in file.readlines():
    if line == "-":
        items = []
    else:
        l = line.replace("(@MATRIX 21 1 ", "").replace(")", "").replace(".", ",").split()
        data.append(l)
file.close()
pprint(data)

with open("data.csv", "w", encoding="UTF-8") as f:
    writer = csv.writer(f)
    for line in data:
        writer.writerow(line)

# prepare_string = p_str.replace("(@MATRIX 21 1 ", "").replace(")", "").replace(".", ",")
# print("---RESULT---")
# print(prepare_string)
