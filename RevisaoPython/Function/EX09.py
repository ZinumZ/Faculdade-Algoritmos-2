def soma(a,b, imprime = False):
    s = a + b
    if imprime:
        print(s)
    return s    
soma(2,3, True) #Sem o True, não iria ser executado a função print(s)
print(soma(2,3)) 
