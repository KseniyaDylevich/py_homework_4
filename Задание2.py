n = 350

def simple_multipliers(chislo):
  simple_multipliers_list =[]
  for i in range (2, chislo+1):
      while chislo%i==0:
          simple_multipliers_list.append(i)
          chislo//=i
  return simple_multipliers_list

print(simple_multipliers(n))