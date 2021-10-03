data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1:sppos]
print(host)


text = 'X-DSPAM-Confidence:    0.8475;'
num = text.find(' ')
space = text.find(';',num)
output = text[num+4 : space]
print(output)