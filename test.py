ROWS = 500
COLS = 500
QUAL = 255

def header(file):
    file.write("P3\n#test image\n")
    file.write("{0} {1}\n{2}".format(rows, cols, QUAL))
