import pandas as pd
from matplotlib import pyplot as plt
sample_data = pd.read_csv('Book1.csv')
sample_data
plt.plot(sample_data.Time, sample_data.GPA,'o')
plt.show()
# COMPARE the GPA BETWEEN DIFFERENT SCHOOL
PU = sample_data[sample_data.School=='Peking University ']
SP = sample_data[sample_data.School=='ShenzhenPolytechnic ']
SU = sample_data[sample_data.School=='Shenzhen Universiy']
PU
SP
SU
plt.plot(PU.GPA, PU.Time, 'o')
plt.plot(SP.GPA, SP.Time, 'o')
plt.plot(SU.GPA, SU.Time,'o')
plt.legend(['PU', 'SP', 'SU'])
plt.xlabel('GPA')
plt.ylabel('Reading time')
plt.show()