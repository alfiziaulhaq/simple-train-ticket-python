import random
cap=0
capin=[]
while cap==0: 
    cr=(random.sample(range(3,15),2))
    print(cr[0],'+',cr[-1])
    capin.append(input('enter re captcha = '))
    if capin[-1]==str(cr[0]+cr[-1]) :
        cap=1
    else :
        pass

        

        