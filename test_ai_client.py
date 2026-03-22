import unittest
from unittest.mock import patch, MagicMock
from ai_client import get_analysis

class TestAIClient(unittest.TestCase):

    @patch('ai_client.genai.GenerativeModel') # Interceptamos la clase modelo
    def test_get_analysis_success(self, mock_model_class):
        # 1. Configuramos el mock (falsa respuesta)
        mock_model_instance = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "ANÁLISIS ESTRUCTURADO: Todo ok"
        mock_model_instance.generate_content.return_value = mock_response
        mock_model_class.return_value = mock_model_instance

        # 2. Ejecutamos la función real
        resultado = get_analysis("print('hola')")

        # 3. Verificamos que se comporte como queremos
        self.assertEqual(resultado, "ANÁLISIS ESTRUCTURADO: Todo ok")
        mock_model_instance.generate_content.assert_called_once()

if __name__ == '__main__':
    unittest.main()
