def squareRootBi (x, epsilon):
    #assumes x>= 0 and epsilone > 0
    #return y s.t. y*y is within epsilone of x
 assert x >= 0, 'x must be non-negative, not'  + str(x)
 assert epsilon > 0, 'epsilone must be positive, not'  + str (epsilon)
 low = 0
 high = max (x , 1.0)
 guess = (low + high) / 2.0
 ctr = 1
 while abs (guess ** 2 - x) > epsilon and ctr <= 100:
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (low + high)/ 2.0
    ctr += 1
 assert ctr <= 100, 'itteration count exceeded'
 print ('Bi method. Num. itteration: ', ctr, 'estimate: ', guess) 
 return guess


