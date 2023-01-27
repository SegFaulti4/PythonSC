import tarfile
import io
import sys


s = sys.stdin.read().replace("\n", "")
tar_file = tarfile.open(
    fileobj=io.BytesIO(
        bytearray([int(s[i:i + 2], 16) for i in range(0, len(s), 2)])))


count = 0
size = 0
for obj in tar_file:
    if obj.isfile():
        count += 1
        size += obj.size

print(size, count)
