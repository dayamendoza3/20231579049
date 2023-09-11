from data.data import * #se importa todos los modulos del file data
from BD.baseDatos import * #se importa todos los modulos del file base de datos
from sklearn.linear_model import LinearRegression #se importa especificamente la regresión lineal
from grafica.grafica import * #se importa todos los modulos del file graficas
import pandas as pd #se importa geopandas

#Datos del excel
dataTeoricoEsfuerzo, dataTeoricoDeformacion = dataTeorico() #se definen las variables de los datos del excel 

#Datos de la base de datos y realizamos el modelo
data_list = lecturaDatos() #se definen la lectura de los datos en un data_list
data_real = pd.DataFrame(data_list) #se convierten los datos contenidos en formato de DataFrame, lo que facilita la manipulación y el análisis de los datos
data_real_fit = data_real #se definen data real fit con data real
X = data_real_fit['Esfuerzo[kN]'].values.reshape(-1, 1) #se definen la variable x (Esfuerzo[kN]) y el rango a evaluar 
y = data_real_fit['Deformacion[mm]'].values.reshape(-1, 1) #se definen la variable y (Deformacion[mm]), tambien el rango a evaluar 
x_lim = data_real['Esfuerzo[kN]'].iloc[-1] #se define el limite de x (Esfuerzo[kN]), se utiliza iloc para acceder al último elemento de una serie de DataFrame
y_lim = data_real['Deformacion[mm]'].iloc[-1] #se define el limite de y (Deformacion[mm]), se utiliza iloc para acceder al último elemento de una serie de DataFrame
model = LinearRegression() #se define el modelo es una regreción lineal
model.fit(X, y) #se define las variables del modelo x y y
prediction = round(model.predict(np.array([3000]).reshape(-1, 1))[0][0],1) #se define la predicción en 3000 
print('la predicción a 1000 kN es de: ', prediction ,'mm') #Imprimimos el valor de la predicción en kn


dataRealEsfuerzo = data_real['Esfuerzo[kN]'] #se define las variable dataRealesfuerzo de la columna Esfuerzo[kN] de data real
dataRealDeformacion = data_real['Deformacion[mm]'] #se define las variable dataRealesfuerzo de la columna Deformacion[mm] de data real

#realizamos la lectura de las gráficas
gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion) #se selecciona los tres graficos respectivos que se generaron
gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion) #se grafica de predicción
gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model)#se grafica la predicción 3000
