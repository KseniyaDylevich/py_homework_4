import random

k =5 # степень многочлена

def polynomial_creation (k):
  polynomial =''
  for i in range (k, -1, -1):
      n = random.randrange(0, 100)
      if n==0:
        continue
      if i > 1:
        test = lambda n: f'{n}*x**{i}' if (n>1) else f'x**{i}'
        polynomial+=test(n)
      if i == 1:
        test = lambda n: f'{n}*x' if (n > 1) else 'x'
        polynomial+=test(n)
      if i == 0:
        polynomial+=(f'{n}')
      if i > 0:
        polynomial+=' + '
  if polynomial[len(polynomial)-1:len(polynomial)-2:-1]==' ':
      polynomial=polynomial[:len(polynomial)-3:]
  return (polynomial)

#print(polynomial_creation (k))


with open('polynomial.txt', 'w+') as file:
  file.write(polynomial_creation (k))

with open('polynomial.txt', 'r') as file:
  print(file.read())