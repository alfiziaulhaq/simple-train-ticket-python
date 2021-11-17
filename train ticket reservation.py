#BISMILLAH
import os
import random
from datetime import datetime
price = [100,150,200,250]
total=[]
a=[]    #dashboard
b=1     #repeat booking
x=[]    #destination
y=[]    #date arrive
z=[]    #name of destination
w=[]    #price
fm=[]   #sex [[]]
p=[]    #passnger name [[]]
q=[]    #passanger seat number[[]]
rs=[]   #number of passangers per destination

print('-------wellcome to E-train ticket reservation---------')
print('this is syncing by your paypal account balance ')
print('you can get discount if your pay out minimum $555.00 ')
print('1. booking ticket now')


while '1'not in a : 
    a.append(input('click " 1 " button for booking now : '))

def info():
    print('------------------------------------------------------')
    print("\t%s\t\t\t%s"%('destination','price'))
    print("%s\t\t\t%s"%('1. NEWCALP - BIKINI BOTTOM',('${:,.2f}'.format(float(price[0])))))
    print("%s\t\t\t%s"%('2. KREMLIN   -  PENTAGON  ',('${:,.2f}'.format(float(price[1])))))
    print("%s\t\t\t%s"%('3. PYONGYANG - CALIFORNIA ',('${:,.2f}'.format(float(price[2])))))
    print("%s\t\t\t%s"%('4. KONOHA  - MARINEFORD   ',('${:,.2f}'.format(float(price[3])))))
    print('------------------------------------------------------')

def passanger(r,s):   
    print('------------------------------------------------------')
    fff=[]
    if r>s:
        ppp=input('name of passanger : ')
        pp.append(ppp)

        while '1' not in fff and '2' not in  fff :
            print("click ' 1 ' button for MALE or click ' 2 ' button for FEMALE ")
            fff.append(input("passanger's sex : "))
        if int(fff[-1])==1:
            f.append('MALE')
        else :
            f.append('FEMALE')
        
        passanger(r,s+1)
    elif r==s :
        ppp=input('name of passanger : ')
        pp.append(ppp)

        while '1' not in fff and '2' not in  fff :
            print("click ' 1 ' button for MALE or click ' 2 ' button for FEMALE ")
            fff.append(input("passanger's sex : "))
        if int(fff[-1])==1:
            f.append('MALE')
        else :
            f.append('FEMALE')

while b ==1 :
    xx=[]
    xxx=0
    yy=0
    yyy=0
    f=[]
    pp=[]
    qq=[]
    rr=[]
    r=0
    s=1

    info()
    while '1'not in xx and '2'not in xx and '3'not in xx and '4'not in xx  :
        xx.append(input('select your destination(1/2/3/4) : '))
    x.append(int(xx[-1]))
    xxx=int(xx[-1])
    if xxx==1 :
        z.append('NEWCALP-BIKINI BOTTOM')
        w.append(price[0])
    elif xxx==2 :
        z.append('KREMLIN  -  PENTAGON')
        w.append(price[1])
    elif xxx==3 :
        z.append('PYONGYANG-CALIFORNIA')
        w.append(price[2])
    else :
        z.append('KONOHA -  MARINEFORD')
        w.append(price[3])

    date = False
    while date==False:
        yy=str(input('enter date destination (dd-mm) : '))
        date = True 
        format = "%d-%m"
        try :
            date = bool(datetime.strptime(yy,format))
            y.append(yy + '-2022')
            date=True
        except  :
            print ('none day or month = ',yy,'-2022')
            print('please fill it carefully !!!')
            date =False

    rr=[]
    while '1'not in rr and '2'not in rr and '3'not in rr and '4'not in rr and '5'not in rr  :
        print ('maximum reservation are 5 passanger !!!')
        rr.append(input('number of passanger = '))
    r=int(rr[-1])
    passanger(r,s)

    qqq= random.sample(range(100,300),1)
    for k in range(r) :
        qq.append(qqq[-1]+k)

    fm.append(f)
    p.append(pp)
    q.append(qq)
    rs.append(r)
    print('------------------------------------------------------')

    c=[]
    print('do you want to choose other destination ? ')
    print('1. yes, i do : click " 1 " button to repeat booking : ')
    print('2. no, thanks: random click except " 1 " button ')
    c.append(input('select your decision : '))
    if '1' not in c:   
        b=5

print('------------------------------------------------------')
print ("\t%s\t%s\t%s\t\t%s\t%s\t%s"%('destination','date arrive','name','sex','seat number ','price'))
print('-----------------------------------------------------------------------------------------------------')
for i in range(len(x)) :
    for j in range(rs[i]) :
        print("%s\t%s\t%s\t\t%s\t%s\t\t%s"%(z[i],y[i],p[i][j],fm[i][j],q[i][j],('${:,.2f}'.format(w[i]))))
print('-----------------------------------------------------------------------------------------------------')

#total order price
for i in range(len(x)):
    total.append(w[i]*len(p[i]))
# count discount
if sum(total)>=555 :
    disc=(1/10)*sum(total)
else:
    disc=0
pay = sum(total)-disc
print("\t\t\t\t\t\t\t\t%s\t%s"%('total    = ',('${:,.2f}'.format(sum(total)))))
print("\t\t\t\t\t\t\t\t%s\t%s"%('discount = ',('${:,.2f}'.format(disc))))
print("\t\t\t\t\t\t\t\t%s\t%s"%('pay out  = ',('${:,.2f}'.format(pay))))

print (x)
print(y)
print(p)




