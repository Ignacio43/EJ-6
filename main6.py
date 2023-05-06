import funciones6



if __name__=='__main__':
    p=[]
    p=listadeviajeros()
   
    
    max_millas=max(p)
    print(f"el mayor numero de millas acumuladas de una persona es de {max_millas} \n")
    
    v1=p[0]
    v2= v1 + 100
    print(f"el numero de millas acumuladas es de {v2.cantidadTotalMillas()} \n")
        
    v3=p[1]
    v4= v3 - 100
    if v4:
        print(f"el numero de millas despues del canje es de {v4.cantidadTotalMillas()} \n")