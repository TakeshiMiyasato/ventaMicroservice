from abc import ABC, abstractmethod

from DDD.SharedKernel.Core.ABSBussinessRule import BussinessRule
from DDD.SharedKernel.Core.BussinessRuleValidationException import BussinessRuleValidationException


class ValueObject(ABC):
    @abstractmethod
    def check_rule(self, rule: BussinessRule):
        if rule is None:
            raise Exception('La regla no puede ser nula')
        if not rule.isValid():
            raise BussinessRuleValidationException.BussinessRuleValidationExceptionSetRule(brokenRule=rule)
