#!/usr/bin/python
import pprint
import fnmatch
import os
from random import randint

import itertools

NUMERO_CIFRAS=6
debug=True
objetivo=100

dict_resultados = {}
elegibles_mapeados = [1, 2 ,3 ,4, 5 ,6 ,7 ,8, 9, 10,  25, 50 ,75, 100]
elegibles = [1, 2 ,3 ,4, 5 ,6 ,7 ,8, 9, "A", "B", "C", "D", "E",]
code = '123456'
operaciones = ['+', '-', '*' , '/']

my_list = []
#my_list=[9, 'C', 4, 3, 5, 8]

lookup_cifras = {
        "E": 100,
        "D": 75,
        "C": 50,
        "B": 25,
        "A": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
        "1": 1, }



def generate_numbers():
    # First cbuild array
    for i in range( 0, NUMERO_CIFRAS ):
        my_numero = randint(0,13)

        my_list.append(elegibles[my_numero])
        print elegibles_mapeados[my_numero]

    objetivo=randint(0,899)+100
    #objetivo=545

    print "Numero a conseguir"
    print objetivo
    print "Cifras"
    print my_list
    return objetivo

def calcular(A , operando  , B ):
    if operando == "+":
        resultado=(A + B)
    elif operando == "-":
        resultado=(A - B)
    elif operando == "*":
        resultado=(A * B)
    else:
        resultado=(A / B)

    return resultado

def mapear(ordinal):
    cifra_temporal=my_list[int(ordinal)-1]
    cifra_final=lookup_cifras[str(cifra_temporal)]
    return cifra_final

def chequear(subtotal, objetivo, cadena,dict_resultados):
    if( int(subtotal) == int(objetivo) ):
        if ( dict_resultados.has_key(cadena)):
            a=0
        else:
            dict_resultados[cadena] = 0
            print "Encontrado::::: " , cadena,objetivo
    else :
        a=0
        #print "Buscando", subtotal, objetivo, len(cadena)
    return

def cifras_calculate_stack( result,objetivo,dict_resultados):
    objetivo_parcial=1000
    cadena_claro=[mapear(result[0]),result[1] ,mapear(result[2]),result[3] ,mapear(result[4]),result[5] ,mapear(result[6]),result[7],mapear(result[8]),result[9],mapear(result[10] )]

    subtotal=calcular(mapear(result[0]),result[1] ,mapear(result[2]  ))
    chequear(subtotal,objetivo,str(cadena_claro[:3]),dict_resultados)
    subtotal=calcular(         subtotal,result[3] ,mapear(result[4]  ))
    chequear(subtotal,objetivo,str(cadena_claro[:5]),dict_resultados)
    subtotal=calcular(         subtotal,result[5] ,mapear(result[6]  ))
    chequear(subtotal,objetivo,str(cadena_claro[:7]),dict_resultados)
    subtotal=calcular(         subtotal,result[7],mapear(result[8] ))
    chequear(subtotal,objetivo,str(cadena_claro[:9]),dict_resultados)
    subtotal=calcular(         subtotal,result[9],mapear(result[10] ))
    chequear(subtotal,objetivo,str(cadena_claro),dict_resultados)

    return

def cifras_generate_stack( my_array,objetivo,dict_resultados):
    operandos = itertools.product('+-*/',repeat=(NUMERO_CIFRAS-1))

    y = list(itertools.islice(operandos,0,100000000,1))

    for j in y:
        result = [None]*(len(my_array) + len(j))
        result[0::2] = my_array
        result[1::2] =  j
        cifras_calculate_stack(result,objetivo,dict_resultados)

    return


if __name__ == '__main__':

    objetivo = generate_numbers()
    codigos = itertools.permutations(code,NUMERO_CIFRAS)
    x = list(itertools.islice(codigos,0,100000000,1))


    for i in x:
        cifras_generate_stack(i,objetivo,dict_resultados)



    print "Fin"
