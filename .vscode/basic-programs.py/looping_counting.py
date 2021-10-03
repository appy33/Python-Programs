word = 'banana'
count = 0
for letter in word : 
  if letter == 'a' :
    count = count + 1 
print(count)

fhand = open('info.txt')
x = 0
for line in fhand:
       x = x + 1
print(x)

phand = open('info.txt')
inp = phand.read()