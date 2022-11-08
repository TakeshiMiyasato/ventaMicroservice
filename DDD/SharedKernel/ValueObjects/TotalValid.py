from DDD.SharedKernel.Core.ABSBussinessRule import BussinessRule
from DDD.SharedKernel.Core.ABSValueObject import ValueObject
from DDD.SharedKernel.Core.BussinessRuleValidationException import BussinessRuleValidationException


class Total(ValueObject):

    def __init__(self, total: float):
        if total < 0.0:
            raise Exception(BussinessRuleValidationException.\
                            BussinessRuleValidationExceptionRaiseMessage(message='El precio no puede ser negativo'))
        self.total = total