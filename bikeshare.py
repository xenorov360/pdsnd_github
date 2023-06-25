import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}


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
    while True:
        city = input("Please enter the city you would like to analyze (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Please enter a valid city name from the list.\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter an input month (January, February, March, April, May, June), or 'All' for no prefercne: ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("Please enter a valid month from the list.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please select day of the week to filter from (Monday, Tuesday, Wednesday ... Friday), or 'All' for no preference: ").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("Please enter valid day of week from the list. \n")

    print('-' * 40)
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
    file = CITY_DATA[city]
    df = pd.read_csv(file)

    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()

    # For tackling 'All' value in Month and Day Of Week Parameter
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]

    
    if day != 'all':
        df = df[df['Day of Week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Month'].mode()[0]
    print(f"Most Common Month is {common_month}")

    # TO DO: display the most common day of week.
    common_day = df['Day of Week'].mode()[0]
    print(f"Most Common Day of Week is {common_day}")

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    common_hour = df['Hour'].mode()[0]
    print(f"Most Common Start Hour is {common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"Most Commonly Used Start Station is {common_start_station}")

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"Most Commonly Used End Station is {common_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_station_combo = df['Station Combination'].mode()[0]
    print(f"Most Common Trip is between {common_station_combo}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    minute,second = divmod(total_travel_time,60)
    hour,minute = divmod(minute,60)
    print(f"Total Travel Time is {hour} Hour(s) {minute} Minute(s) and {second} Second(s)")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    minute,second = divmod(mean_travel_time,60)
    hour,minute = divmod(minute,60)
    print(f"Mean Travel Time is {hour} Hour(s) {minute} Minute(s) and {second} Second(s)")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of User Types:\n")
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of Gender:\n")
        print(gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])

        print("\nBirth Year Statistics for the Passengers:")
        print(f"Earliest Year of Birth: {earliest_year}")
        print(f"Most Recent Year of Birth: {recent_year}")
        print(f"Most Common Year of Birth: {common_year}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def display_data(df):
    ### Display granular level data if needed by user
    print(df.head())
    next = 0
    while True:
        raw_data = input("Would you like to view next 5 rows of data ? Please enter Yes/No.")
        if raw_data.lower()!= 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        while True:
            raw_data = input("Would you like to see first 5 rows of data ? Please enter Yes/No.")
            if raw_data.lower() != 'yes':
                break
            display_data(df)
            break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
