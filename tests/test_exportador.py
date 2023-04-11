import unittest

from nfselib.barueri.exportador import Arquivo
from nfselib.barueri.exportador import CampoPosicional
from nfselib.barueri.exportador import Registro


class TestCampoPosicional(unittest.TestCase):
    def test_exportar(self):
        campo = CampoPosicional("nome", "valor", True, "ALFA", 10, 1, 10)
        self.assertEqual(campo.exportar(), "valor     ")


class TestRegistro(unittest.TestCase):
    def test_campos(self):
        registro = Registro()
        campo_1 = CampoPosicional("campo1", "valor1", True, "NUM", 5, 1, 5)
        campo_2 = CampoPosicional("campo2", "valor2", False, "ALFA", 10, 6, 15)
        registro.campos = [campo_1, campo_2]

        # test __setattr__
        registro.campo1 = "new_value"
        self.assertEqual(registro.campos[0].valor, "new_value")

        # test __getattr__
        self.assertEqual(registro.campo1, "new_value")
        self.assertEqual(registro.campo2, "valor2")

    def test_exportar(self):
        registro = Registro()
        campo_1 = CampoPosicional("campo1", "12345", True, "NUM", 5, 1, 5)
        campo_2 = CampoPosicional("campo2", "valor2", False, "ALFA", 10, 6, 15)
        registro.campos = [campo_1, campo_2]
        self.assertEqual(registro.exportar(), "12345valor2    ")


class TestArquivo(unittest.TestCase):
    def test_adicionar_registro(self):
        arquivo = Arquivo()
        registro = Registro()
        arquivo.adicionar_registro(registro)
        self.assertEqual(len(arquivo.registros), 1)
        self.assertEqual(arquivo.registros[0], registro)

    def test_exportar(self):
        arquivo = Arquivo()
        registro_1 = Registro()
        campo_1_1 = CampoPosicional("campo1", "12345", True, "NUM", 5, 1, 5)
        campo_1_2 = CampoPosicional("campo2", "valor2", False, "ALFA", 10, 6, 15)
        registro_1.campos = [campo_1_1, campo_1_2]

        registro_2 = Registro()
        campo_2_1 = CampoPosicional("campo1", "12345", True, "NUM", 5, 1, 5)
        campo_2_2 = CampoPosicional("campo2", "valor4", False, "ALFA", 10, 6, 15)
        registro_2.campos = [campo_2_1, campo_2_2]

        arquivo.registros = [registro_1, registro_2]
        self.assertEqual(arquivo.exportar(), "12345valor2    12345valor4    ")


if __name__ == '__main__':
    unittest.main()
