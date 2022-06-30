# This is a sample Python script.
import numpy as np
import csv
import pandas as pd
import re
# wanted behaviors
residents_behaviors = []
bachelors_begaviors = []
male_b = []
female_b = []
# files to log
life_history_camile = pd.read_csv('01_Life_History_camile.csv')
life_history_reg = pd.read_csv('Life history to revise csv.csv')

#print(life_history.to_string())
observations = pd.read_csv('Observations_fix.csv')

#observations["Focal /initatior (chip)"] = observations["Focal /initatior (chip)"].apply(lambda x: x.split(" "))

#observations = observations[len(observations['Focal /initatior (chip)']) == 1 and not re.findall('[a-zA-Z]', observations['Focal /initatior (chip)']]

## create wanted chip list to process
dropind = []
for index, row in observations.iterrows():
    #print((row['Focal /initatior (chip)']))
    #print(len(row['Focal /initatior (chip)'].split(" ")))
    chips = row['Focal /initatior (chip)'].split(" ")
    if not len(chips) == 1 or re.findall('[a-zA-Z]', chips[0]): ## check if more
  #      print(chips)
        dropind.append(index)
        #df = observations.drop(index)
    if index == 100:  # a sample of 100 for easier printing
        break
## obers only with one chip
observations = observations.drop(observations.index[dropind])
## rename columns names to perform inner join
observations.rename(columns = {'Focal /initatior (chip)':'Current_chip'}, inplace = True)
print(life_history_reg['Current_chip'][1:100])
print("")
print("")
print(observations['Current_chip'][1:100])
## inner join based on chips to extract males females
merged = pd.merge(observations,life_history_reg, on ='Current_chip')
print(merged[0:5])
all_f = merged[merged['Sex'] == 'F']
all_m = merged[merged['Sex'] == 'M']
# all_bachelors = merged[merged['male.status'] == 'solitary']
# all_residents = merged[merged['male.status'] == 'dominant']
female_b = all_f['Behavior']
males_b = all_m['Behavior']
# bachelors_behaviors = all_bachelors['Behavior']
# residents_behaviors = all_residents['Behavior']



print("fb",female_b[0:10])
# for index, row in observations.iterrows():
#     #print(row['Focal /initatior (chip)'])
#     chips = row['Focal /initatior (chip)'].split(" ")
#  #   print(chips)
#
#     if index == 200:
#         break


#observations.rename(columns = {'Focal /initatior (chip)':'Current_chip'}, inplace = True)
#pd.merge(observations,life_history_reg, on ='Current_chip')

