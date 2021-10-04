"""
	Various experiments with PPU.

"""

from PPU import *


def TestCounterStage():
	print ("TestCounterStage:")
	bit0 = CounterStage()

	res = bit0.sim(0, 0, 0, 1)
	print ("PCLK=0: out, carry_out", res[0], res[1])
	res = bit0.sim(0, 1, 0, 1)
	print ("PCLK=1: out, carry_out", res[0], res[1])

	res = bit0.sim(1, 0, 0, 1)
	print ("PCLK=0: out, carry_out", res[0], res[1])
	res = bit0.sim(1, 1, 0, 1)
	print ("PCLK=1: out, carry_out", res[0], res[1])

	print ("After reset:")
	print (" ")

	# Run 4 pixels (in PPU terms)

	carry = 1
	CLR = 0
	RES = 0

	for i in range(2):
		print("PCLK Cycle:", i)
		PCLK = 0
		res = bit0.sim(carry, PCLK, CLR, RES)
		print ("PCLK=0: out, carry_out", res[0], res[1])
		PCLK = 1
		res = bit0.sim(carry, PCLK, CLR, RES)
		print ("PCLK=1: out, carry_out", res[0], res[1])
	print (" ")


def TestCounter():
	print ("TestCounter:")
	cnt = HVCounter(2)

	carry = 1 			# Input carry for the very first bit
	CLR = 0
	RES = 0	

	for i in range(4):
		print("PCLK Cycle:", i)
		PCLK = 0
		cnt.sim (carry, PCLK, CLR, RES)
		PCLK = 1
		cnt.sim (carry, PCLK, CLR, RES)
		cnt.dump()
		print(" ")


def TestHDecoder():
	print ("TestHDecoder:")
	pla = HDecoder(True) 		# True: NTSC, False: PAL

	# Simulate one full line (HCounter = 0-340) and print all active PLA outputs for each line.
	for i in range(341):
		outs = pla.sim(i, 0, 0)
		print (i, ": ", end='')
		for n in range(len(outs)):
			if outs[n] != 0:
				print (f"{n}, ", end='')
		print (" ")


if __name__ == '__main__':
	TestCounterStage()
	TestCounter()
	TestHDecoder()
