array = [0, 700, 4, 54, 103, 24, 39, 900]

num_mayores_a_100 = 0 

for i in range(len(array)):
    if array[i] > 100:
        num_mayores_a_100 += 1
    else:
        continue

print(num_mayores_a_100)
