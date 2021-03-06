#!/usr/bin/env python3

with open("input.txt") as f:
    data = list(f.readline()[:-1])

garbage = False
layer = 1
score = 0
g_c = 0
for i,char in enumerate(data):
    if garbage:
        if char == ">":
            garbage = False
        elif char == "!":
            g_c -= 1
            data[i+1] = " "
        else:
            g_c += 1

    else:
        if char == "{":
            score += layer
            layer += 1
        elif char == "}":
            layer -= 1
        elif char == "<":
            garbage = True

print(g_c)
