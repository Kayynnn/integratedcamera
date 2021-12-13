import zlib

with open("4.png", "rb") as in_file:
    compressed = zlib.compress(in_file.read(), 9)

with open("4-2.gz", "wb") as out_file:
    out_file.write(compressed)
