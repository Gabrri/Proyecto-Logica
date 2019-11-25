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
    print('((((((((('+C1+'Y'+C2+')Y'+C3+')Y'+C4+')Y'+C5+')Y'+C6+')Y'+C7+')Y'+C8+')Y'+C9+')Y'+C10+')')
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





#regla 1 donde se pone la prelacion del tiempo1
print('((((('+l4+')'+'((('+n4+'))'+'((('+k4+'))')

#regla 2 donde no puede haber dos fichas en una misma casilla
#regla2()
