import deampy.plots.histogram as hist
import deampy.plots.sample_paths as path

import InputData as D
import MarkovClasses as Cls
import ParameterClasses as P
import Support as Support

# selected therapy
therapy = P.Therapies.ANTICOAG

# create a cohort
myCohort = Cls.Cohort(id=1,
                      pop_size=D.POP_SIZE,
                      parameters=P.Parameters(therapy=therapy))

# simulate the cohort over the specified time steps
myCohort.simulate(sim_length=D.SIM_LENGTH)

# plot the sample path (survival curve)
path.plot_sample_path(
    sample_path=myCohort.cohortOutcomes.nLivingPatients,
    title='Survival Curve',
    x_label='Time-Step (Year)',
    y_label='Number Survived')

# plot the histogram of survival times
hist.plot_histogram(
    data=myCohort.cohortOutcomes.nTotalStrokes,
    title='Histogram of Patient Total Strokes',
    x_label='Survival Time (Year)',
    y_label='Count',
    bin_width=1)

# print the outcomes of this simulated cohort
Support.print_outcomes(sim_outcomes=myCohort.cohortOutcomes, therapy_name=therapy)
