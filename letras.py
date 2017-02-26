#!/usr/bin/python
import pprint
import fnmatch
import os
import itertools
import random
import string
from random import randint

print "Inicio"
NUMERO_LETRAS=9
dict_resultados = {}

my_list = []



def load_palabras(full_list):
    with open("/Users/jaimevalero/git/cifras_y_letras/letras.txt") as f:
        for line in f:
            key = line.split()
            longitud = (len(str(key)[2:-2]))
            if ((longitud < 4) or (longitud > 9)) :
                a=0
                #print " skip:", line, longitud
            else:
                full_list[str(key)[2:-2]] = longitud
                #print line,longitud
    return

def generate_letters():
    vocales = ['a','e','i','o','a','e','i','o','u']
    for i in range( NUMERO_LETRAS ):
        vocal_o_consonante = randint(1,10)
        if (vocal_o_consonante > 7 ):
            vocal = randint(0,8)
            my_list.append(vocales[vocal])
        else:
            my_list.append(random.choice(string.ascii_lowercase))

    print "Letras:", my_list
    return my_list


if __name__ == '__main__':

    letras_concursante = {}
    max_longitud=0

    letras_concursante = generate_letters()

    full_list = resultados = {}
    load_palabras(full_list )




    for i in range(9,3,-1):
        if (max_longitud > 0) :
            break
        print "Buscando palabras de: " , i
        codigos = itertools.permutations(letras_concursante,i)
        x = list(itertools.islice(codigos,0,100000000,1))

        mejor_resultado=0
        for j in x:
            candidato = ''.join(j)
            #print "kk4", candidato, str(candidato)
            #full_list[candidato] = 99

            if ( str(candidato) in full_list ) :
                if ( resultados[(candidato)] != 1 ) :
                    print 'encontrado', candidato
                    resultados[(candidato)] = 1
                    max_longitud=1



    print "Fin"
