import InputData as D
import ParameterClasses as P
import MarkovClasses as Cls
import Support as Support


# simulating no therapy
# create a cohort
cohort_none = Cls.Cohort(id=0,
                         pop_size=D.POP_SIZE,
                         parameters=P.ParametersFixed(therapy=P.Therapies.NONE))
# simulate the cohort
cohort_none.simulate(sim_length=D.SIM_LENGTH)

# simulating anticoagulation therapy
# create a cohort
cohort_anti = Cls.Cohort(id=1,
                         pop_size=D.POP_SIZE,
                         parameters=P.ParametersFixed(therapy=P.Therapies.ANTICOAG))
# simulate the cohort
cohort_anti.simulate(sim_length=D.SIM_LENGTH)

# print the estimates for the mean survival time and mean time to AIDS
Support.print_outcomes(sim_outcomes=cohort_none.cohortOutcomes,
                       therapy_name=P.Therapies.NONE)
Support.print_outcomes(sim_outcomes=cohort_anti.cohortOutcomes,
                       therapy_name=P.Therapies.ANTICOAG)

# plot survival curves and histograms
Support.plot_survival_curves_and_histograms(sim_outcomes_mono=cohort_none.cohortOutcomes,
                                            sim_outcomes_combo=cohort_anti.cohortOutcomes)

# print comparative outcomes
Support.print_comparative_outcomes(sim_outcomes_none=cohort_none.cohortOutcomes,
                                   sim_outcomes_anti=cohort_anti.cohortOutcomes)

# report the CEA results
Support.report_CEA_CBA(sim_outcomes_none=cohort_none.cohortOutcomes,
                       sim_outcomes_anti=cohort_anti.cohortOutcomes)
