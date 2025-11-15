# test_main.py
import unittest
from main import somar, subtrair, multiplicar, dividir, potencia

class TestCalculadora(unittest.TestCase):

    # Teste 1: Soma básica de positivos
    def test_somar_positivos(self):
        self.assertEqual(somar(10, 5), 15, "A soma de 10 e 5 deveria ser 15.")

    # Teste 2: Subtração com resultado negativo
    def test_subtrair_negativo(self):
        self.assertEqual(subtrair(5, 15), -10, "A subtração de 5 por 15 deveria ser -10.")

    # Teste 3: Multiplicação por zero (caso limite)
    def test_multiplicar_por_zero(self):
        self.assertEqual(multiplicar(99, 0), 0, "Qualquer número multiplicado por zero deve ser zero.")

    # Teste 4: Divisão por número positivo
    def test_dividir_basico(self):
        self.assertEqual(dividir(20, 4), 5.0, "A divisão de 20 por 4 deveria ser 5.0.")

    # Teste 5: Teste de exceção para divisão por zero (REQUISITO CRÍTICO)
    def test_dividir_por_zero_excecao(self):
        # Verifica se um ValueError é levantado ao tentar dividir por zero
        with self.assertRaises(ValueError):
            dividir(10, 0)

    # Teste 6: Potência com expoente zero
    def test_potencia_expoente_zero(self):
        self.assertEqual(potencia(5, 0), 1, "Qualquer número (não zero) elevado a zero é 1.")

    # Teste 7: Teste com números decimais (float)
    def test_somar_decimais(self):
        self.assertAlmostEqual(somar(1.5, 2.3), 3.8, 2, "A soma de decimais deve ser precisa.")

# Para rodar os testes diretamente
if __name__ == '__main__':
    unittest.main()
