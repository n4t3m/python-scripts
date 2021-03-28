import requests
from random import randrange

#This script generates simple passwords using DinoPass.

num_inp = input("How many passwords would you like to generate? ")

try:
	pw_count = int(num_inp)
except:
	print("Error, please enter a number")
	exit(1)

for i in range(0, pw_count):
	r = requests.get(f"https://www.dinopass.com/password/simple?_={randrange(9999999999999999999)}")
	print(r.text)
