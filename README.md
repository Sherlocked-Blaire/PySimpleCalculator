# PySimpleCalculator
This is a python package and can be used to perform basic functions on calculator such as;
- ADDITION
- SUBTRACTION
- DIVISION
- MULTIPLICATION
- FINDING THE  ROOT OF A NUMBER 
- FINDING THE POWER OF A NUMBER


## Getting Started
### Installation

pypi_calculator requires python3 and can be installed via PYPI

``` shell
$ pip install git+https://github.com/Sherlocked-Blaire/PySimpleCalculator.git
```
### Usage
The calculator can be used for basic operations.he calculator has a memory that caches the last result until it is reset. The cached result is used in the next computation if not reset.

Examples will be shown below
###  Sample Code
```python
from SimpleCalculator import Calculator

calculator = Calculator()
```
#### Addition
```python
>>> calculator.add(200)
200
```
#### Subtraction
`subtract`
```python
>>> my_cal.subtract(54)
146
```
because the memory was not reset, `54` was subtracted from previous value `200`


#### Division
```python
>>> calculator.divide(2)
73
```
because the memory was not reset, `146` was divided by `2`

#### Reset Memory
```python
>>> calculator.reset()
```
```python
>>> calculator.current_value()
0
```


