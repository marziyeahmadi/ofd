# x = 11
# y = 2
# z = 3
# print (x , y , z)
# if x<y and x<z: print ('x the least')
# elif y<z: print ('y the least')
# else: print ('z the least')

# y=0
# x=3
# itersLeft=x
# while (itersLeft>0):
#     y=y+x
#     itersLeft=itersLeft-1
# print (y)    

# #find the square root of a perfect square
# x = 16
# ans = 0
# while (ans*ans < x):
#     ans = ans + 1
# print (ans)    

# x = 1515361
# ans = 0
# if x >= 0:
#  while (ans*ans < x):
#   ans = ans + 1
#   if (ans*ans != x):
#    print (x, 'is not a perfect square')
#   else: print (ans)
# else: print (x, 'is a negative number')

# x = 10
# for i in range (1,x):
#     if x % i == 0:
#         print ('divisor', i)
#     i = i + 1    

# test = (1,2,3,4,5)
# print (test)
# print (test [0])

x = 100
divisors = ()
for i in range (1,x):
    if x%i == 0:
       divisors = divisors + (i,)

