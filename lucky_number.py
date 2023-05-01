import random as rd

counter = 6
lotto = []

for i in range(6):
  selected_number = rd.randint(1, 45+1)
  lotto.append(selected_number)

print(lotto)

result = rd.sample(range(1, 45+1), k=6)
print(result)


