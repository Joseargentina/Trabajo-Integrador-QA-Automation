# Escribir un programa que dado el ingreso de un número retorne si el mismo es primo o no.

def es_primo():
    try:
      n = int(input("Ingresa un número entero: "))
      
      if n <= 1:
        return "Por favor, ingresa un número entero mayor que 1."
      for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return f"{n} no es un número primo."
      return f"{n} es un número primo."
    except ValueError:
        return "Por favor, ingresa un número entero válido."

print(es_primo())
