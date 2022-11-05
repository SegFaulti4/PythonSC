objs = eval(input().strip())

conveyor = []
for obj in objs:
    if type(obj) is tuple:
        conveyor += list(obj)
    else:
        if obj > len(conveyor):
            break
        print(tuple(conveyor[:obj]))
        conveyor = conveyor[obj:]
