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
        #+'('+str(list(b,Ronda,fichasT)))+')'+'Y'+'('+str(list(c,Ronda,fichasT)))+')'+'Y'+'('+str(list(d,Ronda,fichasT)))+')')
        return n1+n2+n3+n4



l1=str(final(1,40))
l2= l1.replace('Y(None)','')
l2= l2.replace('YNone','')
l2=('('+l2.replace('))))',')))'))
#print(l2)
print(l2)
