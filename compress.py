import zlib

with open("4.png", "rb") as in_file:
    compressed = zlib.compress(in_file.read(), 8)

with open("MyCompressedFile.png", "wb") as out_file:
    out_file.write(compressed)