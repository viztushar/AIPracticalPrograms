def WaterJug(jug1, jug2):
    jugg1, jugg2, fill = 3, 4, 2
    print((jug1, jug2))
    if jug2 is fill:
        return
    elif jug2 is jugg2:
        WaterJug(0, jug1)
    elif jug1 != 0 and jug2 is 0:
        WaterJug(0, jug1)
    elif jug1 is fill:
        WaterJug(jug1, 0)
    elif jug1 < jugg1:
        WaterJug(jugg1, jug2)
    elif jug1 < (jugg2 - jug2):
        WaterJug(0, (jug1 + jug2))
    else:
        WaterJug(jug1 - (jugg2 - jug2), (jugg2 - jug2) + jug2)


print("JUG1 JUG2")
WaterJug(0, 0)
