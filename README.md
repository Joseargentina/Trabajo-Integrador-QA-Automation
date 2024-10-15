# Trabajo Integrador QA Automation Selenium & PokeAPI

El proyecto consiste en la automatización de pruebas para a la plataforma [SauceDemo](https://www.saucedemo.com/) utilizando Selenium y pruebas unitarias para la API [PokeApi](https://pokeapi.co/) utilizando la librería `unittest` de Python. El proyecto también está integrado con Github Actions para ejecutar las pruebas en un entorno de integración continua (CI).

## Estructura del proyecto

- **.github\workflows\main.yml/**: contiene la configuración del flujo de trabajo de GitHub Actions.
- **pruebas_sauce_demo/**: Contiene los scripts de prueba automatizados con Selenium para la plataforma.
- **pruebas_poke_api/**: Contiene los scripts de pruebas unitarias para realizar solicitudes a la PokeApi y validar las respuestas.
- **html_runner.py**: Genera un reporte HTML de las pruebas ejecutadas. 
- **punto_1.py**: contiene la resolucion del punto 1
- **punto_2.py**: contiene la resolucion del punto 2

### Requisitos previos

- **Python 3.12**: Asegúrate de usar Python 3.12 o una versión superior.
- **Navegador Firefox**: Para las pruebas de SauceDemo, asegúrate de tener instalado el navegador Firefox.

## Instalación de dependencias:

Ejecuta el siguiente comando para instalar todas las dependencias necesarias:
```bash
pip install selenium requests python-dotenv html-testRunner
```

### Variables de entorno

Debes configurar las variables de entorno necessarias en un archivo `.env`. Un ejemplo de como debería verse tu archivo:

```env
NAME_USER=standard_user
BASE_URL=https://www.saucedemo.com/
PASSWORD=secret_sauce

BASE_URL_API=https://pokeapi.co/api/v2/
```

## Ejecución de pruebas

El proyecto incluye pruebas automatizadas para la plataforma SauceDemo (usando Selenium) y para la API PokeApi (usando Requests). Ambas se ejecutan mediante el mismo archivo `html_runner.py`.

### Casos de prueba de SauceDemo

Las pruebas de SauceDemo cubren los siguientes casos:

**Caso 1: Ordenación de elementos**
- El usuario se loguea al sitio como usuario standard user  
- Ordenar los elementos por “price (low to high)”  
- Verificar que los elementos estén ordenados

**Caso 2: Verificación de carrito y manejo de errores**
- El usuario se loguea al sitio como usuario **standard_user**.
- Se incorporan todos los elementos al carrito.
- Se verifica que todos los elementos están presentes en el carrito.
- Se procede al checkout e ingresa un nombre, luego se hace clic en **Continue**.
- Se verifica que aparece el error "**Error: Last Name is required**".
- Se ingresa un apellido y se hace clic en **Continue**.
- Se verifica que aparece el error "**Error: Postal Code is required**".

**Caso 3: Manejo del carrito y finalización de compra**
- El usuario se loguea al sitio como usuario **standard_user**.
- Se agrega un elemento al carrito.
- Se accede al carrito y se remueve el artículo.
- Se verifica que el carrito esté vacío.
- Se hace clic en **Continue Shopping** y se agregan dos elementos.
- Se verifica que los elementos existen en el carrito.
- Se procede al checkout y se finaliza la compra.
- Se verifica que la compra fue realizada exitosamente.

### Casos de prueba de la API PokeApi

Las pruebas de la API PokeApi cubren los siguientes casos:

**Caso 1: Verificación de Berry 1**
- Hacer un GET a `berry/1`.
- Verificar que el **size** sea 20.
- Verificar que el **soil_dryness** sea 15.
- Verificar que en **firmness**, el **name** sea **soft**.

**Caso 2: Verificación de Berry 2**
- Hacer un GET a `berry/2`.
- Verificar que en **firmness**, el **name** sea **super-hard**.
- Verificar que el **size** sea mayor al del punto anterior.
- Verificar que el **soil_dryness** sea igual al del punto anterior.

**Caso 3: Verificación de Pikachu**
- Hacer un GET a `https://pokeapi.co/api/v2/pokemon/pikachu/`.
- Verificar que su **experiencia base** sea mayor a 10 y menor a 1000.
- Verificar que su **tipo** sea **electric**.

Para ejecutar las pruebas, usa el siguiente comando:

```bash
python html_runner.py
```

Este comando ejecutará ambas pruebas y generará una carpeta llamada `report_directory/` dentro de esta carpeta, se crearán dos subcarpetas: `api_report` y `sauce_report`. Cada una contendrá su propio archivo `testresults.html` con los resultados de las pruebas correspondientes.

## Integración continua con Github Actions

Este proyecto esta configurado para ejecutarse en Github Actions al hacer un push a la rama `main`. El archivo `main.yml` contiene los pasos necesarios para ejecutar las pruebas automáticamente en un entorno CI.

## Author: José Barone

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).