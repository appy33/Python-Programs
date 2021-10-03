import re
handle = open('regex_sum_1202788.txt')
numbers = re.findall(r'[0-9]*',handle)
new_list = []
for i in numbers :
    if i :
        i = int(i)
        new_list.append(i)
print(sum(new_list))