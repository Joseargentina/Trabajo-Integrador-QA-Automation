import requests
import unittest
from dotenv import load_dotenv
import os

class TestPoke(unittest.TestCase):
    def setUp(self) -> None:
        load_dotenv()
        self.url = os.getenv('BASE_URL_API')
        print(f'La url es: {self.url}' )
    

    def test_berry_1_size_soil_dryness_firmness(self):
        r = requests.get(self.url + 'berry/1')
        self.assertEqual(r.status_code, 200, "La solicitud no fue exitosa")
        data = r.json()
        
        self.assertIn('size', data, "No se encontró 'size' en los datos de la respuesta")
        self.assertEqual(data['size'], 20, "El tamaño no es igual a 20")
        self.assertIn('soil_dryness', data, "No se encontró 'soil_dryness' en los datos de la respuesta")
        self.assertEqual(data['soil_dryness'], 15)
        self.assertIn('firmness', data, "No se encontró 'firmness' en los datos de la respuesta")
        self.assertIn('name', data['firmness'])
        self.assertEqual(data['firmness']['name'],'soft')
    
    def test_berry_2_firmness_size_soil_dryness_comparison(self):
        r = requests.get(self.url + 'berry/2')
        self.assertEqual(r.status_code, 200, "La solicitud no fue exitosa")
        data = r.json()
        self.assertIn('firmness', data, "No se encontró 'firmness' en los datos de la respuesta")
        self.assertIn('name', data['firmness'], "No se encontró 'name' en los datos de la firmness")
        self.assertEqual(data['firmness']['name'], 'super-hard')
        self.assertTrue(data['size'] > 20, "El tamaño no es mayor a 20")
        self.assertEqual(data['soil_dryness'], 15)
        
    def test_pikachu_base_experience_and_type(self):
        r = requests.get(self.url + 'pokemon/pikachu/')
        print(f'La url es: {self.url + "pokemon/pikachu/"}')
        self.assertEqual(r.status_code, 200, "La solicitud no fue exitosa")
        data = r.json()
        self.assertIn('base_experience', data, "No se encontró 'base_experience' en los datos de la respuesta")
        self.assertTrue(10 < data['base_experience'] < 1000, "La experiencia base no está en el rango esperado")
        self.assertIn('types', data,"No se encontró 'types' en los datos de la respuesta")
        self.assertEqual(data['types'][0]['type']['name'],'electric',"Pikachu no es de tipo electric")
        
if __name__ == '__main__':
    unittest.main()
