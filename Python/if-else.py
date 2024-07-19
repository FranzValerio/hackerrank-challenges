#!/bin/python3

import math
import os
import random
import re
import sys

def main():

	n = int(input().strip())

	try:

		if n in range(1,101):

			pass

		if n % 2 != 0:

			print("Weird")

		elif (n % 2 == 0 and n in range(2,5)):

			print("Not Weird")

		elif (n % 2 == 0 and n in range(6,21)):

			print("Weird") 

		elif (n % 2 == 0 and n > 20):

			print("Not Weird")

	except:

		print("Out of range!")

if __name__ == '__main__':

	main()


