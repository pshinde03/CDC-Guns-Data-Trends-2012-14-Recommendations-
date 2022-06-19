# importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print('Run by Pratik Shinde \n')

# Defining graph style
plt.style.use('seaborn')

# Reading the csv
df = pd.read_csv('Alll.csv')


# function to plot bar graph with labels and axis data
def bar_plot(labelx, labely, axisx, axisy, name):
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title(name)
    plt.bar(axisx, axisy)
    plt.show()


# function to plot pie charts with percentage labels and variable names
def pie_chart(labels, data, title1):
    plt.title(title1)
    plt.pie(data, labels=labels, autopct='%.1f%%')
    plt.show()


# CAUSE OF DEATHS-------------------------------------------------------------------------------------------------------
dff = pd.read_csv('full-data.csv')
total_deaths = len(dff.axes[0])
intent_counts = [0, 0, 0, 0]


# Defining the intent_index function
def intent_index(parts):
    """
    - The function gets the index value for each educational type so as to append to the list of education_counter

    - The file had some variables named NA which means no data, NA cant be used at gives a null value so the variable
    has been changed to "Unknown".
    """
    if parts == 'Suicide':
        return 0
    if parts == 'Undetermined':
        return 1
    if parts == 'Accidental':
        return 2
    if parts == 'Homicide':
        return 3


# function for appending to intent counter
def intent_counter(dff, counter):
    """
    - The function iterates through the 'intent' column from the specified csv file in the form of 'df'
    - The counter is updated on detecting the intent of death denoted in the loop
    """
    for row in dff['intent']:
        if row == 'Suicide':
            index = intent_index(row)
            counter[index] += 1
        elif row == 'Undetermined':
            index = intent_index(row)
            counter[index] += 1
        elif row == 'Accidental':
            index = intent_index(row)
            counter[index] += 1
        elif row == 'Homicide':
            index = intent_index(row)
            counter[index] += 1


intent_counter(dff, intent_counts)

# counting the percentage of suicides of the total
suicides = int(intent_counts[0])
suicides_percent = (suicides / total_deaths) * 100

# plotting the bar graph
intents = ['Suicide', 'Undetermined', 'Accidental', 'Homicide']
title = 'Distribution of Intents for year 2012 to 2014'
pie_chart(intents, intent_counts, title)

# statistics of suicide from the source file
print(suicides_percent.__round__(2), '% instances of the total', total_deaths, 'deaths, were suicides. \n')
print('The count of intents for death over the year is \n', dff['intent'].value_counts(), '\n')
print('-------------------------------------------------------------------------------------------------------------\n')

# CALCULATING TOTAL NUMBER OF SUICIDES OVER THE YEARS-------------------------------------------------------------------
number_rows = len(df.axes[0])
print('The total number of suicides that took place from the year 2012 to 2014 are:', number_rows, '\n')
print('-------------------------------------------------------------------------------------------------------------\n')

# YEARLY SUICIDAL CALCULATION-------------------------------------------------------------------------------------------

Years = ['2012', '2013', '2014']
df1 = pd.read_csv('2012.csv')
df2 = pd.read_csv('2013.csv')
df3 = pd.read_csv('2014.csv')

# number of suicide cases in the year 2012
suicides_2012 = len(df1.axes[0])
print('The count of suicides for year 2012 is \n', df1['intent'].value_counts(), '\n')
# number of suicide cases in the year 2013
suicides_2013 = len(df2.axes[0])
print('The count of suicides for year 2013 is \n', df2['intent'].value_counts(), '\n')
# number of suicide cases in the year 2014
suicides_2014 = len(df3.axes[0])
print('The count of suicides for year 2014 is \n', df3['intent'].value_counts(), '\n')

yearly_suicides = [suicides_2012, suicides_2013, suicides_2014]

# measuring the statistics for yearly suicides through a bar graph
# defining axis information
x = Years
y = yearly_suicides
xlabel1 = 'Year'
ylabel1 = 'Number of Demises'
title11 = 'Suicides for Years 2012-2014'
# using the bar graph function for plotting graph
bar_plot(xlabel1, ylabel1, x, y, title11)
print('-------------------------------------------------------------------------------------------------------------\n')

