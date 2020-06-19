import pytest
import unittest
import sys
import logging
from Aluguel import Aluguel

log = logging.getLogger()
handler = logging.StreamHandler()
log.addHandler(handler)
VALOR_NOMINAL = 1200.0

class testeAluguelRange1(unittest.TestCase):
    def testeValorRange1InferiorMHGF(self):
        aluguel = Aluguel()
        valor = aluguel.calcular_aluguel(VALOR_NOMINAL, 1)
        VALOR_ESPERADO = 1080.0

        #Log no Report
        texto_log = 'Valor Esperado: {} \nValor Recebido: {}'.format(VALOR_ESPERADO, valor)
        sys.stderr.write(texto_log)
        
        self.assertEqual(valor, VALOR_ESPERADO)

    def testeValorRange1MeioMHGF(self):
        aluguel = Aluguel()
        valor = aluguel.calcular_aluguel(VALOR_NOMINAL, 2)
        VALOR_ESPERADO = 1080.0

        #Log no Report
        texto_log = 'Valor Esperado: {} \nValor Recebido: {}'.format(VALOR_ESPERADO, valor)
        sys.stderr.write(texto_log)
        
        self.assertEqual(valor, VALOR_ESPERADO)

    def testeValorRange1SuperiorMHGF(self):
        aluguel = Aluguel()
        valor = aluguel.calcular_aluguel(VALOR_NOMINAL, 5)
        VALOR_ESPERADO = 1080.0

        #Log no Report
        texto_log = 'Valor Esperado: {} \nValor Recebido: {}'.format(VALOR_ESPERADO, valor)
        sys.stderr.write(texto_log)
        
        self.assertEqual(valor, VALOR_ESPERADO)  
