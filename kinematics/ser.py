import serial as ser
import inverse_kinematics as ik

ser_port = ser.Serial('/dev/ttyUSB0', 9600, timeout=1)  

th_0, xw, zw = ik.get_input()

th_1, th_2, th_3 = ik.calc_IK(xw, zw)
angles = f"{th_0:.4f};{th_1:.4f};{th_2:.4f};{th_3:.4f};"

ser_port.write(angles.encode())  # Send the string as bytes
ser_port.close()
