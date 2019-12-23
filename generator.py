import random
from random import shuffle

# ask what the password will be used for
purpose = str(input('What will this password be used for? '))
# ask the user how long the password should be
length = int(input('How long should the password be? '))

# ask the user how many numbers should be in the password
numbers = int(input('How many numbers should be in the password? '))
numberst = '0123456789'
# ask the user how mant letter should be in the password
letters = int(input('How many letters should be in the password? '))
letterst = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = random.choices(numberst, k=numbers)
l = random.choices(letterst, k=letters)

passlist = n + l


total = numbers + letters

# take the length, numbers and letters to make a random password
if length < 6:
	print('Password must be at least 6 characters long!')
elif total != length:
	print('The amount of numbers and letters does not equal the length you set!')
elif total == length:
	def passToString(passlist):
		
		password = ''

		for ele in passlist:
			password += ele
		return password
	random.shuffle(passlist)
	print('Your random password is: ' + passToString(passlist))
	with open(purpose+'.txt', 'w') as wf:
		wf.write(purpose+': '+passToString(passlist)+'\n')