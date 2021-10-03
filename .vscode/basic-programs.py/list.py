motto = [2, 14, 28, 41, 56]
motto[2] = 36
print(motto)

x = 'do what excites!'
print(len(x))

#using list as append
numlist = list()
while True :
  inp = input('Enter a number: ')
  if inp == 'done' : break
  value = float(inp)
  numlist.append(value)
average = sum(numlist) / len(numlist)
print(average)




