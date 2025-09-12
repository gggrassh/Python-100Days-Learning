for x in range(0,21):
    for y in range(0,34):
        for z in range(0,100,3):
            if x + y + z == 100 and 5*x + 3*y + z//3 == 100:
                print(x,y,z)
