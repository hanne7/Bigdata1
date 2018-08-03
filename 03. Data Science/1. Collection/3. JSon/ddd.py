list = [{'1':1},
        {'1':0},
        {'1':2},
        {'1':1}
        ]

i=0
while i < len(list):
    if list[i]['1'] == 1:
        del list[i]
    i += 1


print(list)