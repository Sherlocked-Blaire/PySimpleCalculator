%%pytest
from SimpleCalculator import Calculator
import pytest

def test_add():
    calculator = Calculator()
    result = calculator.add(5)
    assert result == 5
      
def test_subtract():
    calculator = Calculator()
    calculator.add(10)
    result = calculator.subtract(2)
    assert result == 8
    
def test_reset():
    calculator = Calculator()
    calculator.add(10)
    result = calculator.subtract(2)
    calculator.reset() 
    assert calculator.current_value() == 0
      
    
def test_divide():
    calculator = Calculator()
    calculator.add(10)
    result = calculator.divide(2)
    assert result == 5
    
    
def test_multiply():
    calculator = Calculator()
    calculator.add(20)
    result = calculator.multiply(4)
    assert result == 80   

def test_nth_root():
    calculator = Calculator()
    calculator.add(25)
    result = calculator.nth_root(5)
    assert result == 5  

def test_nth_root_num():
    calculator = Calculator()
    result = calculator.nth_root(2,25)
    assert result == 5        

def test_exp():
    calculator = Calculator()
    calculator.add(4)
    result = calculator.exp(3)
    assert result == 64
    
def test_exp_num():
    calculator = Calculator()
    result = calculator.exp(3,4)
    assert result == 64  

def test_input_validation():
    with pytest.raises(Exception):
        calculator = Calculator()
        calculator.add('3')    

def test_zero_division():
    with pytest.raises(Exception):
        calculator = Calculator()
        calculator.add(6)
        calculator.divide(0) 
  

def test_root_value_equal_than_zero():
    with pytest.raises(Exception):
        calculator = Calculator()
        calculator.add(4)
        calcultor.nth_root(0)    