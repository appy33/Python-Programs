h = input("Enter file name: ")
f = open('words.txt')
for linex in f:
  liney = linex.rstrip()
  print(liney.upper())
