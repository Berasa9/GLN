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

## 2. CAD y prototipado 3D

# Clasificador de cajas por tamaño
## Elementos del programa
El programa utiliza diferentes elementos para poder funcionar. Estos elementos se clasifican entre sensores (input), actuadores (output), memorias y bloques funcionales lógicos.
Los inputs, outputs y las memorias tienen cada uno un nombre y un número de pin.
### Inputs
Los inputs son los elementos que se muestran en color verde en el esquema. Los sensores que encontramos en el programa son los siguientes:
* (5) High sensor: Sensor que detecta las cajas grandes 
* (6) Low sensor: Este sensor detecta tanto las cajas grandes como las pequeñas
* (7) Pallet sensor: Sensor qie detecta los pallets
