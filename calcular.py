
def calcula_raiz(numero):
    for i in range(0,numero+1):
        if i * i == numero:
            return f"A raiz do número {numero} é {i}!"
            break
        if i*i > numero:
            return "Esse número não tem raiz exata!"  
            break


    
