my_list = [1, 1, 2, 10, 10, 23, 10, 123, 66, 78, 123, 0]

def find_not_repetitive(list):
  not_repetitive_list=[]
  for i in list:
      if list.count(i) == 1:
          not_repetitive_list.append(i)
  return not_repetitive_list

print (find_not_repetitive(my_list))