# coding=utf-8
# Ejercicio Python
# Estudiante: Lina Ochoa-Venegas

'''
 Función encargada de hacer el cálculo de la serie Fibonacci
 dado un número entero de iteraciones.
    Pre: el usuario ha definido un número entero mayor a 0 de iteraciones
    Post: se calcula la serie Fibonacci dado el número de iteraciones y se retorna la lista
'''
def calcularFibonacci(iteraciones):
    fibonacci = [1]
    fibonacciString = "1"
    actual = 1

    while actual < iteraciones or actual == 10:
        if actual == 1:
            fibonacci.insert(actual, fibonacci[actual - 1] * 2)
        else:
            fibonacci.insert(actual, fibonacci[actual - 1] + fibonacci[actual - 2])

        fibonacciString += ", " + fibonacci[actual].__str__()
        actual += 1

    return fibonacciString

'''
 Función encargada de solicitar el número de iteraciones para la serie Fibonacci,
 y de validar y entregar el parámetro al método calcularFibonacci().
    Post: Se informa al usuario de posible erro introducido o se devuelve la serie Fibonacci
    por consola.
'''
def main():
    while True:
        try:
            iteraciones = int(raw_input("Por favor, ingrese el número de iteraciones Fibonacci: "))

            if iteraciones == 0:
                 print "Debe ingresar un número entero mayor a cero para visualizar la serie. Inténtelo de nuevo."
                 continue

            print "Serie Fibonacci: " + calcularFibonacci(iteraciones)
            break
        except ValueError:
            print "Debe ingresar un número entero válido. Inténtelo de nuevo."


# Invocación al método main()
main()