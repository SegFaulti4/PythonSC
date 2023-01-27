import base64

ins = input().strip()
inv = base64.b85decode(ins)

header = []
body_idx = 0
for i, int_b in enumerate(inv):
    int_b = int_b - 256 if int_b & 0x80 else int_b
    if int_b == 0:
        body_idx = i + 1
        break
    header.append(int_b)


chunk_size = sum(map(abs, header))
body = inv[body_idx:]
chunk_count = len(body) // chunk_size

res = 0
for i in range(chunk_count):
    chunk = body[i * chunk_size:][:chunk_size]
    i_h = 0
    for h in header:
        f = int.from_bytes(chunk[i_h:][:abs(h)], byteorder="big", signed=h < 0)
        res += f
        i_h += abs(h)

print(res)
