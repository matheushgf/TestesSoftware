import pytest
import unittest
import sys
import logging
from Aluguel import Aluguel

log = logging.getLogger()
handler = logging.StreamHandler()
log.addHandler(handler)
VALOR_NOMINAL = 1200.0

#Fórmula de cálculo do Valor Range 4: V = (1200*1.02)*((1+0.001)^t)
#V=Valor; 1.02 = Multa de 2%; t=Tempo (em dias); (1+0,001) = Cálculo Juros Compostos

class testeAluguelRange4(unittest.TestCase):
    def testeValorRange4InferiorMHGF(self):
        aluguel = Aluguel()
        valor = aluguel.calcular_aluguel(VALOR_NOMINAL, 16)
        VALOR_ESPERADO = 1225.2
        
        #Log no Report
        texto_log = 'Valor Esperado: {} \nValor Recebido: {}'.format(VALOR_ESPERADO, valor)
        sys.stderr.write(texto_log)
        
        self.assertEqual(VALOR_ESPERADO, valor)

    def testeValorRange4MeioMHGF(self):
        aluguel = Aluguel()
        valor = aluguel.calcular_aluguel(VALOR_NOMINAL, 24)
        VALOR_ESPERADO = 1235.0
        
        #Log no Report
        texto_log = 'Valor Esperado: {} \nValor Recebido: {}'.format(VALOR_ESPERADO, valor)
        sys.stderr.write(texto_log)
        
        self.assertEqual(VALOR_ESPERADO, valor)

    def testeValorRange4SuperiorMHGF(self):
        aluguel = Aluguel()
        valor = aluguel.calcular_aluguel(VALOR_NOMINAL, 30)
        VALOR_ESPERADO = 1242.4
        
        #Log no Report
        texto_log = 'Valor Esperado: {} \nValor Recebido: {}'.format(VALOR_ESPERADO, valor)
        sys.stderr.write(texto_log)
        
        self.assertEqual(VALOR_ESPERADO, valor)
        
        
