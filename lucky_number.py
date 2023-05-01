import random as rd

def get_lucky_nums():
  return rd.sample(range(1, 45+1), k=6)

if __name__ == '__main__':
  print(get_lucky_nums())


