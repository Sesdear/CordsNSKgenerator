import random as ran
import os
#55.118939, 82.792001
#54.941055, 82.971902
cordDolgota1 = 55.118939
cordDolgota2 = 54.941055
cordShirota1 = 82.792001
cordShirota2 = 82.971902
f = int(input('Choose: 1-Add new cords in file; 2-Delete all cords from file ::  '))
if f == 1:
    stop = int(input("Input how many cords generated: "))
    stop_count = 1
    generated = 0
    while True:
        x = ran.uniform(cordDolgota1, cordDolgota2)
        y = ran.uniform(cordShirota1, cordShirota2)
        print(x, y)
        generated = x, y
        stop_count = stop_count + 1
        with open('coords_generated.txt', 'a') as f:
            cords_writes = f.writelines(f"{generated}\n")
        f.close()
        if stop == stop_count:
            break
elif f == 2:
    f = open("coords_generated.txt", 'w')
    f.close()
