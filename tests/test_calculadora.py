import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculadora import sumar, restar, multiplicar, dividir, potencia 
import pytest

def test_sumar():
    assert sumar(2, 3) == 5

def test_restar():
    assert restar(10, 4) == 6

def test_multiplicar():
    assert multiplicar(3, 4) == 12

def test_dividir():
    assert dividir(10, 2) == 5.0

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(5, 0)
        
def test_potencia(): 
    assert potencia(2, 3) == 8 
    assert potencia(5, 0) == 1 
    assert potencia(3, 2) == 9 