# THE RELATION WITH AGE-------------------------------------------------------------------------------------------------
# defining the list of age groups to sort the data
age_groups = ['0-24', '25-34', '35-44', '45-54', '55-64', '65-74', '75-84', '85+']
age_counters = []  # a list to accumulate the number of cases as per the age group

# extracting ages from 0-24 years:
grp_024 = []
for age in df['age']:
    if 0 <= age <= 24:
        grp_024.append(age)

# extracting ages from 25-34 years:
grp_2534 = []
for age in df['age']:
    if 25 <= age <= 34:
        grp_2534.append(age)

# extracting ages from 35-44 years:
grp_3544 = []
for age in df['age']:
    if 35 <= age <= 44:
        grp_3544.append(age)

# extracting ages from 45-54 years:
grp_4554 = []
for age in df['age']:
    if 45 <= age <= 54:
        grp_4554.append(age)

# extracting ages from 55-64 years:
grp_5564 = []
for age in df['age']:
    if 55 <= age <= 64:
        grp_5564.append(age)

# extracting ages from 65-74 years:
grp_6574 = []
for age in df['age']:
    if 65 <= age <= 74:
        grp_6574.append(age)

# extracting ages from 75-84 years:
grp_7584 = []
for age in df['age']:
    if 75 <= age <= 84:
        grp_7584.append(age)

# extracting ages from 85-100 years:
grp_85 = []
for age in df['age']:
    if 85 <= age:
        grp_85.append(age)

# getting the number of cases in the respective age categories
age_counters = [len(grp_024), len(grp_2534), len(grp_3544), len(grp_4554), len(grp_5564), len(grp_6574), len(grp_7584),
                len(grp_85)]

print('There are', number_rows - sum(age_counters), 'suicide cases with unknown ages. \n')

# plotting a graph for the cases according to age groups
# defining axis information
x = age_groups
y = age_counters
x_label = 'Age Groups'
y_label = 'Number of Demises'
title2 = 'Suicides According to the Age-Groups'
# using the bar graph function for plotting graph
bar_plot(x_label, y_label, x, y, title2)
print('-------------------------------------------------------------------------------------------------------------\n')


# GENDER SPECIFIC VALUES FOR SUICIDES-----------------------------------------------------------------------------------
gender = ['Male', 'Female']
gender_counter = []
males = []
females = []

for item in df['sex']:
    if item == 'M':
        males.append(item)
    elif item == 'F':
        females.append(item)

# count as per the gender
gender_counter = [len(males), len(females)]

males_percent = (len(males)/number_rows) * 100  # calculating percentage of male who committed suicide
females_percent = (len(females)/number_rows) * 100  # calculating percentage of female who committed suicide

print(males_percent.__round__(2), '% males committed suicide from the year 2012 to 2014')
print(females_percent.__round__(2), '% females committed suicide from the year 2012 to 2014 \n')

# Plotting the pie chart
title3 = 'Gender Distribution of Suicides'
pie_chart(gender, gender_counter, title3)
print('-------------------------------------------------------------------------------------------------------------\n')


# CHECKING THE EDUCATIONAL LEVEL PERSPECTIVE TO SUICIDES----------------------------------------------------------------


# Defining the education_level function
def education_level(parts):
    """
    - The function gets the index value for each educational type so as to append to the list of education_counter

    - The file had some variables named NA which means no data, NA cant be used at gives a null value so the variable
    has been changed to "Unknown".
    """
    if parts == 'BA+':
        return 0
    if parts == 'Some college':
        return 1
    if parts == 'HS/GED':
        return 2
    if parts == 'Unknown':
        return 3
    if parts == 'Less than HS':
        return 4


# function for appending to education counter
def education_counter(dff, counter):
    """
    - The function iterates through the 'education' column from the specified csv file in the form of 'df'
    - The counter is updated on detecting the educational level denoted in the loop
    """
    for row in dff['education']:
        if row == 'BA+':
            index = education_level(row)
            counter[index] += 1
        elif row == 'Some college':
            index = education_level(row)
            counter[index] += 1
        elif row == 'HS/GED':
            index = education_level(row)
            counter[index] += 1
        elif row == 'Unknown':
            index = education_level(row)
            counter[index] += 1
        elif row == 'Less than HS':
            index = education_level(row)
            counter[index] += 1


# defining a list to input the education background counts
education_counts = [0, 0, 0, 0, 0]   # education background counters list

