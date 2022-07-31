#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
#e.g. nr_letters = 4
for char in range(1, nr_letters + 1):
  #range going from 1 - 4
  random_char = random.choice(letters)
  password += random.choice(letters)

for char in range(1, nr_numbers + 1):
  password += random.choice(numbers)

for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)

print(password)