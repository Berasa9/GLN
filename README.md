# Fabricación de ROBOT de TELEPRESENCIA
## Proyecto Final del curso de Tecnologías Industriales
*Master Universitario en Digital Manufacturing*

Desarrollado por:
* Goiatz Ezpeleta
* Nekane Berasategui
* Laura Zambrano


Contenido:
1. Sensorización y control mediante programación en Python
2. CAD y prototipado 3D
3. Programación de línea de packaging con Factory IO
4. Visualización de los datos ambientales con Tableu

## 1. Sensorización y control mediante programación en Python
Se programó la funcionalidad y control del robot en Python en la plataforma https://makecode.microbit.org/#editor y utilizando el módulo de gigglebot. Para esta actividad se basó en la documentación de Microbit disponible en https://microbit.org/projects/make-it-code-it/

![Extension Gigglebot](/img/ext_giggle.PNG)

Nuestro equipo propuso el manejo remoto del robot mediante otra tarjeta microbit, por tanto se incluye el código de dos microbit. Uno referente al controlador (tarjeta en mano) y otro al código del gigglebot.

La letra A indica que se mueva a la derecha, B hacia la izquierda y AB hacia delante. Adicionalmente se incluyen luces, flechas y caritas en las distintas funcionalidades del robot.

![B](/img/der.PNG)

Se agregó el sensor de proximidad, con su respectivo código en Arduino para la detección de objetos que pueden ser un obstáculo para el robot y funciones para esquilarlos. Esto se complementa con la propuesta de modelado 3D en el siguiente apartado.
También se programó la detección de líneas negras como indicador de finalización de un camino.


## 2. CAD y prototipado 3D
## 3.

# Clasificador de cajas por tamaño
## Elementos del programa
El programa utiliza diferentes elementos para poder funcionar. Estos elementos se clasifican entre sensores (input), actuadores (output), memorias y bloques funcionales lógicos.
Los inputs, outputs y las memorias tienen cada uno un nombre y un número de pin.
### Inputs
Los inputs son los elementos que se muestran en color verde en el esquema. Los sensores que encontramos en el programa son los siguientes:
* (5) High sensor: Sensor que detecta las cajas grandes 
* (6) Low sensor: Este sensor detecta tanto las cajas grandes como las pequeñas
* (7) Pallet sensor: Sensor qie detecta los pallets

![Sensores de detección de altura](/img/1.png)

*	(8) At left entry:	 Detecta cuando una caja sale por hacia cinta izquierda
*	(12) At right entry: Detecta cuando una caja sale hacia la cinta derecha
*	(16) Loaded: Detecta cuando un pallet está cargado correctamente en la unidad de transferencia

![Sensores del transfer](/img/2.png)

*	(11) At left exit: Detecta cuando una caja ha salido de la cinta izquierda
*	(10) At right exit: Detecta cuando una caja ha salido de la cinta derecha
