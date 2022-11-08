from DDD.SharedKernel.Core.ABSValueObject import ValueObject
from DDD.SharedKernel.Core.BussinessRuleValidationException import BussinessRuleValidationException


class Cantidad(ValueObject):
    def __init__(self, cantidad: int):
        if cantidad < 0:
            raise Exception(BussinessRuleValidationException.
            BussinessRuleValidationExceptionRaiseMessage(
                message='La cantidad de productos no debe ser menor o igual a 0'))
        self.cantidad = cantidad
