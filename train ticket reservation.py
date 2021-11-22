#BISMILLAH
import os
import random
import pandas as pd
from datetime import datetime
price = [100,150,200,250,300,350,400,450]
total=[]
a=[]    #while conditional
b=1     #repeat booking
x=[]    #departures
y=[]    #depart time
z=[]    #name of departure
w=[]    #price
fm=[]   #gender [[]]
p=[]    #passnger name [[]]
q=[]    #passanger seat number[[]]
clas=[] #class
rs=[]   #number of passangers per destination
t=[]    #train number

print('-------- WELCOME TO E-TRAIN TICKET RESERVATION ---------')
print('this is SYNCING to your unlimited paypal account balance :)')
print('you can get DISCOUNT if your TOTAL ORDER MINIMUM $555.00 ')
print('1. booking ticket NOW !!!')

while '1'not in a : 
    a.append(input('click " 1 " button for booking now : '))

def info():
    print('------------------------------------------------------')
    print("\t%s\t\t%s\t%s"%('DEPARTURES','ECONOMY','BUSINESS'))
    print("%s\t%s\t%s"%('1. NEWCALP - BIKINI BOTTOM',('$'+str(price[0])),('$'+str(price[1]))))
    print("%s\t%s\t%s"%('2. KREMLIN   -  PENTAGON  ',('$'+str(price[2])),('$'+str(price[3]))))
    print("%s\t%s\t%s"%('3. PYONGYANG - CALIFORNIA ',('$'+str(price[4])),('$'+str(price[5]))))
    print("%s\t%s\t%s"%('4. KONOHA  - MARINEFORD   ',('$'+str(price[6])),('$'+str(price[7]))))
    print('------------------------------------------------------')

def datapas(s) :
    if s==1 :
        print('DATA OF first passanger ')
    elif s==2 :
        print('DATA OF second passanger ')
    elif s==3 :
        print('DATA OF third passanger ')
    else :
        print('DATA OF ',s,'th passanger ')

def passanger(s,r):   #input personal data of passanger
    print('------------------------------------------------------')
    datapas(s)
    fff=[]
    if s<r:
        ppp=input('NAME of passanger : ')
        pp.append(ppp.capitalize())

        while '1' not in fff and '2' not in  fff :
            print("1. MALE ")
            print('2. FEMALE')
            fff.append(input("select gender (1/2) : "))
        if int(fff[-1])==1:
            f.append('MALE')
        else :
            f.append('FEMALE')
        
        passanger(s+1,r)
    elif s==r :
        ppp=input('NAME of passanger : ')
        pp.append(ppp.capitalize())

        while '1' not in fff and '2' not in  fff :
            print("1. MALE ")
            print('2. FEMALE')
            fff.append(input("select gender (1/2) : "))
        if int(fff[-1])==1:
            f.append('MALE')
        else :
            f.append('FEMALE')

def classs(m,n):    #input class and the price
    if cl[-1]==str(1) :
        clas.append('BUSINESS')
        w.append(price[n])
    else:
        clas.append('ECONOMY')
        w.append(price[m])

def seat(m,n) : #for seat number that chosen randomly
    qqq= random.sample(range(m,n),1)
    if m<100 :
        kk='A '
    else :
        kk='B '

    for k in range(r) :
        qq.append(kk+str(qqq[-1]+k))

def train(u) :  #for train number
    uu=random.sample(range(500,700),1)
    t.append(u+str(uu[-1]))

def captcha() :
    cap=0
    capin=[]
    while cap==0: 
        cr=(random.sample(range(3,15),2))
        print('--------------------')
        print('enter re captcha !')
        capin.append(input(str(cr[0])+' + '+str(cr[-1])+' = '))
        if capin[-1]==str(cr[0]+cr[-1]) :
            cap=1
        else :
            pass

captcha()

