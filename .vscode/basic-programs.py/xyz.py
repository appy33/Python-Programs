hrs = input("Enter hours:")
rate = input("Enter rate:")
h = float(hrs)
r = float(rate)
if h > 40 :
  r1 = r * h
  h1 = (h - 40) * (r * 0.5)
  pay = r1 + h1
else :
  pay = h * r
print("Pay:", pay)