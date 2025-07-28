import math

a1 = 105
a2 = 145
d1 = 100

x = int(input("enter x: "))
y = int(input("enter y: "))
z = int(input("enter z: "))
z1 = z - d1

th1 = math.atan2(y, x)

th3 = math.acos((x**2 + z1**2 - (a1**2 + a2**2)) / (2*a1*a2))

gamma = math.atan2(z1, x)
beta = math.atan((a2*math.degrees(math.sin(th3))) / (a1 + (a2*math.degrees(math.cos(th3)))))

th2 = gamma + beta

print("gamma: ", math.degrees(gamma))
print("beta: ", math.degrees(beta))

print(math.degrees(th1), "\n", math.degrees(th2), "\n", math.degrees(th3), "\n")
