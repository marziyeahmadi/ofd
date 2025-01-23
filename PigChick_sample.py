#20 heads and 56 legs in a farmyard, how many pigs and chicks?
def solve (numLegs,numHeads):
    for numChicks in range (0, numHeads+1):
        numPigs = numHeads - numChicks
        totLegs = 4*numPigs + 2*numChicks
        if totLegs == numLegs:
           return (numPigs, numChicks)
    return (None, None)

def barnYard ():
    heads = int (input ('Enter number of heads'))
    legs = int(input ('Enter number of legs'))
    pigs , chickens = solve (legs, heads)
    if pigs == None:
      print ('there is no solution')
    else:
       print ('number of pigs', pigs)
       print ('number of chicks', chickens)