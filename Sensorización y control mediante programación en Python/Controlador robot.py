#on start controlador o mando
x = 0 #se declara la variable x, que hace referencia al acelerometro en la coordinada y del microbit en mano
basic.show_icon(IconNames.YES) #verificación del programa mediante la visualización en led del check (✔)
radio.set_group(27) #el valor de la frecuencia de radio es 27
radio.set_transmit_power(7) # la potencia de radio es la máxima con un valor de 7

def on_button_pressed_a(): #al presionar boton A
    radio.send_number(1) #enviar el numero 1 y mostrar led hacia la izq
    basic.show_leds("""
        . . # . .
        . # . . .
        # # # # #
        . # . . .
        . . # . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab(): #al presionar boton AB
    radio.send_number(5)  #enviar el numero 5 y mostrar led stop
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b(): #al presionar boton B
    radio.send_number(3)  #enviar el numero 3 y mostrar led hacia la der
    basic.show_leds("""
        . . # . .
        . . . # .
        # # # # #
        . . . # .
        . . # . .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global x #se utiliza la variable x definida de forma global
    x = input.acceleration(Dimension.Y) #X es igual a la entrada del acelerímetro en dirección Y
    if x < -500: #Si X es menor que -500mg, es el equivalente a un giro manual hacia delante del controlador
        radio.send_number(2) #se envia al robot el numero 2 por radio frecuencia
        basic.show_leds("""
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            """) #Se muestra por leds la acción de ir hacia delante en el mando
    elif x > 500: #Si X es mayor que 500mg
        radio.send_number(4)  #enviar el numero 4 y mostrar led hacia abajo
        basic.show_leds("""
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            """)
basic.forever(on_forever)