# counting the number of suicides by relating it to the educational background
education_counter(df, education_counts)

# plotting bar graph for suicides according to the educational background
education_types = ['BA+', 'Some college', 'HS/GED', 'Unknown', 'Less than HS']
title4 = 'Suicides as per the Educational Backgrounds'
pie_chart(education_types, education_counts, title4)

print('The count of suicides per education class is \n', df['education'].value_counts(), '\n')
print('-------------------------------------------------------------------------------------------------------------\n')


# ANALYSING THE RACE FACTOR FOR SUICIDES--------------------------------------------------------------------------------


# Defining the race function for getting index
def race(parts):
    """
    The function gets the index value for each race type so as to append to the list of race_counter
    """
    if parts == 'Asian/Pacific Islander':
        return 0
    if parts == 'Native American/Native Alaskan':
        return 1
    if parts == 'White':
        return 2
    if parts == 'Black':
        return 3
    if parts == 'Hispanic':
        return 4


# function for appending to race counter
def race_counter(dff1, counters):
    """
    - The function iterates through the 'race' column from the specified csv file in the form of 'df'
    - The counter is updated on detecting the race denoted in the loop
    """
    for row in dff1['race']:
        if row == 'Asian/Pacific Islander':
            index = race(row)
            counters[index] += 1
        elif row == 'Native American/Native Alaskan':
            index = race(row)
            counters[index] += 1
        elif row == 'White':
            index = race(row)
            counters[index] += 1
        elif row == 'Black':
            index = race(row)
            counters[index] += 1
        elif row == 'Hispanic':
            index = race(row)
            counters[index] += 1


# defining a list to input the racial factor counts
race_counts = [0, 0, 0, 0, 0]

# counting the number of suicides by relating it to the race
race_counter(df, race_counts)

# plotting bar graph for suicides according to the race of victim
race_types = ['Asian/Pacific Islander', 'Native American/Native Alaskan', 'White', 'Black', 'Hispanic']
title5 = 'Suicides as per Race'
pie_chart(race_types, race_counts, title5)

print('The count of suicides per racial class is \n', df['race'].value_counts(), '\n')
print('-------------------------------------------YEARLY ANALYSIS---------------------------------------------------\n')


# ------------------------------------------------YEARLY ANALYSIS-------------------------------------------------------

# GENDER BASED STATISTICS FOR THE GIVEN 3 YEARS (2012, 2013, 2014)------------------------------------------------------
# YEAR 2012


# a function to count the number of male and females
def gender_counter(hf, male_counter, female_counter):
    for item in hf['sex']:
        if item == 'M':
            male_counter.append(item)
        elif item == 'F':
            female_counter.append(item)


males_2012 = []
females_2012 = []

gender_counter(df1, males_2012, females_2012)
# count as per the gender
gender_counts_2012 = [len(males_2012), len(females_2012)]

males_percent_2012 = (len(males_2012)/suicides_2012) * 100  # calculating percentage of male who committed suicide
females_percent_2012 = (len(females_2012)/suicides_2012) * 100  # calculating percentage of female who committed suicide

print(males_percent_2012.__round__(2), '% males committed suicide from the year 2012 to 2014')
print(females_percent_2012.__round__(2), '% females committed suicide from the year 2012 to 2014 \n')

# YEAR 2013
males_2013 = []
females_2013 = []
gender_counter(df2, males_2013, females_2013)

# count as per the gender
gender_counts_2013 = [len(males_2013), len(females_2013)]

males_percent_2013 = (len(males_2013)/suicides_2013) * 100  # calculating percentage of male who committed suicide
females_percent_2013 = (len(females_2013)/suicides_2013) * 100  # calculating percentage of female who committed suicide

print(males_percent_2013.__round__(2), '% males committed suicide from the year 2012 to 2014')
print(females_percent_2013.__round__(2), '% females committed suicide from the year 2012 to 2014 \n')

# YEAR 2014
males_2014 = []
females_2014 = []
gender_counter(df3, males_2014, females_2014)

# count as per the gender
gender_counter_2014 = [len(males_2014), len(females_2014)]

males_percent_2014 = (len(males_2014)/suicides_2014) * 100  # calculating percentage of male who committed suicide
females_percent_2014 = (len(females_2014)/suicides_2014) * 100  # calculating percentage of female who committed suicide

