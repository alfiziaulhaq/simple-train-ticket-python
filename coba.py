import random
incap=[]
concap=1
while concap==1 :
    rancap= random.sample(range(1,12),2)
    print (rancap[-1],'+',rancap[-2])
    incap.append(input('re captha = '))
    if incap[-1]==str(rancap[-1]+rancap[-2]) :
        concap=2
    else :
        print('your captcha input is false !!!')
print (' gotcha')