#just input 1-100
b=False
while b==False :
    a= input('(1-100) = ')
    for i in range(100) :
        if a==str(i+1) :
            b= True
        else :
            continue
print ('gotcha')
print(b)
print(a)