while b ==1 :
    info()
    xx=[]
    xxx=0
    while '1'not in xx and '2'not in xx and '3'not in xx and '4'not in xx  :
        xx.append(input('select your departure(1/2/3/4) : ')) 
    x.append(int(xx[-1]))
     
    cl=[]
    while '1' not in cl and '2' not in cl :
        print('1. BUSINESS class')
        print('2. ECONOMY class')
        cl=input('select your class(1/2): ')

    xxx=int(xx[-1])
    if xxx==1 :
        z.append('NEWCALP-BIKINI BOTTOM')
        classs(0,1)
        train('NB ')
    elif xxx==2 :
        z.append('KREMLIN  -  PENTAGON')
        classs(2,3)       
        train('KP ')
    elif xxx==3 :
        z.append('PYONGYANG-CALIFORNIA')
        classs(4,5)
        train('PC ')
    else :
        z.append('KONOHA -  MARINEFORD')
        classs(6,7)
        train('KM ')

    yy=0
    yyy=0
    date = False
    while date==False:
        yy=str(input('enter DEPART TIME for the year of 2022 (DD-MM): '))
        date = True 
        format = "%d-%m"
        try :
            date = bool(datetime.strptime(yy,format))
        except  :
            print ('none day or month = ',yy,'-2022')
            print('please fill it carefully !!!')
            date =False
    clock=random.sample(range(1,12),1)
    y.append(yy +'-2022 '+str(clock[-1])+'pm GMT')

    r=0
    rc=False
    while rc==False :
        print ('maximum 9 passangers per departure package!!!')
        rr= input('NUMBER of passangers = ')
        for i in range(9) :
            if rr==str(i+1) :
                r=int(rr)
                rs.append(r)
                rc= True
            else :
                continue

    f=[]
    pp=[]
    s=1
    passanger(s,r)
    fm.append(f)
    p.append(pp)

    qq=[]
    if cl[-1]==str(1):
        seat(1,90)
    else :
        seat(100,300)
    q.append(qq)

    print('------------------------------------------------------')

    c=[]
    print('do you want to choose other departures ? ')
    print('1. yes, i do . click " 1 " button for REPEAT BOOKING : ')
    print('2. no, thanks. random click except " 1 " button for PRINT your INVOICE')
    c.append(input('select (1/2) : '))
    if '1' not in c:   
        b=4

print('------------------------------------------------------')

aa=['--------------------']
bb=['-------------------']
cc=['--------------------']
dd=['-------']
ee=['---------']
ff=['------------']
gg=['-----------']
hh=['-----']
for i in range(len(x)) :
    for j in range(rs[i]) :
        (aa.append(z[i]),bb.append(y[i]),cc.append(p[i][j]),dd.append(fm[i][j]),ee.append(clas[i]),ff.append(t[i]),
        gg.append(q[i][j]),hh.append('$'+str(w[i])))
inv= {'DEPARTURES    ':aa,'DEPART TIME   ':bb,'NAME      ':cc,'GENDER':dd,'CLASS ':ee,'TRAIN NUMBER':ff,
'SEAT NUMBER':gg,'PRICE':hh}
invoice= pd.DataFrame(inv)
print(invoice)

#total order price
for i in range(len(x)):
    total.append(w[i]*len(p[i]))
# count discount
if sum(total)>=555 :
    disc=(1/10)*sum(total)
else:
    disc=0
pay = sum(total)-disc
print('-----------------------------------------------------------------------'+
'--------------------------------------------------')
print("\t\t\t\t\t\t\t\t\t\t\t\t%s\t%s"%('TOTAL    = ',('${:,.2f}'.format(sum(total)))))
print("\t\t\t\t\t\t\t\t\t\t\t\t%s\t%s"%('DISCOUNT = ',('${:,.2f}'.format(disc))))
print("\t\t\t\t\t\t\t\t\t\t\t\t%s"%('-------------------------'))
print("\t\t\t\t\t\t\t\t\t\t\t\t%s\t%s"%('PAY OUT  = ',('${:,.2f}'.format(pay))))


print('this is syncing to unlimited paypal account balance :)')
print('1. BUY now and PRINT TICKET')
a=[]
while '1'not in a : 
    a.append(input('click " 1 " button for BUY now and PRINT TICKET: '))

captcha()
for i in range(len(x)) :
    for j in range(rs[i]) :
        uwu=random.sample(range(1500,3000),1)
        print('=========================================================')
        print('                   E-TRAIN TICKET')
        print('TICKET NUMBER: ',t[i],'/',q[i][j],'/',uwu[-1])
        print('NAME         : ',p[i][j])
        print('GENDER       : ',fm[i][j])
        print('DEPARTURE    : ',z[i])
        print('DEPART TIME  : ',y[i])
        print('CLASS        : ',clas[i])
        print('TRAIN NUMBER : ',t[i])
        print('SEAT NUMBER  : ',q[i][j])
        print('PRICE        : ',('${:,.2f}'.format(w[i])))
print('=========================================================')





