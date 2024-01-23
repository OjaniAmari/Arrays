import numpy as np
import math
a = np.array([1,2,3])
print("Simple Array:", a)

b = np.array([[1,2,3], [4,5,6]])
print("2D Array:", b)

c = np.array([31,29,31,30,31,30,31,31,31,30,31,30,31])
print("Array:", c)

d = np.array([["Dec", "Jan", "Feb"], ["Mar", "Apr", "May"], ["Jun", "Jul", "Aug"], ["Sep", "Oct", "Nov"]])
print("Months in 2D Array:" , d[0,2],d[1,2], d[3,1] )

e = np.array([["World of Warcraft","World of Tanks", "Star wars old republic"], ["Osu", "Lethal Company", "Binding of Isaac"], ["Valorant", "Apex", "Call of Duty"], ["For Honour", "Elden Ring", "Red Dead Redemption 2"], ["Phasmophobia", "Fallout 76", "Dead by deadlight"]])
print("Game Genre 2D Array:", e)

f = np.array([[["Room1"], ["Room2"], ["Room3"]], [["Room1"], ["Room2"], ["Room3"]], [["Room1"], ["Room2"], ["Room3"]]])
print("Room Arrays:", f)

Array = np.array([[[1,2,3], [1,2,3], [1,2,3]],[[1,2,3], [1,2,3], [1,2,3]],[[1,2,3], [1,2,3], [1,2,3]]])
print("Anwser to the Questions is:", Array[0,2,2], Array[1,1,0], Array[1,2,1], Array[2,0,2])

x = np.array ([1,2,3])
y = np.array ([10,20,30])

m = np.array([4,8,16,53])
print(m[0] + m[2], m[1], m[3])
for x in m:
    print(x)

NoA = np.array([5,10,23,34,40])
NoB = np.array([3,5,7,9,12])

print(NoA * NoB)
print(NoA + NoB)
print(NoA * NoB[2])

Temp = math.array([4.6,6.5,7.5,8.9,12.8,14.9,18.1,18.3,14.3,12.7,8.9,3.5])
minimum = min(Temp)
max = max(Temp)
print(minimum))