# Escribir una función que dado el ingreso de 3 variables (a, b, c) 
# retorne las raíces resultantes de una ecuación cuadrática.

def raiz_cuadrada(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return "Error: Los valores de a, b y c deben ser números."
    
    # Calculamos el discriminante
    discriminante = b**2 - 4*a*c

    # Caso cuando hay dos soluciones reales
    if discriminante > 0:
        raiz1 = (-b + discriminante**0.5) / (2 * a)
        raiz2 = (-b - discriminante**0.5) / (2 * a)
        return f"Dos raíces reales: {raiz1} y {raiz2}"

    # Caso cuando hay una solución real
    elif discriminante == 0:
        raiz = -b / (2 * a)
        return f"Una raíz real: {raiz}"

    # Caso cuando hay soluciones complejas (discriminante negativo)
    else:
        parte_real = -b / (2 * a)
        parte_imaginaria = (-discriminante)**0.5 / (2 * a)
        return f"Raíces complejas: {parte_real} + {parte_imaginaria}i y {parte_real} - {parte_imaginaria}i"


print(raiz_cuadrada(1, -3, 2))   # Dos raíces reales: 2.0 y 1.0
print(raiz_cuadrada(1, 2, 1))    # Una raíz real: -1.0
print(raiz_cuadrada(1, 1, 1))    # Raíces complejas: -0.5 + 0.8660254037844386i y -0.5 - 0.8660254037844386i
print(raiz_cuadrada('a', 2, 3))  # Error: Los valores de a, b y c deben ser números.