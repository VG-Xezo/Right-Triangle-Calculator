import time
import random

def calculate():
	a = input("What is the measurement of the a side")
	b = input("What is the measurement of the b side")
	c = input("What is the measurement of the c side")
	a1 = int(a)*int(a)
	b1 = int(b)*int(b)
	c1 = int(c)*int(c)
	a2 = int(a1)
	b2 = int(b1)
	c2 = int(c1)
	print("Calculating...")
	time.sleep(random.randint(1,4))
	if a2+b2 == c2:
		print("Makes a right triangle")
	else:
		print("Does not make a right triangle")
	again = input("Do you want to calculate another input")
	if again == " Yes":
		calculate()
	else:
		print("Shutting down...")
		exit()

def main():
	pW = input("What is the password to use this app?")
	if pW == " Hackz1":
		print("Starting app...")
		time.sleep(random.randint(1,3))
		calculate()
	else:
		print("Wrong password please do not steal code")
		exit()

main()