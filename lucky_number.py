import random as rd

counter = 6
lotto = []

for i in range(6):
  selected_number = rd.randint(6, 45)
  lotto.append(selected_number)

print(lotto)

