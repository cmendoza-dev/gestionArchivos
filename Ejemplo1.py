import pandas
import numpy as np
import pandas as pd

# Obtener la sumatoria de los valores de una determinada columna y/o campo
archivo = pd.read_csv('Panamericanos_Lima.csv')
def calculo_suma():
    print(archivo['Oro'].sum())
    print(archivo.Oro.sum())

#calculo_suma()

#Obtener el número de elementos
def calculo_elementos():
    print(archivo['Oro'].count())
    print(len(archivo['Oro']))
    print(len(archivo.Oro))

#calculo_elementos()

# Otener el número de elementos
def calculo_media():
    print(archivo['Oro'].sum()/archivo['Oro'].count())
    print(archivo['Oro'].mean())
#calculo_media()



def calculo_mediana():
    numero=np.size(archivo.Oro)
    posicion=round(numero/2)
    print('Posicion mediana: ', posicion)
    mediana = archivo.Oro[posicion-1]
    print(mediana)
    print(archivo['Oro'].median())
#calculo_mediana()


# Obtener la moda
def calculo_moda():
    print(archivo['Oro'].mode())
#calculo_moda()




