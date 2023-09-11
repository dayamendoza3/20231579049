import matplotlib.pyplot as plt #se importa la libreria matplot
import numpy as np #se importa la libreria numpy



def gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion): #se toman varios valores con el propósito de realizar una predicion, gráfico que involucra datos teóricos y datos reales de esfuerzo y deformación.
    
    
    plt.figure(figsize=(15, 6)) #se definen los tamaños de la figura
    plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) #se crea el grafico con las variables  de esfuerzo y deformación
    plt.scatter(	dataRealEsfuerzo, dataRealDeformacion, color='red') #se un grafico de dispersión con las variables de dataRealEsfuerzo, dataRealDeformacion y se especifica que tenga el color rojo
    plt.xlabel('Esfuerzo [kN]') #se define el eje x como el esfuerzo kN
    plt.ylabel('Deformación [mm]') #Se define el eje y como la deformación mm
    plt.title('Gráfica 2: teórico versus real [ZOOM]') #se define el titulo del grafico 
    plt.xlim(0, x_lim) #se define el rango de los valores del esfuerzo kN que es x
    plt.ylim(0, y_lim) #se define el rango de los valores de la deformación mm que es y
    plt.grid() #se define la grilla del fondo del grafico
    plt.gca().invert_yaxis() #se invierten los valores del eje y, se presentan de manera descendente 
    plt.show() #se visualiza el gráfico 

def gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model): #se toman varios valores con el propósito de realizar una predicion, gráfico que involucra predicion anterior, datos teóricos y datos reales de esfuerzo y deformación.
    
  plt.figure(figsize=(15, 6)) #Definimos los tamaños de la figura
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) #se crea el grafico con las variables  de esfuerzo y deformación
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red') #se un grafico de dispersión con las variables de dataRealEsfuerzo, dataRealDeformacion y se especifica que tenga el color rojo
  plt.plot(np.linspace(0,1000).reshape(-1,1),model.predict(np.linspace(0,1000).reshape(-1,1)),'m') #se traza una línea o curva de predicciones del modelo sobre un rango de valores en el eje x
  plt.scatter(	3000 , prediction, color='green') #se crea un grafico de dispersión en las coordenadas establecidas y se representa la predicción en color verde
  plt.xlabel('Esfuerzo [kN]') #se define el rango de los valores del esfuerzo kN que es x
  plt.ylabel('Deformación [mm]') #se define el rango de los valores de la deformación mm que es y
  plt.title('Gráfica 3: Predicción a una carga de 3000 kN') #se define el titulo del grafico 
  plt.xlim(0, 3000) #se define el rango de los valores del esfuerzo que es x
  plt.ylim(0, 45) #se define el rango de los valores de la deformación que es y
  plt.grid() #se define la grilla del fondo del grafico
  plt.gca().invert_yaxis() #se invierten los valores del eje se prensentan de manera descendente
  plt.show() #se visualiza el gráfico

def gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion): #se define el grafico de comparación teorico vs real
  plt.figure(figsize=(15, 6)) #se definen los tamaños de la figura
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) #se define las variables del grafico
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red') #se crea un grafico de dispersión y especificamos el color rojo
  plt.xlabel('Esfuerzo [kN]') #se define el eje x como el esfuerzo  kN que es x
  plt.ylabel('Deformación [mm]') #se define el rango de los valores de la deformación mm que es y
  plt.title('Gráfica 1: teórico versus real') #se define el titulo del grafico
  plt.grid() #se define la grilla del fondo del grafico
  plt.gca().invert_yaxis() #se invierten los valores del eje se prensentan de manera descendente
  plt.show() #se visualiza el gráfico