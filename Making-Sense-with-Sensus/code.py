# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data.shape)
#Code starts here
census = np.concatenate((data,new_record),axis=0)
print(census.shape)

age=census[:,0]
max_age = max(age)
min_age = min(age)
age_mean = np.mean(age)
age_std = np.std(age)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)

race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

minority_race = min(len_0,len_1,len_2,len_3,len_4)
if minority_race == len_0:
    minority_race == "0"
elif minority_race == len_1:
    minority_race == "1"
elif minority_race == len_2:
    minority_race == "2"
elif minority_race == len_3:
    minority_race == "3"
else:
    minority_race == "4"
print(minority_race)

senior_citizen = census[census[:,0]>60]
senior_citizen_len = len(senior_citizen)
working_hours_sum = senior_citizen.sum(axis = 0)[6]
avg_working_hours = working_hours_sum/senior_citizen_len
print(working_hours_sum)
print(avg_working_hours)

high = census[census[:,1]>10]
low = census[census[:,1]<10]
income_sum_high = high.sum(axis = 0)[7]
income_sum_low = low.sum(axis = 0)[7]
income_len_high = len(high)
income_len_low = len(low)
avg_pay_high = income_sum_high/income_len_high
avg_pay_low = (income_sum_low/income_len_low) + 0.01
avg_pay_low_round = round(avg_pay_low,2) + 0.01
print(avg_pay_high)
print(avg_pay_low)


