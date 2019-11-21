import string

def codify(fil,cas):
    #fil maximo hay 4
    return((fil-1)*10)+cas

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
        fn=str('(' + '-'+'('+ l1 +','+ i1 +')'+rec(39,Ronda) + ')')
        fn1 = fn.replace(pr1,'')
        fn2 = fn1.replace("None",'')
        return pr+'>'+fn2

def final(i,Ronda,fichasT):

    if i<=fichasT:
        n1= str('('+str(list(i,Ronda,fichasT)))+')'+'Y'+str(final(i+1,Ronda+1,fichasT))
        return n1



l1=str(final(1,1,40))
l2= l1.replace('Y(None)','')
l2= l2.replace('YNone','')
#print(l2)
print(l2)
