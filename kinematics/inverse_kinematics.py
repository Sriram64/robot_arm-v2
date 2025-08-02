import math as mt

xt = float(input("enter x: "))
yt = float(input("enter y: "))
zt = float(input("enter z: ")) 
zt = zt - 105.0

l1 = 105
l2 = 75
l3 = 30

psi = 0 # orientation angle
psi_rad = mt.radians(psi)

xw = xt - (l3 * mt.cos(psi_rad))
zw = zt - (l3 * mt.sin(psi_rad))

th0 = mt.atan2(yt, xt)

def calc_IK(x, z):
	#psi = 0

	h = mt.sqrt((x**2) + (z**2))

	alpha = mt.acos((((l1**2)+(l2**2))-(h**2))/(2 * l1 * l2))
	th2 = mt.pi - alpha
	alpha_deg = mt.degrees(alpha)
	th2_deg = mt.degrees(th2)
	
	beta = mt.atan2(z, x)

	c1 = l2 * mt.sin(th2)
	c2 = l1 + (l2 * mt.cos(th2))

	gamma = mt.atan2(c1, c2)

	th1 = beta + gamma
	th1_deg = mt.degrees(th1)
	
	th3_deg = psi - (th1_deg - (th2_deg))
	
	return (th0, th1_deg, th2_deg, th3_deg)
	
x = calc_IK(xw, zw)
print(x)
