counts = dict()
names = ['qwerty', 'uiop', 'asdf', 'ghjkl']
for name in names : 
  if name not in counts : 
    counts[name] = 1
  else : 
    counts[name] = counts[name] + 1
print(counts)

#or 

counts = dict()
names = ['qwerty', 'uiop', 'asdf', 'ghjkl']
for name in names : 
  counts[name] = counts.get(name, 0) + 1      #'get' combines if and else in one line  
print(counts)                                 # and can be used to give back a static value.