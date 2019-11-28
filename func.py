import string
def codify(fil,cas):
    #fil maximo hay 4
    return((fil-1)*10)+cas

a=codify(1,2)
b=codify(2,3)
c=codify(3,4)
d=codify(4,5)
Lista=[a,b,c,d]
def decodify(n):
    #no poner numeros mayores a 40
    f= (n//10) +1
    aux = n%10
    if aux ==0:
        c = 10
    else:
        c= aux
    return f,c


def ronda(n,R):
    #R max 3 y n max 40
    return (n-1)*3 +R

def rec(l,m):
    if l>0:
        i1=str(l)
        m1= str(m)
        return ('Y'+'-'+'('+ i1 +','+ m1 +')')+str(rec(l-1,m))

codig={}
def char(int):
    codig[int]=chr(int)

for i in range (121):
    char(i)


codig[89]=chr(160)
codig[45]=chr(161)
codig[40]=chr(162)
codig[41]=chr(163)
codig[79]=chr(164)
codig[62]=chr(165)
#print(codig)

def tra(lista):
    size=len(lista)-1
    mo=lista
    for i in range(size):
        if lista[i].isdigit():
            if lista[i+1].isdigit():
                if lista[i+2].isdigit():
                    mo=mo.replace(lista[i:i+3], codig[int(lista[i:i+3])])
                    continue
                else:
                    mo=mo.replace(lista[i:i+2], codig[int(lista[i:i+2])])
                    continue
            else:
                mo=mo.replace(lista[i], codig[int(lista[i])])
                continue
        else:
            continue
    return mo


def list(numero_guia,Ronda,fichasT):
    if Ronda <=3:
        n1 = str(numero_guia)
        i1 =str(Ronda)
        l1=str(fichasT)
        pr=str('('+ n1 + ',' + i1 + ')' )
        pr1= str('Y'+'-'+pr)

        fn=str('[' + '-'+'('+ l1 +','+ i1 +']'+rec(39,Ronda) + ']')
        fn1 = fn.replace(pr1,'')
        fn3 = fn1.replace('[','('*33)
        fn4=fn3.replace(')',')'*2)
        fn5=fn4.replace(']',')')
        fn2 = fn5.replace("None",'')
        return pr+'>'+fn2

def final(Ronda,fichasT):
        n1= str('('+str(list(a,Ronda,fichasT))+'Y')
        n2= str('('+str(list(b,Ronda,fichasT))+'Y')
        n3= str('('+str(list(c,Ronda,fichasT))+'Y')
        n4= str('('+str(list(d,Ronda,fichasT)))
        return n1+n2+n3+n4

def casill(base,casilla):
    bas = base
    List=[1,2,3,4]
    List[0]= str(base)
    for i in range(1,4):
        base+=10
        List[i]= str(base)
    if bas==casilla:
        return '((('+str(casilla) +'Y-'+List[1]+')Y-'+List[2]+')Y-'+List[3]+')'
    else:
        n1='((('+str(casilla) +'Y-'+List[0]+')Y-'+List[1]+')Y-'+List[2]+')Y-'+List[3]+")"
        n2 =n1.replace("Y-"+str(casilla)+")","")
        return n2
def regla2():
    C1='((('+casill(1,1)+'Y'+casill(1,11)+')Y'+casill(1,21)+')Y'+casill(1,31)+')'
    C2='((('+casill(2,2)+'Y'+casill(2,12)+')Y'+casill(2,22)+')Y'+casill(2,32)+')'
    C3='((('+casill(3,3)+'Y'+casill(3,13)+')Y'+casill(3,23)+')Y'+casill(3,33)+')'
    C4='((('+casill(4,4)+'Y'+casill(4,14)+')Y'+casill(4,24)+')Y'+casill(4,34)+')'
    C5='((('+casill(5,5)+'Y'+casill(5,15)+')Y'+casill(5,25)+')Y'+casill(5,35)+')'
    C6='((('+casill(6,6)+'Y'+casill(6,16)+')Y'+casill(6,26)+')Y'+casill(6,36)+')'
    C7='((('+casill(7,7)+'Y'+casill(7,17)+')Y'+casill(7,27)+')Y'+casill(7,37)+')'
    C8='((('+casill(8,8)+'Y'+casill(8,18)+')Y'+casill(8,28)+')Y'+casill(8,38)+')'
    C9='((('+casill(9,9)+'Y'+casill(9,19)+')Y'+casill(9,29)+')Y'+casill(9,39)+')'
    C10='((('+casill(10,10)+'Y'+casill(10,20)+')Y'+casill(10,30)+')Y'+casill(10,40)+')'
    return '((((((((('+C1+'Y'+C2+')Y'+C3+')Y'+C4+')Y'+C5+')Y'+C6+')Y'+C7+')Y'+C8+')Y'+C9+')Y'+C10+')'

print('------------------------------------------------------------')
#regla1
l1=str(final(1,40))
l2= l1.replace('Y(None)','')
l2= l2.replace('YNone','')
#l2 ya es el final de la primera regla
l3=('('+l2.replace('))))',')))'))

l4=l3.replace('Y((24,1)',')Y((24,1)')
l4=l4.replace('Y((35,1)',')Y((35,1)')
l4=l4.replace('(((((((((((((((((((((((((((((((((','((((((((((((((((((((((((((((((((((((((')

n1=str(final(2,40))
n2= n1.replace('Y(None)','')
n2= n2.replace('YNone','')
#l2 ya es el final de la primera regla
n3=('('+n2.replace('))))',')))'))

n4=n3.replace('Y((24,2)',')Y((24,2)')
n4=n4.replace('Y((35,2)',')Y((35,2)')
n4=n4.replace('(((((((((((((((((((((((((((((((((','((((((((((((((((((((((((((((((((((((((')

k1=str(final(3,40))
k2= k1.replace('Y(None)','')
k2= k2.replace('YNone','')
#l2 ya es el final de la primera regla
k3=('('+k2.replace('))))',')))'))

k4=k3.replace('Y((24,3)',')Y((24,3)')
k4=k4.replace('Y((35,3)',')Y((35,3)')
k4=k4.replace('(((((((((((((((((((((((((((((((((','((((((((((((((((((((((((((((((((((((((')

regla='((((('+l4+')'+'((('+n4+'))'+'((('+k4+'))'
#print (regla1)

o=regla
o=o.replace("(2,1)",str(ronda(2,1)))
o=o.replace("(1,1)",str(ronda(1,1)))
o=o.replace("(3,1)",str(ronda(3,1)))
o=o.replace("(4,1)",str(ronda(4,1)))
o=o.replace("(5,1)",str(ronda(5,1)))
o=o.replace("(6,1)",str(ronda(6,1)))
o=o.replace("(7,1)",str(ronda(7,1)))
o=o.replace("(8,1)",str(ronda(8,1)))
o=o.replace("(9,1)",str(ronda(9,1)))
o=o.replace("(10,1)",str(ronda(10,1)))

o=o.replace("(12,1)",str(ronda(12,1)))
o=o.replace("(11,1)",str(ronda(11,1)))
o=o.replace("(13,1)",str(ronda(13,1)))
o=o.replace("(14,1)",str(ronda(14,1)))
o=o.replace("(15,1)",str(ronda(15,1)))
o=o.replace("(16,1)",str(ronda(16,1)))
o=o.replace("(17,1)",str(ronda(17,1)))
o=o.replace("(18,1)",str(ronda(18,1)))
o=o.replace("(19,1)",str(ronda(19,1)))
o=o.replace("(20,1)",str(ronda(20,1)))

o=o.replace("(22,1)",str(ronda(22,1)))
o=o.replace("(21,1)",str(ronda(21,1)))
o=o.replace("(23,1)",str(ronda(23,1)))
o=o.replace("(24,1)",str(ronda(24,1)))
o=o.replace("(25,1)",str(ronda(25,1)))
o=o.replace("(26,1)",str(ronda(26,1)))
o=o.replace("(27,1)",str(ronda(27,1)))
o=o.replace("(28,1)",str(ronda(28,1)))
o=o.replace("(29,1)",str(ronda(29,1)))
o=o.replace("(30,1)",str(ronda(30,1)))

o=o.replace("(32,1)",str(ronda(32,1)))
o=o.replace("(31,1)",str(ronda(31,1)))
o=o.replace("(33,1)",str(ronda(33,1)))
o=o.replace("(34,1)",str(ronda(34,1)))
o=o.replace("(35,1)",str(ronda(35,1)))
o=o.replace("(36,1)",str(ronda(36,1)))
o=o.replace("(37,1)",str(ronda(37,1)))
o=o.replace("(38,1)",str(ronda(38,1)))
o=o.replace("(39,1)",str(ronda(39,1)))
o=o.replace("(40,1)",str(ronda(40,1)))

o=o.replace("(2,2)",str(ronda(2,2)))
o=o.replace("(1,2)",str(ronda(1,2)))
o=o.replace("(3,2)",str(ronda(3,2)))
o=o.replace("(4,2)",str(ronda(4,2)))
o=o.replace("(5,2)",str(ronda(5,2)))
o=o.replace("(6,2)",str(ronda(6,2)))
o=o.replace("(7,2)",str(ronda(7,2)))
o=o.replace("(8,2)",str(ronda(8,2)))
o=o.replace("(9,2)",str(ronda(9,2)))
o=o.replace("(10,2)",str(ronda(10,2)))

o=o.replace("(12,2)",str(ronda(12,2)))
o=o.replace("(11,2)",str(ronda(11,2)))
o=o.replace("(13,2)",str(ronda(13,2)))
o=o.replace("(14,2)",str(ronda(14,2)))
o=o.replace("(15,2)",str(ronda(15,2)))
o=o.replace("(16,2)",str(ronda(16,2)))
o=o.replace("(17,2)",str(ronda(17,2)))
o=o.replace("(18,2)",str(ronda(18,2)))
o=o.replace("(19,2)",str(ronda(19,2)))
o=o.replace("(20,2)",str(ronda(20,2)))

o=o.replace("(22,2)",str(ronda(22,2)))
o=o.replace("(21,2)",str(ronda(21,2)))
o=o.replace("(23,2)",str(ronda(23,2)))
o=o.replace("(24,2)",str(ronda(24,2)))
o=o.replace("(25,2)",str(ronda(25,2)))
o=o.replace("(26,2)",str(ronda(26,2)))
o=o.replace("(27,2)",str(ronda(27,2)))
o=o.replace("(28,2)",str(ronda(28,2)))
o=o.replace("(29,2)",str(ronda(29,2)))
o=o.replace("(30,2)",str(ronda(30,2)))

o=o.replace("(32,2)",str(ronda(32,2)))
o=o.replace("(31,2)",str(ronda(31,2)))
o=o.replace("(33,2)",str(ronda(33,2)))
o=o.replace("(34,2)",str(ronda(34,2)))
o=o.replace("(35,2)",str(ronda(35,2)))
o=o.replace("(36,2)",str(ronda(36,2)))
o=o.replace("(37,2)",str(ronda(37,2)))
o=o.replace("(38,2)",str(ronda(38,2)))
o=o.replace("(39,2)",str(ronda(39,2)))
o=o.replace("(40,2)",str(ronda(40,2)))

o=o.replace("(2,3)",str(ronda(2,3)))
o=o.replace("(1,3)",str(ronda(1,3)))
o=o.replace("(3,3)",str(ronda(3,3)))
o=o.replace("(4,3)",str(ronda(4,3)))
o=o.replace("(5,3)",str(ronda(5,3)))
o=o.replace("(6,3)",str(ronda(6,3)))
o=o.replace("(7,3)",str(ronda(7,3)))
o=o.replace("(8,3)",str(ronda(8,3)))
o=o.replace("(9,3)",str(ronda(9,3)))
o=o.replace("(10,3)",str(ronda(10,3)))

o=o.replace("(12,3)",str(ronda(12,3)))
o=o.replace("(11,3)",str(ronda(11,3)))
o=o.replace("(13,3)",str(ronda(13,3)))
o=o.replace("(14,3)",str(ronda(14,3)))
o=o.replace("(15,3)",str(ronda(15,3)))
o=o.replace("(16,3)",str(ronda(16,3)))
o=o.replace("(17,3)",str(ronda(17,3)))
o=o.replace("(18,3)",str(ronda(18,3)))
o=o.replace("(19,3)",str(ronda(19,3)))
o=o.replace("(20,3)",str(ronda(20,3)))

o=o.replace("(22,3)",str(ronda(22,3)))
o=o.replace("(21,3)",str(ronda(21,3)))
o=o.replace("(23,3)",str(ronda(23,3)))
o=o.replace("(24,3)",str(ronda(24,3)))
o=o.replace("(25,3)",str(ronda(25,3)))
o=o.replace("(26,3)",str(ronda(26,3)))
o=o.replace("(27,3)",str(ronda(27,3)))
o=o.replace("(28,3)",str(ronda(28,3)))
o=o.replace("(29,3)",str(ronda(29,3)))
o=o.replace("(30,3)",str(ronda(30,3)))

o=o.replace("(32,3)",str(ronda(32,3)))
o=o.replace("(31,3)",str(ronda(31,3)))
o=o.replace("(33,3)",str(ronda(33,3)))
o=o.replace("(34,3)",str(ronda(34,3)))
o=o.replace("(35,3)",str(ronda(35,3)))
o=o.replace("(36,3)",str(ronda(36,3)))
o=o.replace("(37,3)",str(ronda(37,3)))
o=o.replace("(38,3)",str(ronda(38,3)))
o=o.replace("(39,3)",str(ronda(39,3)))
o=o.replace("(40,3)",str(ronda(40,3)))



a='((4>((((((((((((((((((((((((((((((((((((((-118Y-115)Y-112)Y-109)Y-106)Y-103)Y-100)Y-97)Y-94)Y-91)Y-88)Y-85)Y-82)Y-79)Y-76)Y-73)Y-70)Y-67)Y-64)Y-61)Y-58)Y-55)Y-52)Y-49)Y-46)Y-43)Y-40)Y-37)Y-34)Y-31)Y-28)Y-25)Y-22)Y-19)Y-16)Y-13)Y-10)Y-7)Y-1)))'
b='(37>((((((((((((((((((((((((((((((((((((((-118Y-115)Y-112)Y-109)Y-106)Y-103)Y-100)Y-97)Y-94)Y-91)Y-88)Y-85)Y-82)Y-79)Y-76)Y-73)Y-70)Y-67)Y-64)Y-61)Y-58)Y-55)Y-52)Y-49)Y-46)Y-43)Y-40)Y-34)Y-31)Y-28)Y-25)Y-22)Y-19)Y-16)Y-13)Y-10)Y-7)Y-4)Y-1))'
c='(70>((((((((((((((((((((((((((((((((((((((-118Y-115)Y-112)Y-109)Y-106)Y-103)Y-100)Y-97)Y-94)Y-91)Y-88)Y-85)Y-82)Y-79)Y-76)Y-73)Y-67)Y-64)Y-61)Y-58)Y-55)Y-52)Y-49)Y-46)Y-43)Y-40)Y-37)Y-34)Y-31)Y-28)Y-25)Y-22)Y-19)Y-16)Y-13)Y-10)Y-7)Y-4)Y-1))'
d='(103>((((((((((((((((((((((((((((((((((((((-118Y-115)Y-112)Y-109)Y-106)Y-100)Y-97)Y-94)Y-91)Y-88)Y-85)Y-82)Y-79)Y-76)Y-73)Y-70)Y-67)Y-64)Y-61)Y-58)Y-55)Y-52)Y-49)Y-46)Y-43)Y-40)Y-37)Y-34)Y-31)Y-28)Y-25)Y-22)Y-19)Y-16)Y-13)Y-10)Y-7)Y-4)Y-1))'


ma= '(('+a+'Y'+b+')'+'Y'+'('+c+'Y'+d+'))'


e='(5>((((((((((((((((((((((((((((((((((((((-119Y-116)Y-113)Y-110)Y-107)Y-104)Y-101)Y-98)Y-95)Y-92)Y-89)Y-86)Y-83)Y-80)Y-77)Y-74)Y-71)Y-68)Y-65)Y-62)Y-59)Y-56)Y-53)Y-50)Y-47)Y-44)Y-41)Y-38)Y-35)Y-32)Y-29)Y-26)Y-23)Y-20)Y-17)Y-14)Y-11)Y-8)Y-2))'
f='(38>((((((((((((((((((((((((((((((((((((((-119Y-116)Y-113)Y-110)Y-107)Y-104)Y-101)Y-98)Y-95)Y-92)Y-89)Y-86)Y-83)Y-80)Y-77)Y-74)Y-71)Y-68)Y-65)Y-62)Y-59)Y-56)Y-53)Y-50)Y-47)Y-44)Y-41)Y-35)Y-32)Y-29)Y-26)Y-23)Y-20)Y-17)Y-14)Y-11)Y-8)Y-5)Y-2))'
g='(71>((((((((((((((((((((((((((((((((((((((-119Y-116)Y-113)Y-110)Y-107)Y-104)Y-101)Y-98)Y-95)Y-92)Y-89)Y-86)Y-83)Y-80)Y-77)Y-74)Y-68)Y-65)Y-62)Y-59)Y-56)Y-53)Y-50)Y-47)Y-44)Y-41)Y-38)Y-35)Y-32)Y-29)Y-26)Y-23)Y-20)Y-17)Y-14)Y-11)Y-8)Y-5)Y-2))'
h='(104>((((((((((((((((((((((((((((((((((((((-119Y-116)Y-113)Y-110)Y-107)Y-101)Y-98)Y-95)Y-92)Y-89)Y-86)Y-83)Y-80)Y-77)Y-74)Y-71)Y-68)Y-65)Y-62)Y-59)Y-56)Y-53)Y-50)Y-47)Y-44)Y-41)Y-38)Y-35)Y-32)Y-29)Y-26)Y-23)Y-20)Y-17)Y-14)Y-11)Y-8)Y-5)Y-2))'
mo= '(('+e+'Y'+f+')'+'Y'+'('+g+'Y'+h+'))'



i='(6>((((((((((((((((((((((((((((((((((((((-120Y-117)Y-114)Y-111)Y-108)Y-105)Y-102)Y-99)Y-96)Y-93)Y-90)Y-87)Y-84)Y-81)Y-78)Y-75)Y-72)Y-69)Y-66)Y-63)Y-60)Y-57)Y-54)Y-51)Y-48)Y-45)Y-42)Y-39)Y-36)Y-33)Y-30)Y-27)Y-24)Y-21)Y-18)Y-15)Y-12)Y-9)Y-3))'
j='(39>((((((((((((((((((((((((((((((((((((((-120Y-117)Y-114)Y-111)Y-108)Y-105)Y-102)Y-99)Y-96)Y-93)Y-90)Y-87)Y-84)Y-81)Y-78)Y-75)Y-72)Y-69)Y-66)Y-63)Y-60)Y-57)Y-54)Y-51)Y-48)Y-45)Y-42)Y-36)Y-33)Y-30)Y-27)Y-24)Y-21)Y-18)Y-15)Y-12)Y-9)Y-6)Y-3))'
k='(72>((((((((((((((((((((((((((((((((((((((-120Y-117)Y-114)Y-111)Y-108)Y-105)Y-102)Y-99)Y-96)Y-93)Y-90)Y-87)Y-84)Y-81)Y-78)Y-75)Y-69)Y-66)Y-63)Y-60)Y-57)Y-54)Y-51)Y-48)Y-45)Y-42)Y-39)Y-36)Y-33)Y-30)Y-27)Y-24)Y-21)Y-18)Y-15)Y-12)Y-9)Y-6)Y-3))'
l='(105>((((((((((((((((((((((((((((((((((((((-120Y-117)Y-114)Y-111)Y-108)Y-102)Y-99)Y-96)Y-93)Y-90)Y-87)Y-84)Y-81)Y-78)Y-75)Y-72)Y-69)Y-66)Y-63)Y-60)Y-57)Y-54)Y-51)Y-48)Y-45)Y-42)Y-39)Y-36)Y-33)Y-30)Y-27)Y-24)Y-21)Y-18)Y-15)Y-12)Y-9)Y-6)Y-3))'

#regla 1 donde se pone la prelacion del tiempo1
mu= '(('+i+'Y'+j+')'+'Y'+'('+k+'Y'+l+'))'
#print(mu)
#regla1 traducida
lo= '(('+ma+'Y'+mo+')'+'Y'+mu+')'
#print(lo)
regla1=tra(lo)
print(regla1)


print('------------------------------------------------------------')
#regla 2 donde no puede haber dos fichas en una misma casilla

gol='(((((((((((((((1Y-31)Y-61)Y-91)Y(((31Y-1)Y-61)Y-91))Y(((61Y-1)Y-31)Y-91))Y(((91Y-1)Y-31)Y-61))Y((((((4Y-34)Y-64)Y-94)Y(((34Y-4)Y-64)Y-94))Y(((64Y-4)Y-34)Y-94))Y(((94Y-4)Y-34)Y-64)))Y((((((7Y-37)Y-67)Y-97)Y(((37Y-7)Y-67)Y-97))Y(((67Y-7)Y-37)Y-97))Y(((97Y-7)Y-37)Y-67)))Y((((((10Y-40)Y-70)Y-100)Y(((40Y-10)Y-70)Y-100))Y(((70Y-10)Y-40)Y-100))Y(((100Y-10)Y-40)Y-70)))Y((((((13Y-43)Y-73)Y-103)Y(((43Y-13)Y-73)Y-103))Y(((73Y-13)Y-43)Y-103))Y(((103Y-13)Y-43)Y-73)))Y((((((16Y-46)Y-76)Y-106)Y(((46Y-6)Y-76)Y-106))Y(((76Y-16)Y-46)Y-106))Y(((106Y-16)Y-46)Y-76)))Y((((((19Y-49)Y-79)Y-109)Y(((49Y-19)Y-79)Y-109))Y(((79Y-19)Y-49)Y-109))Y(((109Y-19)Y-49)Y-79)))Y((((((22Y-52)Y-82)Y-112)Y(((52Y-22)Y-82)Y-112))Y(((82Y-22)Y-52)Y-112))Y(((112Y-22)Y-52)Y-82)))Y((((((25Y-55)Y-85)Y-115)Y(((55Y-25)Y-85)Y-115))Y(((85Y-25)Y-55)Y-115))Y(((115Y-25)Y-55)Y-85)))Y((((((28Y-58)Y-88)Y-118)Y(((58Y-28)Y-88)Y-118))Y(((88Y-28)Y-58)Y-118))Y(((118Y-28)Y-58)Y-88)))'


gal='(((((((((((((((2Y-32)Y-62)Y-92)Y(((32Y-2)Y-62)Y-92))Y(((62Y-2)Y-32)Y-92))Y(((92Y-2)Y-32)Y-62))Y((((((5Y-35)Y-65)Y-95)Y(((35Y-5)Y-65)Y-95))Y(((65Y-5)Y-35)Y-95))Y(((95Y-5)Y-35)Y-65)))Y((((((8Y-38)Y-68)Y-98)Y(((38Y-8)Y-68)Y-98))Y(((68Y-8)Y-38)Y-98))Y(((98Y-8)Y-38)Y-68)))Y((((((11Y-41)Y-71)Y-101)Y(((41Y-11)Y-71)Y-101))Y(((71Y-11)Y-41)Y-101))Y(((101Y-11)Y-41)Y-71)))Y((((((14Y-44)Y-74)Y-104)Y(((44Y-14)Y-74)Y-104))Y(((74Y-14)Y-44)Y-104))Y(((104Y-14)Y-44)Y-74)))Y((((((17Y-47)Y-77)Y-107)Y(((47Y-7)Y-77)Y-107))Y(((77Y-17)Y-47)Y-107))Y(((107Y-17)Y-47)Y-77)))Y((((((20Y-50)Y-80)Y-110)Y(((50Y-20)Y-80)Y-110))Y(((80Y-20)Y-50)Y-110))Y(((110Y-20)Y-50)Y-80)))Y((((((23Y-53)Y-83)Y-113)Y(((53Y-23)Y-83)Y-113))Y(((83Y-23)Y-53)Y-113))Y(((113Y-23)Y-53)Y-83)))Y((((((26Y-56)Y-86)Y-116)Y(((56Y-26)Y-86)Y-116))Y(((86Y-26)Y-56)Y-116))Y(((116Y-26)Y-56)Y-86)))Y((((((29Y-59)Y-89)Y-119)Y(((59Y-29)Y-89)Y-119))Y(((89Y-29)Y-59)Y-119))Y(((119Y-29)Y-59)Y-89)))'

gil='(((((((((((((((3Y-33)Y-63)Y-93)Y(((33Y-3)Y-63)Y-93))Y(((63Y-3)Y-33)Y-93))Y(((93Y-3)Y-33)Y-63))Y((((((6Y-36)Y-66)Y-96)Y(((36Y-6)Y-66)Y-96))Y(((66Y-6)Y-36)Y-96))Y(((96Y-6)Y-36)Y-66)))Y((((((9Y-39)Y-69)Y-99)Y(((39Y-9)Y-69)Y-99))Y(((69Y-9)Y-39)Y-99))Y(((99Y-9)Y-39)Y-69)))Y((((((12Y-42)Y-72)Y-102)Y(((42Y-12)Y-72)Y-102))Y(((72Y-12)Y-42)Y-102))Y(((102Y-12)Y-42)Y-72)))Y((((((15Y-45)Y-75)Y-105)Y(((45Y-15)Y-75)Y-105))Y(((75Y-15)Y-45)Y-105))Y(((105Y-15)Y-45)Y-75)))Y((((((18Y-48)Y-78)Y-108)Y(((48Y-8)Y-78)Y-108))Y(((78Y-18)Y-48)Y-108))Y(((108Y-18)Y-48)Y-78)))Y((((((21Y-51)Y-81)Y-111)Y(((51Y-21)Y-81)Y-111))Y(((81Y-21)Y-51)Y-111))Y(((111Y-21)Y-51)Y-81)))Y((((((24Y-54)Y-84)Y-114)Y(((54Y-24)Y-84)Y-114))Y(((84Y-24)Y-54)Y-114))Y(((114Y-24)Y-54)Y-84)))Y((((((27Y-57)Y-87)Y-117)Y(((57Y-27)Y-87)Y-117))Y(((87Y-27)Y-57)Y-117))Y(((117Y-27)Y-57)Y-87)))Y((((((30Y-60)Y-90)Y-120)Y(((60Y-30)Y-90)Y-120))Y(((90Y-30)Y-60)Y-120))Y(((120Y-30)Y-60)Y-90)))'

esta= '(('+gol+'Y'+gal+')Y'+gil+')'
#print(esta)
#regla2 traducida
regla2= tra(esta)
print(regla2)
print('------------------------------------------------------------')
def mov1 ():
#Movimiento una ficha en la posicion 1 implica
    mov1 = str('('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'1'+'>'+'-1'+'Y'+')'+'-2'+'Y'+')'+'3'+'Y'+')'+'-4'+'Y'+')'+'-5'+'Y'+')'+'-6'+'Y'+')'+'-7'+'Y'+')'+'-8'+'Y'+')'+'-9'+'Y'+')'+'-10'+')')
    return mov1

def mov2():
#Movimiento una ficha en la posicion 2 imnplica
    mov2 =str('('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'4'+'Y'+'23'+')'+'>'+'-1'+'Y'+')'+'-2'+'Y'+')'+'-3'+'Y'+')'+'-4'+'Y'+')'+'-5'+'Y'+')'+'-6'+'Y'+')'+'-7'+'Y'+')'+'-8'+'Y'+')'+'-9'+'Y'+')'+'10'+')'+'-11'+'Y'+')'+'-12'+'Y'+')'+'-13'+'Y'+')'+'-14'+'Y'+')'+'-15'+'Y'+')'+'-16'+'Y'+')'+'-17'+'Y'+')'+'-18'+'Y'+')'+'-19'+'Y'+')'+'-20'+')'+'-21'+'Y'+')'+'-22'+'Y'+')'+'-23'+'Y'+')'+'-24'+'Y'+')'+'-25'+'Y'+')'+'-26'+'Y'+')'+'-27'+'Y'+')'+'-28'+'Y'+')'+'-29'+'Y'+')'+'-30'+')'+'-31'+'Y'+')'+'-32'+'Y'+')'+'-33'+'Y'+')'+'-34'+'Y'+')'+'-35'+'Y'+')'+'-36'+'Y'+')'+'-37'+'Y'+')'+'-38'+'Y'+')'+'-39'+'Y'+')'+'-40'+'Y'+')'+'-41'+'Y'+')'+'-42'+'Y'+')'+'-43'+'Y'+')'+'-44'+'Y'+')'+'-45'+'Y'+')'+'-46'+'Y'+')'+'-47'+'Y'+')'+'-48'+'Y'+')'+'-49'+'Y'+')'+'-50'+'Y'+')'+'-51'+'Y'+')'+'-52'+'Y'+')'+'-53'+'Y'+')'+'-54'+'Y'+')'+'-55'+'Y'+')'+'-56'+'Y'+')'+'-57'+'Y'+')'+'-58'+'Y'+')'+'-59'+'Y'+')'+'-60'+'Y'+')'+'-61'+'Y'+')'+'-62'+'Y'+')'+'-63'+'Y'+')'+'-64'+'Y'+')'+'-65'+'Y'+')'+'-66'+'Y'+')'+'-67'+'Y'+')'+'-68'+'Y'+')'+'-69'+'Y'+')'+'-70'+'Y'+')'+'-71'+'Y'+')'+'-72'+'Y'+')'+'-73'+'Y'+')'+'-74'+'Y'+')'+'-75'+'Y'+')'+'-76'+'Y'+')'+'-77'+'Y'+')'+'-78'+'Y'+')'+'-79'+'Y'+')'+'-80'+'Y'+')'+'-81'+'Y'+')'+'-82'+'Y'+')'+'-83'+'Y'+')'+'-84'+'Y'+')'+'-85'+'Y'+')'+'-86'+'Y'+')'+'-87'+'Y'+')'+'-88'+'Y'+')'+'-89'+'Y'+')'+'-90'+'Y'+')'+'-91'+'Y'+')'+'-92'+'Y'+')'+'-93'+'Y'+')'+'-94'+'Y'+')'+'-95'+'Y'+')'+'-96'+'Y'+')'+'-97'+'Y'+')'+'-98'+'Y'+')'+'-99'+'Y'+')'+'-100'+'Y'+')'+'-101'+'Y'+')'+'-102'+'Y'+')'+'-103'+'Y'+')'+'-104'+'Y'+')'+'-105'+'Y'+')'+'-106'+'Y'+')'+'-107'+'Y'+')'+'-108'+'Y'+')'+'-109'+'Y'+')'+'-110'+'Y'+')'+'-111'+'Y'+')'+'-112'+'Y'+')'+'-113'+'Y'+')'+'-114'+'Y'+')'+'-115'+'Y'+')'+'-116'+'Y'+')'+'-117'+'Y'+')'+'-118'+'Y'+')'+'-119'+'Y'+')'+'-120'+')')
    return mov2

def mov3():
#Movimiento una ficha en la posicion 3 imnplica
    mov3 =str('('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'3'+'>'+'1'+'Y'+')'+'-2'+'Y'+')'+'-3'+'Y'+')'+'-4'+'Y'+')'+'-5'+'Y'+')'+'-6'+'Y'+')'+'-7'+'Y'+')'+'-8'+'Y'+')'+'-9'+'Y'+')'+'-10'+')'+'O'+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'3'+'>'+'-1'+'Y'+')'+'-2'+'Y'+')'+'-3'+'Y'+')'+'4'+'Y'+')'+'-5'+'Y'+')'+'-6'+'Y'+')'+'-7'+'Y'+')'+'8'+'Y'+')'+'-9'+'Y'+')'+'-10'+')')
    return mov3

def mov4():
#Movimiento una ficha en la posicion 4 imnplica
    mov4 =str('('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'12'+'Y'+'55'+')'+'>'+'-1'+'Y'+')'+'-2'+'Y'+')'+'-3'+'Y'+')'+'-4'+'Y'+')'+'-5'+'Y'+')'+'-6'+'Y'+')'+'-7'+'Y'+')'+'-8'+'Y'+')'+'-9'+'Y'+')'+'-10'+')'+'-11'+'Y'+')'+'-12'+'Y'+')'+'-13'+'Y'+')'+'-14'+'Y'+')'+'-15'+'Y'+')'+'-16'+'Y'+')'+'-17'+'Y'+')'+'-18'+'Y'+')'+'-19'+'Y'+')'+'-20'+')'+'-21'+'Y'+')'+'-22'+'Y'+')'+'-23'+'Y'+')'+'-24'+'Y'+')'+'-25'+'Y'+')'+'-26'+'Y'+')'+'27'+'Y'+')'+'-28'+'Y'+')'+'-29'+'Y'+')'+'-30'+')'+'-31'+'Y'+')'+'-32'+'Y'+')'+'-33'+'Y'+')'+'-34'+'Y'+')'+'-35'+'Y'+')'+'-36'+'Y'+')'+'-37'+'Y'+')'+'-38'+'Y'+')'+'-39'+'Y'+')'+'-40'+')'+'-41'+'Y'+')'+'-42'+'Y'+')'+'-43'+'Y'+')'+'-44'+'Y'+')'+'-45'+'Y'+')'+'-46'+'Y'+')'+'-47'+'Y'+')'+'-48'+'Y'+')'+'-49'+'Y'+')'+'-50'+')'+'-51'+'Y'+')'+'-52'+'Y'+')'+'-53'+'Y'+')'+'-54'+'Y'+')'+'-55'+'Y'+')'+'-56'+'Y'+')'+'-57'+'Y'+')'+'-58'+'Y'+')'+'-59'+'Y'+')'+'-60'+')'+'-61'+'Y'+')'+'-62'+'Y'+')'+'-63'+'Y'+')'+'-64'+'Y'+')'+'-65'+'Y'+')'+'-66'+'Y'+')'+'-67'+'Y'+')'+'-68'+'Y'+')'+'-69'+'Y'+')'+'-70'+')'+'-71'+'Y'+')'+'-72'+'Y'+')'+'-73'+'Y'+')'+'-74'+'Y'+')'+'-75'+'Y'+')'+'-76'+'Y'+')'+'-77'+'Y'+')'+'-78'+'Y'+')'+'-79'+'Y'+')'+'-80'+')'+'-81'+'Y'+')'+'-82'+'Y'+')'+'-83'+'Y'+')'+'-84'+'Y'+')'+'-85'+'Y'+')'+'-86'+'Y'+')'+'-87'+'Y'+')'+'-88'+'Y'+')'+'-89'+'Y'+')'+'-90'+')'+'-91'+'Y'+')'+'-92'+'Y'+')'+'-93'+'Y'+')'+'-94'+'Y'+')'+'-95'+'Y'+')'+'-96'+'Y'+')'+'-97'+'Y'+')'+'-98'+'Y'+')'+'-99'+'Y'+')'+'-100'+')'+'-101'+'Y'+')'+'-102'+'Y'+')'+'-103'+'Y'+')'+'-104'+'Y'+')'+'-105'+'Y'+')'+'-106'+'Y'+')'+'-107'+'Y'+')'+'-108'+'Y'+')'+'-109'+'Y'+')'+'-110'+')'+'-111'+'Y'+')'+'-112'+'Y'+')'+'-113'+'Y'+')'+'-114'+'Y'+')'+'-115'+'Y'+')'+'-116'+'Y'+')'+'-117'+'Y'+')'+'-118'+'Y'+')'+'-119'+'Y'+')'+'-120'+')')
    return mov4

def mov5():
#Movimiento una ficha en la posicion 5 imnplica
    mov5 =str('('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'44'+'Y'+'47'+')'+'>'+'-1'+'Y'+')'+'-2'+'Y'+')'+'-3'+'Y'+')'+'-4'+'Y'+')'+'-5'+'Y'+')'+'-6'+'Y'+')'+'-7'+'Y'+')'+'-8'+'Y'+')'+'-9'+'Y'+')'+'-10'+')'+'-11'+'Y'+')'+'-12'+'Y'+')'+'-13'+'Y'+')'+'-14'+'Y'+')'+'-15'+'Y'+')'+'-16'+'Y'+')'+'-17'+'Y'+')'+'-18'+'Y'+')'+'-19'+'Y'+')'+'-20'+'Y'+')'+'-21'+'Y'+')'+'-22'+'Y'+')'+'-23'+'Y'+')'+'-24'+'Y'+')'+'-25'+'Y'+')'+'-26'+'Y'+')'+'-27'+'Y'+')'+'-28'+'Y'+')'+'-29'+'Y'+')'+'-30'+'Y'+')'+'-31'+'Y'+')'+'-32'+'Y'+')'+'-33'+'Y'+')'+'-34'+'Y'+')'+'-35'+'Y'+')'+'-36'+'Y'+')'+'-37'+'Y'+')'+'-38'+'Y'+')'+'-39'+'Y'+')'+'-40'+'Y'+')'+'-41'+'Y'+')'+'-42'+'Y'+')'+'-43'+'Y'+')'+'-44'+'Y'+')'+'-45'+'Y'+')'+'-46'+'Y'+')'+'-47'+'Y'+')'+'-48'+'Y'+')'+'-49'+'Y'+')'+'50'+'Y'+')'+'-51'+'Y'+')'+'-52'+'Y'+')'+'-53'+'Y'+')'+'-54'+'Y'+')'+'-55'+'Y'+')'+'-56'+'Y'+')'+'-57'+'Y'+')'+'-58'+'Y'+')'+'-59'+'Y'+')'+'-60'+'Y'+')'+'-61'+'Y'+')'+'-62'+'Y'+')'+'-63'+'Y'+')'+'-64'+'Y'+')'+'-65'+'Y'+')'+'-66'+'Y'+')'+'-67'+'Y'+'Y'+')'+'-68'+'Y'+')'+'-69'+'Y'+')'+'-70'+'Y'+')'+'-71'+'Y'+')'+'-72'+'Y'+')'+'-73'+'Y'+')'+'-74'+'Y'+')'+'-75'+'Y'+')'+'-76'+'Y'+')'+'-77'+'Y'+')'+'-78'+'Y'+')'+'-79'+'Y'+')'+'-80'+'Y'+')'+'-81'+'Y'+')'+'-82'+'Y'+')'+'-83'+'Y'+')'+'-84'+'Y'+')'+'-85'+'Y'+')'+'-86'+'Y'+')'+'-87'+'Y'+')'+'-88'+'Y'+')'+'-89'+'Y'+')'+'-90'+'Y'+')'+'-91'+'Y'+')'+'-92'+'Y'+')'+'-93'+'Y'+')'+'-94'+'Y'+')'+'-95'+'Y'+')'+'-96'+'Y'+')'+'-97'+'Y'+')'+'-98'+'Y'+')'+'-99'+'Y'+')'+'-100'+'Y'+')'+'-101'+'Y'+')'+'-102'+'Y'+')'+'-103'+'Y'+')'+'-104'+'Y'+')'+'-105'+'Y'+')'+'-106'+'Y'+')'+'-107'+'Y'+')'+'-108'+'Y'+')'+'-109'+'Y'+')'+'-110'+'Y'+')'+'-111'+'Y'+')'+'-112'+'Y'+')'+'-113'+'Y'+')'+'-114'+'Y'+')'+'-115'+'Y'+')'+'-116'+'Y'+')'+'-117'+'Y'+')'+'-118'+'Y'+')'+'-119'+'Y'+')'+'-120'+')')
    return mov5

def mov7():
#Movimiento una ficha en la posicion 7 imnplica
    mov7 =str('('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'7'+'>'+'-1'+'Y'+')'+'-2'+'Y'+')'+'-3'+'Y'+')'+'-4'+'Y'+')'+'5'+'Y'+')'+'-6'+'Y'+')'+'-7'+'Y'+')'+'-8'+'Y'+')'+'-9'+'Y'+')'+'-10'+')'+'O'+'('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'7'+'>'+'-1'+'Y'+')'+'-2'+'Y'+')'+'-3'+'Y'+')'+'-4'+'Y'+')'+'-5'+'Y'+')'+'-6'+'Y'+')'+'-7'+'Y'+')'+'8'+'Y'+')'+'-9'+'Y'+')'+'10'+')')
    return mov7

def mov8():
#Movimiento una ficha en la posicion 8 imnplica
    mov8 =str('('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'8'+'>'+'1'+'Y'+')'+'-2'+'Y'+')'+'3'+'Y'+')'+'-4'+'Y'+')'+'-5'+'Y'+')'+'-6'+'Y'+')'+'-7'+'Y'+')'+'-8'+'Y'+')'+'-9'+'Y'+')'+'-10'+')')
    return mov8

def mov9():
#Movimiento una ficha en la posicion 9 imnplica
    mov9 =str('('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'9'+'>'+'-1'+'Y'+')'+'-2'+'Y'+')'+'-3'+'Y'+')'+'4'+'Y'+')'+'-5'+'Y'+')'+'-6'+'Y'+')'+'-7'+'Y'+')'+'-8'+'Y'+')'+'-9'+'Y'+')'+'-10'+')')
    return mov9

def mov10():
#Movimiento una ficha en la posicion 2 imnplica
    mov10 =str('('+'('+'('+'('+'('+'('+'('+'('+'('+'('+'10'+'>'+'-1'+'Y'+')'+'-2'+'Y'')'+'-3'+'Y'+')'+'-4'+'Y'+')'+'-5'+'Y'+')'+'-6'+'Y'+')'+'7'+'Y'+')'+'-8'+'Y'+')'+'-9'+'Y'+')'+'-10'+')')
    return mov10

M = str('('+'('+'('+mov2()+')'+'Y'+')'+'('+mov5()+')'+'Y'+')'+'('+mov4()+')')
#print(M)
#regla3 traducida
regla3 = tra(M)

#print(regla3)
