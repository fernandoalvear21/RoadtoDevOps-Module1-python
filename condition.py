import variables

# if
for i in variables.edades:
    if i < 37:
        print(i, "es menor a 37")
    else:
        print(i, "es mayor o igual a 37")

# if-elif-else
for i in variables.alturas:
    if i < 1.70:
        print(i, "es menor a 1.70")
    elif i >= 1.70 and i < 1.80:
        print(i, "es mayor o igual a 1.70 y menor a 1.80")
    else:
        print(i, "es mayor o igual a 1.80")

