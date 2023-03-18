from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-","*","/"]
cont = 0
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    result = float(input("resultado: "))
    if operator == "+":
        result2 = number_1 + number_2
    elif operator == "-":
        result2 = number_1 - number_2
    elif operator == "*":
        result2 = number_1 * number_2
    elif operator == "/" and number_2 == 0:
        print(f"Casi... pensaste que iba a dividir por cero!!!"
              " para seguir la diversion busquemos otro denominador.")
        number_2 = randrange(1,9)
        print(f"¿Cuánto es {number_1} {operator} {number_2}?")
        result = float(input("resultado: "))
        result2 = number_1 / (number_2) 
    else :
        result2 = number_1 / number_2

    if result == result2 :
        print(f"uste posee la verdad")
        cont = cont + 1
    else :
        print(f"la verdad es {result2}")
    # Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos y tuviste {cont} verdades universales")
