import pandas as pd


data = pd.read_csv('italy-covid-daywise.csv', sep=',')


data['date'] = pd.to_datetime(data['date'])

# Get user input
date = input("\nEnter Date (YYYY-MM-DD): ")


frame = {'date': [date]}
frame1 = pd.DataFrame(frame)


frame1['date'] = pd.to_datetime(frame1['date'])

# Extracting date information
day_name = frame1['date'].dt.day_name().iloc[0]
day_of_week = frame1['date'].dt.day_of_week.iloc[0]
day_of_year = frame1['date'].dt.day_of_year.iloc[0]

print(frame1)
print(f'\nDay on {date}: {day_name}\nIt was the {day_of_week+1} day of the week\nIt was the {day_of_year} day of the year.')
