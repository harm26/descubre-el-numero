'''

Juguemos al juego de adivinar el numero, generaremos un número entre 1 y 100.
Nuestro objetivo es adivinar el número. Si fallamos nos dirán si es mayor o menor
que el número buscado.
'''

numero_a_adivinar=23
mi_numero = int(input("digite un numero--->"))


if mi_numero==numero_a_adivinar:
    print("felicidades, haz ganado")

else:

    while mi_numero>numero_a_adivinar:
        print("el numero digitado es mayor")
        mi_numero = int(input("digite un numero--->"))
        if mi_numero == numero_a_adivinar:
            print("felicidades, haz ganado")


    if mi_numero<numero_a_adivinar:
            print("el numero digitado es menor")
            mi_numero = int(input("digite un numero--->"))
            if mi_numero == numero_a_adivinar:
                print("felicidades, haz ganado")
