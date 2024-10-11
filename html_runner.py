import unittest
from HtmlTestRunner import HTMLTestRunner
import os

# Crear directorios para los reportes si no existen
# os.makedirs('report_directory/sauce_report', exist_ok=True)
# os.makedirs('report_directory/api_report', exist_ok=True)

# Cargar y ejecutar pruebas de Sauce
pruebas_sauce_suite = unittest.TestLoader().discover('pruebas_sauce_demo')
runner_sauce = HTMLTestRunner(output='report_directory/sauce_report', report_title='Pruebas Sauce', combine_reports=True)
try:
    runner_sauce.run(pruebas_sauce_suite)
except Exception as e:
    print(f'Ocurrio algun problema: {e}')

# Cargar y ejecutar pruebas de API
pruebas_api_suite = unittest.TestLoader().discover('pruebas_poke_api')
runner_api = HTMLTestRunner(output='report_directory/api_report', report_title='Pruebas Poke API', combine_reports=True)
try:
    runner_api.run(pruebas_api_suite)
except Exception as e:
    print(f'Ocurrió algún problema: {e}')
