first_digit = 23//10
last_digit  = 23%10
SOD         =  first_digit+last_digit
print(SOD)
num = 12
sumofdigits = 0
while num>0:
  sumofdigits += num%10        #sod = sod + num%10
  num //=10                    #num = num + //10  # // = Integer Division
print(sumofdigits)




