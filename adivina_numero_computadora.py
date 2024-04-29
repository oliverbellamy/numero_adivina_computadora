import random


def adivina_numero_computadora(x):
    
    print("=====================")
    print(" Bienvenido al juego!")
    print("=====================")
    print(f"Selecciona un numero entre 1 y {x} para que la computadora intente adivinarlo.")

    limite_inferior = 1
    limite_superior = x
    
    respuesta = ""
    while respuesta != "c":
        #Generar prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior #tambien podria ser el limite superior.

            #Obtener respuesta del usuario
        respuesta = input(f"Mi prediccion es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcto ingresa (C): ").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1

        #Intervalo inicial: [1, 10]
        #Prediccion: 6
        #Respuesta: "a"
        #Intervalo ahi lo achica para acercarse a lo que quiere el user, o sea obtenemos respuesta y segun lo que responde el user se achica o no el intervalo [1, 5]
        #si el user dice que la prediccion es muy baja se sube el intervalo y si dice que es muy alta se baja el intervalo para acercarse al valor que piensa el user.
        #si es muy alto cambiamos el limite superior y lo hacemos mas pequeno, y si es muy bajo cambiamos el limite inferior y lo hacemos mas alto. O sea si el numero que predecimos lo estamos diceindo muy alto hacemos que diga ese numero que predecimos menos uno, y si lo estamos diciendo muy bajo hacemos que diga ese numero que predecimos mas uno.


    print (f"Siii! La computadora adivino tu numero correctamente: {prediccion}.")


adivina_numero_computadora(10)