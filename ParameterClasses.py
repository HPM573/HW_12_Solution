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


class ParametersFixed:
    def __init__(self, therapy):

        # selected therapy
        self.therapy = therapy

        # initial health state
        self.initialHealthState = HealthStates.WELL

        # transition probability matrix of the selected therapy
        self.rateMatrix = []

        # calculate transition rate matrices depending of which therapy options is in use
        if therapy == Therapies.NONE:
            self.rateMatrix = D.get_trans_rate_matrix(with_treatment=False)
        else:
            self.rateMatrix = D.get_trans_rate_matrix(with_treatment=True)

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


# def get_prob_matrix(trans_matrix):
#     """
#     :param trans_matrix: transition matrix containing counts of transitions between states
#     :return: transition probability matrix
#     """
#
#     # initialize transition probability matrix
#     trans_prob_matrix = []
#
#     # for each row in the transition matrix
#     for row in trans_matrix:
#         # calculate the transition probabilities
#         prob_row = np.array(row)/sum(row)
#         # add this row of transition probabilities to the transition probability matrix
#         trans_prob_matrix.append(prob_row)
#
#     return trans_prob_matrix


# def get_rate_matrix_mono(trans_prob_matrix):
#
#     # find the transition rate matrix
#     trans_rate_matrix = Markov.discrete_to_continuous(
#         prob_matrix=trans_prob_matrix,
#         delta_t=1)
#
#     # calculate background mortality rate
#     mortality_rate = -np.log(1 - Data.ANNUAL_PROB_BACKGROUND_MORT)
#
#     # add background mortality rate
#     for row in trans_rate_matrix:
#         row.append(mortality_rate)
#
#     # add 2 rows for HIV death and natural death
#     trans_rate_matrix.append([0] * len(HealthStates))
#     trans_rate_matrix.append([0] * len(HealthStates))
#
#     return trans_rate_matrix
#

# def get_rate_matrix_combo(rate_matrix_mono, combo_rr):
#     """
#     :param rate_matrix_mono: (list of lists) transition rate matrix under mono therapy
#     :param combo_rr: relative risk of the combination treatment
#     :returns (list of lists) transition rate matrix under combination therapy """
#
#     # create an empty list of lists
#     prob_matrix = copy.deepcopy(rate_matrix_mono)
#
#     # change the probability of moving from 'post-stroke' to 'stroke' when anti-coagulation is used
#     prob_matrix[HealthStates.POST_STROKE.value][HealthStates.STROKE.value] = \
#         rate_matrix_mono[HealthStates.POST_STROKE.value][HealthStates.STROKE.value] * combo_rr
#
#     # change the probability of staying in 'post-stroke' when anti-coagulation is used
#     prob_matrix[HealthStates.POST_STROKE.value][HealthStates.POST_STROKE.value] = \
#         1 - prob_matrix[HealthStates.POST_STROKE.value][HealthStates.STROKE.value]
#
#     return prob_matrix
#

# # tests
# matrix_mono = get_rate_matrix(Data.TRANS_MATRIX)
# matrix_combo = get_rate_matrix_combo(matrix_mono, Data.TREATMENT_RR)
#
# print(matrix_mono)
# print(matrix_combo)
