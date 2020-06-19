import pytest
import unittest
import sys
import logging
from Aluguel import Aluguel

log = logging.getLogger()
handler = logging.StreamHandler()
log.addHandler(handler)
VALOR_NOMINAL = 1200.0

class testeAluguelRange3(unittest.TestCase):
    def testeValorRange3InferiorMHGF(self):
        aluguel = Aluguel()
        valor = aluguel.calcular_aluguel(VALOR_NOMINAL, 11)
        VALOR_ESPERADO = VALOR_NOMINAL
        
        #Log no Report
        texto_log = 'Valor Esperado: {} \nValor Recebido: {}'.format(VALOR_ESPERADO, valor)
        sys.stderr.write(texto_log)
        
        self.assertEqual(VALOR_ESPERADO, valor)

    def testeValorRange3MeioMHGF(self):
        aluguel = Aluguel()
        valor = aluguel.calcular_aluguel(VALOR_NOMINAL, 14)
        VALOR_ESPERADO = VALOR_NOMINAL
        
        #Log no Report
        texto_log = 'Valor Esperado: {} \nValor Recebido: {}'.format(VALOR_ESPERADO, valor)
        sys.stderr.write(texto_log)
        
        self.assertEqual(VALOR_ESPERADO, valor)

    def testeValorRange3SuperiorMHGF(self):
        aluguel = Aluguel()
        valor = aluguel.calcular_aluguel(VALOR_NOMINAL, 15)
        VALOR_ESPERADO = VALOR_NOMINAL
        
        #Log no Report
        texto_log = 'Valor Esperado: {} \nValor Recebido: {}'.format(VALOR_ESPERADO, valor)
        sys.stderr.write(texto_log)
        
        self.assertEqual(VALOR_ESPERADO, valor)
        
        
