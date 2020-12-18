# Fabricación de ROBOT de TELEPRESENCIA
## Proyecto Final del curso de Tecnologías Industriales
*Master Universitario en Digital Manufacturing*

Desarrollado por:
* Nekane Berasategui
* Goiatz Ezpeleta
* Laura Zambrano


Contenido:
1. Sensorización y control mediante programación en Python
2. CAD y prototipado 3D
3. Programación de línea de packaging con Factory IO
4. Visualización de los datos ambientales con Tableu

## 1. Sensorización y control mediante programación en Python
Se ha programado la funcionalidad y control del robot en Python en la plataforma https://makecode.microbit.org/#editor y utilizando el módulo de gigglebot. Para esta actividad se ha basado en la documentación de Microbit disponible en https://microbit.org/projects/make-it-code-it/

![Extension Gigglebot](/img/ext_giggle.PNG)

Nuestro equipo propone el control remoto del robot mediante otra tarjeta microbit, por tanto se incluye el código de dos microbit: uno referente al controlador (tarjeta en mano) y otro al código del gigglebot.

La letra A indica movimiento a la derecha, B hacia la izquierda y AB hacia delante. Adicionalmente se incluyen luces, flechas y caras en las distintas funcionalidades del robot.

| Acción        | Dirección     | Color   |
|:-------------:|:-------------:|:-------:|
| A             | ←             | Azul    |
| B             | →             | Verde   |                                        
| Y<-500        | ↑             | Blanco  |                                         
| Y>+500        | ↓             | Amarillo|                                         
|    AB         | X             | Rojo    |                                                                                  
                                                                                 

![A](/img/izq.PNG)
![AB](/img/arriba.PNG)
![B](/img/der.PNG)

Se ha agregado el sensor de proximidad con su respectivo código en Arduino para la detección de objetos que pueden ser un obstáculo para el robot y funciones para esquilarlos. Esto se complementa con la propuesta de modelado 3D en el siguiente apartado.
También se ha programado la detección de líneas negras como indicador de finalización de un camino.


## 2. CAD y prototipado 3D
## 3. Programación de línea de packaging con Factory IO

### Clasificador de cajas por tamaño
### Elementos del programa
El programa consta de diferentes elementos para su uso. Estos elementos se clasifican entre sensores (input), actuadores (output), memorias y bloques funcionales lógicos.
Los inputs, outputs y las memorias tienen cada uno un nombre y un número de pin.

#### Inputs
Los inputs son los elementos que se muestran en color verde en el esquema. Los sensores que encontramos en el programa son los siguientes:
* (5) High sensor: Sensor que detecta las cajas grandes 
* (6) Low sensor: Este sensor detecta tanto las cajas grandes como las pequeñas
* (7) Pallet sensor: Sensor que detecta los pallets

![Sensores de detección de altura](/img/1.png)

*	(8) At left entry:	 Detecta cuando una caja sale hacia la cinta izquierda
*	(12) At right entry: Detecta cuando una caja sale hacia la cinta derecha
*	(16) Loaded: Detecta cuando un pallet está cargado correctamente en la unidad de transferencia

![Sensores del transfer](/img/2.png)

*	(11) At left exit: Detecta cuando una caja ha salido de la cinta izquierda
*	(10) At right exit: Detecta cuando una caja ha salido de la cinta derecha

## 4. Visualización de los datos ambientales con Tableu 
Mediante la plataforma Tableau se han visualizado varias gráficas relacionadas con datos de clima recogidos en Elgoibar durante los años 2016 y 2017. 

[![IMAGEN TABLEAU](/img/tableau.PNG)](https://public.tableau.com/views/dashboard_16082122007840/Dashboard1?:showVizHome=no#2)

Los parámetros que se han medido durante este periodo son los siguientes:

* Fecha de captura
* Calidad del Aire (cualitativo)
* Índice de Calidad del Aire (cuantitativo)
* CO2 (ug/m3)
* Humedad Rh (%)
* Temperatura (ºC)
* Grado de partículas suspendidas en el aire de diámetro 2.5 micras o inferior. (cualitativo)
* Número de partículas suspendidas en el aire de diámetro 2.5 micras o inferior. PM 2.5 (cuantitativo)


Análisis de las gráficas publicadas: 
### CALIDAD DEL AIRE
La calidad del aire se mide según 4 contaminantes perjudiciales tanto para la salud de las personas como para el mediambiente:
* Ozono troposférico (O3)
* Dióxido de nitrógeno (NO2)
* Dióxido de azufre (SO2)
* Partículas en suspensión (PM 2,5 y PM10)

#### Valoración de la Calidad del aire. 
Se han relacionado datos cuantitativos y cualitativos para que de manera visual se aprecie el grado de la calidad del aire

![](/img/calidad_aire.PNG)

#### Relación de la calidad del aire y la carga de partículas PM2.5
Las partículas que se encuentran en suspensión en el aire se miden según dos tamaños: PM2.5 y PM10. Las PM 2.5 tienen un diámetro igual o menor a 2.5 micras y las PM10 un diámetro igual o inferior a 10 micrómetros. En el análisis llevado a cabo en este proyecto, únicamente se tienen datos de PM2.5
En la siguiente gráfica se percibe la clara relación entre la carga de partículas y la calidad del aire PM2.5. 


![](/img/HOJA_10.PNG)

### Valores promedio de Temperatura (ºC), Humedad (%Rh) y CO2 (ug/m3)
La gráfica que se ve a continuación se ha creado para la consulta de los tres parámetros anteriormente mencionados entre los años los años 2016 y 2017.

![](/img/HOJA_9.PNG)
