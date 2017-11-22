'''
Created on 21/11/2017

@author: 
XXX: https://code.google.com/codejam/contest/90101/dashboard#s=p2
'''
import logging
from _collections import defaultdict
import sys

nivel_log = logging.ERROR
nivel_log = logging.DEBUG
logger_cagada = None

def puta_mierda(arre):
    return '\n'.join([''.join(['{},'.format(item) for item in row]) for row in arre])

# XXX: https://www.accelebrate.com/blog/using-defaultdict-python/
def bienvenida_culera_genera_posiciones_letras(cadena):
    posiciones = defaultdict(list)
    for pos, letra in enumerate(cadena):
        posiciones[letra].append(pos)
    
    return posiciones

def bienvenida_culera_core(cadenota, cadenita):
    cadenota_tam = len(cadenota)
    cadenita_tam = len(cadenita)
    
    posiciones_cadenita = bienvenida_culera_genera_posiciones_letras(cadenita)
    posiciones_cadenota = bienvenida_culera_genera_posiciones_letras(cadenota)
    
#    logger_cagada.debug("laspos  de cadenita {}".format(posiciones_cadenita))
#    logger_cagada.debug("laspos  de cadenota {}".format(posiciones_cadenota))
    
    matrix_conteo = []
    for _ in range(cadenita_tam):
        matrix_conteo.append([0] * cadenota_tam)
    
    for posicion_primera_letra in posiciones_cadenota[cadenita[0]]:
        matrix_conteo[0][posicion_primera_letra] = 1
    
    for i in range(1, cadenota_tam):
        num_act = matrix_conteo[0][i]
        matrix_conteo[0][i] = matrix_conteo[0][i - 1]
        if(num_act):
            matrix_conteo[0][i] += 1
    
    for posicion_letra_cadenota, letra_cadenota in enumerate(cadenota[1:], 1):
        for posicion_letra_cadenita, letra_cadenita in enumerate(cadenita[1:], 1):
            matrix_conteo[posicion_letra_cadenita][posicion_letra_cadenota] = matrix_conteo[posicion_letra_cadenita][posicion_letra_cadenota - 1] 
            if(letra_cadenita == letra_cadenota):
                matrix_conteo[posicion_letra_cadenita][posicion_letra_cadenota] += matrix_conteo[posicion_letra_cadenita - 1][posicion_letra_cadenota - 1]
    
#    logger_cagada.debug("la matrxi cont\n{}".format(puta_mierda(matrix_conteo)))
    return matrix_conteo[-1][-1]
    

def bienvenida_culera_main():
    lineas = list(sys.stdin)
    cadenita = "welcome to code jam"
    
    for cagada, linea in enumerate(lineas[1:], 1):
        cadenota = linea.strip()
        caca = bienvenida_culera_core(cadenota, cadenita)
        print("Case #{}: {:04d}".format(cagada, caca % 10000))
        

if __name__ == '__main__':
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
        logging.basicConfig(level=nivel_log, format=FORMAT)
        logger_cagada = logging.getLogger("asa")
        logger_cagada.setLevel(nivel_log)
        bienvenida_culera_main()