print(males_percent_2014.__round__(2), '% males committed suicide from the year 2012 to 2014')
print(females_percent_2014.__round__(2), '% females committed suicide from the year 2012 to 2014 \n')

# a bar chart with the collective information of all the 3 years
N = 2  # value of
ind = np.arange(N)  # creating a range for values
width = 0.25

info1 = gender_counts_2012
graph1 = plt.bar(ind, info1, width)

info2 = gender_counts_2013
graph2 = plt.bar(ind + width, info2, width)

info3 = gender_counts_2013
graph3 = plt.bar(ind + width * 2, info3, width)

plt.xlabel("Year")
plt.ylabel('Number of Demises')
plt.title('Suicides as per the Gender for year 2012 to 2014')

plt.xticks(ind + width, ['Males', 'Females'])
plt.legend((graph1, graph2, graph3), ('2012', '2013', '2014'))
plt.show()

print('-------------------------------------------------------------------------------------------------------------\n')


# RACE STATISTICS VARIANCE OVER THE YEARS-------------------------------------------------------------------------------
# Using the earlier defined functions to add values to the counters
# YEAR 2012
race_2012 = [0, 0, 0, 0, 0]
race_counter(df1, race_2012)
print('The count of suicides per racial class in year 2012 is \n', df1['race'].value_counts(), '\n')

# YEAR 2013
race_2013 = [0, 0, 0, 0, 0]
race_counter(df2, race_2013)
print('The count of suicides per racial class in year 2013 is \n', df2['race'].value_counts(), '\n')

# YEAR 2014
race_2014 = [0, 0, 0, 0, 0]
race_counter(df3, race_2014)
print('The count of suicides per racial class in year 2014 is \n', df3['race'].value_counts(), '\n')

# a bar chart with the collective information of all the 3 years
N = 5  # value of
ind = np.arange(N)  # creating a range for values
width = 0.25

info1 = race_2012
graph1 = plt.bar(ind, info1, width)

info2 = race_2013
graph2 = plt.bar(ind + width, info2, width)

info3 = race_2014
graph3 = plt.bar(ind + width * 2, info3, width)

plt.xlabel("Year")
plt.ylabel('Number of Demises')
plt.title("Suicides trends w.r.t to Race for 2012 to 2014")

plt.xticks(ind + width, ['Asian/Pacific Islander', 'Native American/Native Alaskan', 'White', 'Black', 'Hispanic'])
plt.legend((graph1, graph2, graph3), ('2012', '2013', '2014'))
plt.show()

print('-------------------------------------------------------------------------------------------------------------\n')

# EDUCATION STATISTICS VARIANCE OVER THE YEARS--------------------------------------------------------------------------
# Using the earlier defined functions to add values to the counters
# YEAR 2012
education_2012 = [0, 0, 0, 0, 0]
education_counter(df1, education_2012)
print('The count of suicides per educational qualification in year 2012 is \n', df1['education'].value_counts(), '\n')

# YEAR 2013
education_2013 = [0, 0, 0, 0, 0]
education_counter(df2, education_2013)
print('The count of suicides per educational qualification in year 2013 is \n', df2['education'].value_counts(), '\n')

# YEAR 2014
education_2014 = [0, 0, 0, 0, 0]
education_counter(df3, education_2014)
print('The count of suicides per educational qualification in year 2014 is \n', df3['education'].value_counts(), '\n')

# a bar chart with the collective information of all the 3 years
N = 5  # value of
ind = np.arange(N)  # creating a range for values
width = 0.25

info1 = education_2012
graph1 = plt.bar(ind, info1, width)

info2 = education_2013
graph2 = plt.bar(ind + width, info2, width)

info3 = education_2014
graph3 = plt.bar(ind + width * 2, info3, width)

plt.xlabel("Year")
plt.ylabel('Number of Demises')
plt.title("Suicides trends w.r.t to Educational Qualification for 2012 to 2014")

plt.xticks(ind + width, ['BA+', 'Some College', 'HS/GED', 'Unknown', 'Less than HS'])
plt.legend((graph1, graph2, graph3), ('2012', '2013', '2014'))
plt.show()

print('-------------------------------------------------------------------------------------------------------------\n')
