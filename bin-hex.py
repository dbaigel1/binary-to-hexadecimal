#A program to convert from binary to hexadecimal demonstrating the actual algorithm, 
#not just using hex()
import sys
import math

#input the binary number
correct = False
inputBinary = ""
while not correct:
	inputBinary = input("Enter a number in binary \n")
	for value in inputBinary:
		if value == str(1) or value == str(0):
			continue
		else:
			inputBinary = input("Enter some real binary please \n")
	correct = True

counter = 0
currentValue = ""
totalValue = ""

while len(inputBinary) % 4 != 0:
	inputBinary = "0" + inputBinary

for bit in inputBinary:
	if counter > 3:
		counter = 0
		totalValue += str(currentValue)
		currentValue = ""
	if counter == 0:
		currentValue = int(bit) * 8
	elif counter == 1:
		currentValue += int(bit) * 4
	elif counter == 2:
		currentValue += int(bit) * 2
	else:
		currentValue += int(bit)
		if currentValue <= 9:
			totalValue += str(currentValue)
		elif currentValue == 10:
			totalValue += "A"
		elif currentValue == 11:
			totalValue += "B"
		elif currentValue == 12:
			totalValue += "C"
		elif currentValue == 13:
			totalValue += "D"
		elif currentValue == 14:
			totalValue += "E"
		elif currentValue == 15:
			totalValue += "F"
	counter += 1

print(totalValue)
