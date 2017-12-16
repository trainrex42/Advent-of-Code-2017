#!/usr/bin/env python3

def knot(data):
    lengths = []

    for c in data:
        lengths.append(ord(c))

    lengths += [17,31,73,47,23]

    nums = list(range(256))
    pos = 0
    skip = 0

    for j in range(64):
        for l in lengths:
            if l <= 255:
                work = []
                for i in range(pos,pos+l):
                    work.append(nums[i%256])
                work = work[::-1]
                for i in range(pos,pos+l):
                    nums[i%256] = work[i-pos]

                pos += (l + skip)%256
                skip += 1

    sparse = nums[:]
    dense = []

    for i in range(0,256,16):
        x = sparse[i]
        for j in range(1,16):
            x = x^sparse[i+j]

        dense.append(x)

    out = ""

    for i in dense:
        out += hex(i)[2:].zfill(2)


    return out

def h2b(h):
    b = bin(int(h,16))[2:].zfill(len(h)*4)
    return b

puzzle = "wenycdww"

disk = ""

for i in range(128):
    h = knot(puzzle + "-" + str(i))
    b = h2b(h)
    disk += b

print(disk.count("1"))
