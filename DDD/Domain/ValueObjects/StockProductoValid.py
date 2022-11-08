from DDD.SharedKernel.Core.ABSValueObject import ValueObject
from DDD.SharedKernel.Core.BussinessRuleValidationException import BussinessRuleValidationException


class StockProducto(ValueObject):
    def __init__(self, stock: int):
        if stock < 0:
            raise Exception(BussinessRuleValidationException.
                            BussinessRuleValidationExceptionRaiseMessage(message='El stock no '
                                                                         'puede ser menor a 0'))
        self.stock: int = stock