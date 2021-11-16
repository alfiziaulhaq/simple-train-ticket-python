#BISMILLAH
import os
from datetime import datetime
price = [100,150,200,250]
a=[]
b=1
x=[]
y=[]
z=[]
v=[]
p=[]
q=[]
rs=[]

print('-------wellcome to E-train ticket reservation---------')
print('1. booking ticket now')
print('2. no ! next time')

while '1'not in a and '2' not in a: 
    a.append(input('select your choice (1/2) : '))
if a ==2:
    os.system('cls') #cant close program

def info():
    print('------------------------------------------------------')
    print("\t%s\t\t\t%s"%('destination','price'))
    print("%s\t\t\t%s"%('NEWCALP - BIKINI BOTTOM',('${:,.2f}'.format(float(price[0])))))
    print("%s\t\t\t%s"%('KREMLIN   -  PENTAGON  ',('${:,.2f}'.format(float(price[1])))))
    print("%s\t\t\t%s"%('PYONGYANG - CALIFORNIA ',('${:,.2f}'.format(float(price[2])))))
    print("%s\t\t\t%s"%('KONOHA  - MARINEFORD   ',('${:,.2f}'.format(float(price[3])))))
    print('------------------------------------------------------')

def passanger(r,s):   
    print('------------------------------------------------------')
    if r>s:
        ppp=input('name of passanger : ')
        pp.append(ppp)
        
        qqq=0
        while qqq<=0 or qqq>100 :
            qqq=int(input('number of chair(1-100) : '))
        qq.append(qqq)
        passanger(r,s+1)
        
    elif r==s :
        ppp=input('name of passanger : ')
        pp.append(ppp)
        
        qqq=0
        while qqq<=0 or qqq>100 :
            qqq=int(input('number of chair(1-100) : '))
        
        qq.append(qqq)

while b ==1 :
    xx=[]
    xxx=0
    yy=0
    yyy=0
    pp=[]
    qq=[]
    rr=[]
    r=0
    s=1

    info()
    while '1'not in xx and '2'not in xx and '3'not in xx and '4'not in xx  :
        xx.append(input('select your destination : '))
    x.append(int(xx[-1]))
    xxx=int(xx[-1])
    if xxx==1 :
        z.append('NEWCALP-BIKINI BOTTOM')
        v.append('${:,.2f}'.format(float(price[0])))
    elif xxx==2 :
        z.append('KREMLIN  -  PENTAGON')
        v.append('${:,.2f}'.format(float(price[1])))
    elif xxx==3 :
        z.append('PYONGYANG-CALIFORNIA')
        v.append('${:,.2f}'.format(float(price[2])))
    else :
        z.append('KONOHA -  MARINEFORD')
        v.append('${:,.2f}'.format(float(price[3])))

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
    p.append(pp)
    q.append(qq)
    rs.append(r)
    print('------------------------------------------------------')

    c=[]
    c.append(input('booking again(1)? '))
    if '1' not in c:   
        b=5

print('------------------------------------------------------')
print ("\t%s\t%s\t%s\t\t%s\t%s"%('destination','date arrive','name','number of chair ','price'))

for i in range(len(x)) :
    for j in range(rs[i]) :
        print("%s\t%s\t%s\t\t\t%s\t\t%s"%(z[i],y[i],p[i][j],q[i][j],v[i]))
