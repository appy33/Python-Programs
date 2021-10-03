def sumofevennos(n, limit):
  totalsum = 0
  while n < limit:
    totalsum += n
    n += 2
  return totalsum
print(sumofevennos(2,100))  

   
  