import pandas as pd #se importa pandas

# Importar datos del csv
data_teorico = pd.read_csv(r"D:\TEC. CIVILES U. DISTRITAL\Ingenieria civil\Semestre 2\Programacion II\actividad_4-main\data\Data ingeniero.csv") #se carga los datos desde el archivo csv en la variable data_teorico

#Código general
""" En caso que se exigiera realizar la limpieza de la data se haría aca"""

def dataTeorico(): #se define el dataTeorico 
    dataTeoricoEsfuerzo = data_teorico['Esfuerzo[kN]'] #se le asigna a  la variable dataTeoricoEsfuerzo la columna de esfuerzo
    dataTeoricoDeformacion = data_teorico['Deformacion[mm]'] #se le asigna a  la variable dataTeoricoDeformacion la columna de deformacion
    return dataTeoricoEsfuerzo, dataTeoricoDeformacion #se retornan los datos establecidos anteriormente


