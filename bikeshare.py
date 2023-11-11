import time
import pandas as pd
import numpy as np

# code begins
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    #let's  Initialize variables to store user inputs
    city = ''
    month = ''
    day = ''

     # Define valid options for city, month, and day
    valid_cities = list(CITY_DATA.keys())
    valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # Getting user input for city (case-insensitive)
    while city.lower() not in valid_cities:
        city = input('Enter the name of the city (Chicago, New York City, Washington): ').lower()

    # Getting user input for month (case-insensitive)
    while month.lower() not in valid_months:
        month = input('Enter the name of the month (all, January, February, ..., June): ').lower()

    # Getting user input for day of the week (case-insensitive)
    while day.lower() not in valid_days:
        day = input('Enter the name of the day of the week (all, Monday, Tuesday, ..., Sunday): ').lower()

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
    file_name = CITY_DATA[city]
    df = pd.read_csv(file_name)

    # Convert the 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract the month and day of the week into separate columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month != 'all':
        month_num = months.index(month) + 1  # Convert month name to month number
        df = df[df['month'] == month_num]

    # Filter by day of the week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()] 


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month for travel is:', common_month)


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of the week for travel is:', common_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour for travel is:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is:', common_start_station)

     # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is:', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    #let's Create a new column 'Trip' by combining 'Start Station' and 'End Station'
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    
    #Now, we can display most frequent combination of start and end station trip
    common_trip = df['Trip'].mode()[0]
    print('The most frequent combination of start and end stations is:', common_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time in seconds:', total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time in seconds:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_counts = df['User Type'].value_counts()
    print('Counts of User Types:\n', user_types_counts)


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of Genders:\n', gender_counts)
    else:
        print('\nGender data not available for this city.')


    # TO DO: Display earliest, most recent, and most common year of birth
    # Check if 'Birth Year' column exists in the DataFrame
    if 'Birth Year' in df.columns:
        # Display earliest birth year
        earliest_birth_year = int(df['Birth Year'].min())
        print('\nEarliest Birth Year:', earliest_birth_year)

        # Display most recent birth year
        most_recent_birth_year = int(df['Birth Year'].max())
        print('Most Recent Birth Year:', most_recent_birth_year)

        # Display most common birth year
        most_common_birth_year = int(df['Birth Year'].mode().values[0])
        print('Most Common Birth Year:', most_common_birth_year)
    else:
        print('\nBirth year data not available for this city.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    """
    Displays raw data upon request by the user, showing 5 rows at a time.

    Args:
        df - Pandas DataFrame containing city data
    """
    start_loc = 0

    while True:
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no: ").lower()

        if view_data == 'yes':
            end_loc = start_loc + 5
            print(df.iloc[start_loc:end_loc])
            start_loc = end_loc
        else:
            break    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

# code ends
