import pytest
import unittest
import sys
import logging
from Aluguel import Aluguel

log = logging.getLogger()
handler = logging.StreamHandler()
log.addHandler(handler)
VALOR_NOMINAL = 1200.0

class testeAluguelRange2(unittest.TestCase):
    def testeValorRange2InferiorMHGF(self):
        aluguel = Aluguel()
        valor = aluguel.calcular_aluguel(VALOR_NOMINAL, 6)
        VALOR_ESPERADO = 1140.0
        
        #Log no Report
        texto_log = 'Valor Esperado: {} \nValor Recebido: {}'.format(VALOR_ESPERADO, valor)
        sys.stderr.write(texto_log)
        
        self.assertEqual(VALOR_ESPERADO, valor)

    def testeValorRange2MeioMHGF(self):
        aluguel = Aluguel()
        valor = aluguel.calcular_aluguel(VALOR_NOMINAL, 8)
        VALOR_ESPERADO = 1140.0
        
        #Log no Report
        texto_log = 'Valor Esperado: {} \nValor Recebido: {}'.format(VALOR_ESPERADO, valor)
        sys.stderr.write(texto_log)
        
        self.assertEqual(VALOR_ESPERADO, valor)

    def testeValorRange2SuperiorMHGF(self):
        aluguel = Aluguel()
        valor = aluguel.calcular_aluguel(VALOR_NOMINAL, 10)
        VALOR_ESPERADO = 1140.0
        
        #Log no Report
        texto_log = 'Valor Esperado: {} \nValor Recebido: {}'.format(VALOR_ESPERADO, valor)
        sys.stderr.write(texto_log)
        
        self.assertEqual(VALOR_ESPERADO, valor)
        
        
