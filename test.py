import random

ROWS = 500
COLS = 500
QUAL = 250

def header(file):
    file.write("P3\n#test image\n")
    file.write("{0} {1}\n{2}\n".format(ROWS, COLS, QUAL))

def body(file):
    for row in range(ROWS):
        for col in range(COLS):
            y = row
            if (y >= ROWS/2):
                y = ROWS - row
            x = col
            if (x >= COLS/2):
                x = COLS - col

            r = y
            b = x
            g = 250 % (abs(x - y)+1)

            file.write("{0} {1} {2}    ".format(r,g,b))
        file.write("\n")

f = open("test.ppm", "w")
header(f)
body(f)
f.close()
