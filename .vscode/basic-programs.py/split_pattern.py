#double split pattern
line = 'From stephen.marquard@uct.ac.za Sat Jan4 9:14:16 2008'
words = line.split()   
email = words[1]             #>>stephen.marquard@uct.ac.za
pieces = email.split('@')    #>>['stephen.marquard', 'uct.ac.za']
print(pieces[1])             #>> #>> 'uct.ac.za'

# using list and strings to split the line of code
line = 'A lot of     spaces'
etc = line.split()
print(etc)
#print(len(etc))
#print(len[2])

#rather use .startswith() function : line.startswith("From:") : continue

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(len(c))

t = [9, 41, 12, 3, 74, 15]
print(t[2:4])