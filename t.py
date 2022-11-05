from ChudnPi import PiGen

for i, p in enumerate(PiGen()):
    if i>120:
        break
print(str(p)[1400:1470])
