from enum import Enum

import InputData as D


class HealthStates(Enum):
    """ health states of patients """
    WELL = 0
    STROKE = 1
    POST_STROKE = 2
    STROKE_DEAD = 3
    NATURAL_DEATH = 4


class Therapies(Enum):
    """ none vs anticoagulation """
    NONE = 0
    ANTICOAG = 1


class Parameters:
    def __init__(self, therapy):

        # selected therapy
        self.therapy = therapy

        # initial health state
        self.initialHealthState = HealthStates.WELL

        # transition probability matrix of the selected therapy
        self.transRateMatrix = []

        # calculate transition rate matrices depending on which therapy options is in use
        if therapy == Therapies.NONE:
            self.transRateMatrix = D.get_trans_rate_matrix(with_treatment=False)
        else:
            self.transRateMatrix = D.get_trans_rate_matrix(with_treatment=True)

        # annual treatment cost
        if self.therapy == Therapies.NONE:
            self.annuaAntiCoagCost = 0
        elif self.therapy == Therapies.ANTICOAG:
            self.annuaAntiCoagCost = D.ANTICOAG_COST

        # stroke cost
        self.strokeCost = D.STROKE_COST

        # state costs and utilities
        self.annualStateCosts = D.ANNUAL_STATE_COST
        self.annualStateUtilities = D.ANNUAL_STATE_UTILITY

        # discount rate
        self.discountRate = D.DISCOUNT

