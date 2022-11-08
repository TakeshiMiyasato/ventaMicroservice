from DDD.SharedKernel.Core.ABSValueObject import ValueObject
from DDD.SharedKernel.Core.BussinessRuleValidationException import BussinessRuleValidationException


class PrecioProducto(ValueObject):
    def __init__(self, precio: float):
        if precio < 0.0:
            raise Exception(BussinessRuleValidationException.
                            BussinessRuleValidationExceptionRaiseMessage(message='El precio de un producto '
                                                                         'no puede ser 0 o menor'))
        self.precio: float = precio