#!/usr/bin/python
import pprint
import fnmatch
import os
import random
import string
import itertools

NUMERO_LETRAS=9
debug=True
objetivo=100

dict_resultados = {}

my_list = []

def load_palabras(full_list):
    with open("/Users/jaimevalerodebernabe/git/cifras_y_letras/letras.txt") as f:
        for line in f:
            key = line.split()
            longitud = (len(str(line))-1)
            if ((longitud < 4) or (longitud > 9)) :
                a=0
                #print " skip:", line, longitud
            else:
                full_list[line] = longitud
                #print line,longitud
    full_list

def generate_letters():

    for i in range( NUMERO_LETRAS ):
        my_list.append(random.choice(string.ascii_lowercase))

    print "Letras:", my_list
    return my_list


if __name__ == '__main__':

    full_list = {}
    load_palabras(full_list )


    letras_concursante = {}
    letras_concursante = generate_letters()

    a='comer'
    #print "Pepe", dict_resultados[a]

    #codigos = itertools.permutations(letras_concursante,NUMERO_CIFRAS)

    #codigo=str(letras_concursante)
    #print "Letras",letras_concursante
#NUMERO_LETRAS
    codigos = itertools.permutations(letras_concursante,6)
    x = list(itertools.islice(codigos,0,100000000,1))
    #exit
    #for range (9:4)
    for i in x:
        if letras_concursante.has_key(''.join(i)):
            print 'encontrado', ''.join(i)

        print ''.join(i)
        #cifras_generate_stack(i,objetivo,dict_resultados)



    print "Fin"
