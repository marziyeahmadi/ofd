import math

#get base
inputOK = False 
while not inputOK:
    base = float (input ('enter base: '))
    if type (base) == type (1.0): inputOK = True
    else: print ('error. base must be a floating point number')

#get height
inputOK = False
while not inputOK:
    height = float(input ('enter hight: '))
    if type (height) == type (1.0): inputOK = True
    else: print ('error. height must be a floating point number')
hype = math.sqrt (base * base + height * height)   
print ('base: '+ str (base) + ',height: ' + str (height) + ',hyp:' + str (hype))
