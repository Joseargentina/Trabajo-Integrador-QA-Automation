import requests
import unittest
from dotenv import load_dotenv
import os

class TestPoke(unittest.TestCase):
    def setUp(self) -> None:
        load_dotenv()
        self.url = os.getenv('BASE_URL_API')

    def test_get_title(self):
        print(f'La url es: {self.url}' )
        r = requests.get(self.url + 'berry/1')
        self.assertEqual(r.status_code, 200, "La solicitud no fue exitosa")
        
        data = r.json()
        # print(data)
        
        self.assertIn('size', data)  # Asegúrate de que la clave 'size' esté presente
        self.assertEqual(data['size'], 20, "El tamaño no es igual a 20")
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
