# Ejercicio integrador

## Punto 1:

Escribir un programa que dado el ingreso de un número retorne si el mismo es primo o no.

## Punto 2:

Escribir una función que dado el ingreso de 3 variables (a, b, c) retorne las raíces resultantes de una ecuación cuadrática.

![][image1]

## Punto 3: 

Automatizar los siguientes casos de prueba. Luego de que sean automatizados, deben ser subidos a un repositorio git, se debe generar el archivo para que se ejecute en CI y debe retornar un reporte HTML con los resultados de la ejecución.

Sitio: [https://www.saucedemo.com/](https://www.saucedemo.com/)

Caso 1

* El usuario se loguea al sitio como usuario standard user  
* Ordenar los elementos por “price (low to high)”  
* Verificar que los elementos estén ordenados

Caso 2

* El usuario se loguea al sitio como usuario standard user  
* Incorporar al carrito todos los elementos  
* Ir al carrito  
* Verificar que todos los elementos están en el carrito  
* Ir al checkout  
* Ingresar nombre y clickear Continue  
* Verificar que aparece el error “**Error: Last Name is required”**  
* Ingresar un apellido y clickear Continue  
* Verificar que aparece el error “**Error: Postal Code is required”**

Caso 3

* El usuario se loguea al sitio como usuario standard user  
* Agregar un elemento al carrito  
* Ir al carrito  
* Remover el artículo  
* Verificar que el sitio no tiene artículos agregados  
* Ir a Continue Shopping  
* Agregar dos elementos  
* Ir al carrito  
* Verificar que los elementos existen  
* Hacer el checkout  
* Finalizar la compra  
* Verificar que la compra fue realizada

Sitio: Poke Api ([https://pokeapi.co/api/v2](https://pokeapi.co/api/v2))

Caso 1

* Hacer un get a berry/1  
* Verificar que el size sea 20  
* Verificar que el soil\_dryness sea 15  
* Verificar que en firmness, el name sea soft.

Caso 2

* Hacer un get a berry/2  
* Verificar que en firmness, el name sea super-hard  
* Verificar que el size sea mayor al del punto anterior  
* Verificar que el soil\_dryness sea igual al del punto anterior

Caso 3

* Hacer un get a pikachu ([https://pokeapi.co/api/v2/pokemon/pikachu/](https://pokeapi.co/api/v2/pokemon/pikachu/))  
* Verificar que su experiencia base es mayor a 10 y menor a 1000  
* Verificar que su tipo es “electric”