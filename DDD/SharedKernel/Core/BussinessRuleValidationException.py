from DDD.SharedKernel.Core.ABSBussinessRule import BussinessRule


class BussinessRuleValidationException(Exception):
    def __init__(self, brokenRule: BussinessRule, details: str):
        self.brokenRule: BussinessRule = brokenRule
        self.details: str = details

    def BussinessRuleValidationExceptionSetRule(self, brokenRule: BussinessRule):
        self.brokenRule = brokenRule
        self.details = brokenRule.message

    def BussinessRuleValidationExceptionRaiseMessage(self, message: str):
        self.details = message
