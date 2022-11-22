def factorial(num):
   if num == 1:
       print(num)
       return 1
   else:
       print(num)
       return num * factorial(num-1)
factorial(2)
