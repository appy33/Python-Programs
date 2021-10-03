fname = input("Enter file: ")
if len(fname) < 1 : fname = 'romeo.txt'
handle = open(fname)

dic = dict()
for line in handle : 
    line = line.rstrip()
    words = line.split()
    for w in words : 
        #idiom: retrieve/create/update counter
        dic[w] = dic.get(w, 0) + 1

#now we want to find the most common word 
largest = -1 
theword = None
for k, v in dic.items() :
    if v > largest : 
        largest = v
        theword = k 
print(theword, largest)
