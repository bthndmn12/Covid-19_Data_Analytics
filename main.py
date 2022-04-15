import pandas as pd

vacc = pd.read_csv('country_vaccination_stats.csv')


#------------------------QUESTION4--------------------------------
print(vacc.isnull().sum().sum())
vacc['daily_vaccinations'] = vacc['daily_vaccinations'].fillna(0)
print(vacc.isnull().sum().sum())
#-----------------------------------------------------------------


#------------------------QUESTION5--------------------------------
median = vacc[['country', 'daily_vaccinations']].groupby('country').median()
median.to_csv('median.csv')
median_vacc = pd.read_csv('median.csv')
print(median_vacc.nlargest(3,'daily_vaccinations'))
#-----------------------------------------------------------------

#------------------------QUESTION6--------------------------------
dates = vacc[['date', 'daily_vaccinations']].groupby('date').sum()
dates.to_csv('datevacc.csv')
date_vaccs = pd.read_csv('datevacc.csv')
print(date_vaccs.loc[date_vaccs['date']== '1/6/2021'])
#-----------------------------------------------------------------

