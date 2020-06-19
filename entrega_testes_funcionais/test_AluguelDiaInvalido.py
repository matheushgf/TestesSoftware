import pytest
import unittest
import sys
import logging
from Aluguel import Aluguel

log = logging.getLogger()
handler = logging.StreamHandler()
log.addHandler(handler)
VALOR_NOMINAL = 1200.0

class testeAluguelDiaInvalido(unittest.TestCase):       
    def testeDiaInvalidoInferiorMHGF(self):
        aluguel = Aluguel()
        valor = aluguel.calcular_aluguel(VALOR_NOMINAL, 0)
        VALOR_ESPERADO = -1

        #Log no Report
        texto_log = 'Valor Esperado: {} \nValor Recebido: {}'.format(VALOR_ESPERADO, valor)
        sys.stderr.write(texto_log)
        
        self.assertEqual(VALOR_ESPERADO, valor)
        
    def testeDiaInvalidoSuperiorMHGF(self):
        aluguel = Aluguel()
        valor = aluguel.calcular_aluguel(VALOR_NOMINAL, 31)
        VALOR_ESPERADO = -1

        #Log no Report
        texto_log = 'Valor Esperado: {} \nValor Recebido: {}'.format(VALOR_ESPERADO, valor)
        sys.stderr.write(texto_log)
        
        self.assertEqual(VALOR_ESPERADO, valor)
