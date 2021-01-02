
#Sites and videos that helps me: 
#Practice solutions at the classroom.
#https://thehelloworldprogram.com/python/python-string-methods/
#https://www.youtube.com/watch?v=vmEHCJofslg&t=3147s
#https://stackoverflow.com/questions/59489348/filling-a-dictionary-with-multiple-user-input
#https://www.youtube.com/watch?v=BITjlIWiPso

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs    
    
    city_name = ""
    
    while True:
        city = input('Would you like to see data for chicago, new York, or washington? ').lower()
        try:
            if city.lower() in ['chicago','new york','washington']:
                break
        except:
            print("invalid inputs, please try again")
            city = input('Would you like to see data for chicago, new York, or washington? ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)

    month_name = ""
   
    while True:
        month = input('Do you want to filter by any month? from january to june or all?  ').lower()
        try:
            if month.lower() in ['all', 'january', 'february', 'march', 'april', 'may', 'june']: 
                break
        except:
            print("invalid inputs, please try again")
            month = input('Do you want to filter by any month? from january to june or all? ').lower()
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    day_name = ""
    while True:
        day = input('Do you want to filter by any day? or all? ').lower()
        try:
            if day.lower() in ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']:
                break
        except:
            print("invalid inputs, please try again")
            day = input('Do you want to filter by any day? or all? ').lower()
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

   
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month from the given fitered data is: " + str(common_month))

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week from the given fitered data is: "+ str(common_day_of_week))

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour from the given fitered data is: " + str(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: " + common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: " + common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station']+df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is :  " + str(frequent_combination))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: " + str(total_travel_time))


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: " + str(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of User Types  is: " + str(user_types))


    # TO DO: Display counts of gender
    if city != 'washington':
        Gender = df['Gender'].value_counts()
        print("The count of Gender is: " + str(Gender))
  # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print('Earliest year of birth from the given fitered data is: '+ str(earliest_birth))
        print('Most recent birth from the given fitered data is: '+ str(most_recent_birth))
        print('Most common birth from the given fitered data is:  '+ str(most_common_birth))
    elif city == 'washington':
        print('This city does not contain the year of birth or gender')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """ Displays raw data on user request. """
    start_loc = 0
    while True:
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        if view_data.lower() != 'yes':
            return
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
            


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        while True:
            view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
            if view_data.lower() != 'yes':
                break
            display_data(df)
            break
      
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

