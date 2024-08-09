from __future__ import annotations
from typing import Type
class Currency:
"""
1 EUR = 2 USD = 100 GBP
1 EUR = 2 USD ; 1 EUR = 100 GBP
1 USD = 0.5 EUR ; 1 USD = 50 GBP
1 GBP = 0.02 USD ; 1 GBP = 0.01 EUR
"""
d = {
'Euro': (1, 'EUR'),
"Pound": (100, 'GBP'),
'Dollar': (2, 'USD')
}
def __init__(self, value: float):
self.value=value
@classmethod
def course(cls, other_cls: Type[Currency]) -> str:
curreny1=cls.__name__
curreny2=other_cls.__name__
result=f"{(Currency.d[curreny2][0])/Currency.d[curreny1][0]} {Currency.d[curreny2][1]} for {1} {Currency.d[curreny1][1]}"
return result
def to_currency(self, other_cls: Type[Currency]):
pass
def __add__(self, other):
converted=other.to_currency(self.__class__)
return self.__class__(float(self.value+converted.value))
def __sub__(self, other):
converted=other.to_currency(self.__class__)
return self.__class__(float(self.value-converted.value))
def __lt__(self, other):
converted=other.to_currency(self.__class__)
return True if (self.value<converted.value) else False
def __gt__(self, other):
converted=other.to_currency(self.__class__)
return True if (self.value>converted.value) else False
def __eq__(self, other):
converted=other.to_currency(self.__class__)
return True if(self.value==converted.value) else False
def __repr__(self):
return str(self.value)+' '+Currency.d[self.__class__.__name__][1]
class Euro(Currency):
def to_currency(self, other_cls: Type[Currency]):
return other_cls(float(self.value * self.d[other_cls.__name__][0]))
class Dollar(Currency):
def to_currency(self, other_cls: Type[Currency]):
if other_cls.__name__=='Euro':
return other_cls(float(self.value/2))
if other_cls.__name__=='Pound':
return other_cls(float(self.value*50))
return other_cls(float(self.value))
class Pound(Currency):
def to_currency(self, other_cls: Type[Currency]):
if other_cls.__name__=="Dollar":
return other_cls(float(self.value /50))
if other_cls.__name__=='Euro':
return other_cls(float(self.value /100))
return other_cls(float(self.value))