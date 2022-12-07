import math

t = input ('введите требуемую точность округления (в формате 0.1, 0.001, 0.0001 и т.д): ')

def accuracy (t):
  return round(math.pi, len(t)-2)

accuracy(t)