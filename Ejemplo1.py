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

# Obtener la media redondeada a 2 decimales

# Obtener la media
def calculo_media():
    print(archivo['Oro'].sum() / archivo['Oro'].count())
    print(archivo['Oro'].mean())

#calculo_media()



# print("Obtener la media redondeada a 2 decimales: ", np.round(archivo['Oro'].mean(), 2))

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


def calculo_percentile25():
    print("Percentil 25: ",archivo['Oro'].quantile(0.25))
#calculo_percentile25()

def calculo_percentile50():
    print("Percentil 50: ",archivo['Oro'].quantile(0.5))
#calculo_percentile50()

def calculo_percentile75():
    print("Percentil 75: ",archivo['Oro'].quantile(0.75))
#calculo_percentile75()

def calculo_percentile90():
    print("Percentil 90: ",archivo['Oro'].quantile(0.9))
#calculo_percentile90()

#Obtener la varianza
def calculo_varianza():
    varP= archivo["Oro"].var(ddof=0)
    varM = archivo["Oro"].var(ddof=1)
    std = archivo["Oro"].std(ddof=0)
    print("Varianza poblacional:", varP)
    print("Varianza muestral:", varM)
    print()
    print("Desviación típica:", std)

calculo_varianza()