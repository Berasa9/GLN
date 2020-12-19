# se define que el numero recibido sera igual a x
def on_received_number_deprecated(receivedNumber):
    global x
    x = receivedNumber
radio.on_received_number_deprecated(on_received_number_deprecated)

x = 0 # Se crea e inicializa x
basic.show_icon(IconNames.HAPPY) # se muestra una carita feliz para verificar la instalacion del codigo
radio.set_group(27) # se define la frecuencia de radio 27, igual que el controlador
x = 0

def on_forever():
    if x == 1: #si se recibe 1, girar a la izq, y mostrar leds
        basic.show_leds("""
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            """)
        gigglebot.turn(gigglebotWhichTurnDirection.RIGHT)
        lights.smile_show(NeoPixelColors.BLUE)
    elif x == 3: #si se recibe 3, girar a la der, y mostrar leds
        basic.show_leds("""
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            """)
        gigglebot.turn(gigglebotWhichTurnDirection.RIGHT)
        lights.smile_show(NeoPixelColors.GREEN)
    elif x == 2: #si se recibe 2, se mueve hacia adelante, y mostrar leds
        basic.show_leds("""
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            """)
        gigglebot.drive_straight(gigglebotWhichDriveDirection.FORWARD)
        lights.smile_show(NeoPixelColors.WHITE)
    elif x == 4: #si se recibe 4, se mueve hacia atras, y mostrar leds
        basic.show_leds("""
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            """)
        gigglebot.drive_straight(gigglebotWhichDriveDirection.BACKWARD)
        lights.smile_show(NeoPixelColors.YELLOW)
    elif x == 5: #si se recibe 5, se detiene y mostrar leds
        gigglebot.stop()
        basic.show_icon(IconNames.NO)
        lights.smile_show(NeoPixelColors.RED)
    #Detección de obstáculos, si hay un objeto cerca de 50 mm
    if gigglebot.distance_sensor_test_for_obstacle(gigglebotInequality.CLOSER, 50):
        gigglebot.stop() # se detiene el robot
        basic.show_icon(IconNames.NO) #mostrar en pantalla "X"
        lights.smile_show(NeoPixelColors.RED) #mostrar leds rojos
        basic.pause(1000) # esperar 1 segundo
        gigglebot.turn_millisec(gigglebotWhichTurnDirection.RIGHT, 1000) # y girar a la derecha
    #Detección de linea negra
    if gigglebot.line_test(gigglebotLineColor.BLACK):
        gigglebot.stop() #se detiene el robot
        basic.show_icon(IconNames.NO) # mostrar en pantalla "x"
        lights.smile_show(NeoPixelColors.RED) #mostar leds rojos
basic.forever(on_forever)