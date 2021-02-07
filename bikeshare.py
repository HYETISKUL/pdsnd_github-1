import time

import pandas as pd

import numpy as np





CITY_DATA = { 'chicago': 'chicago.csv',

              'new york city': 'new_york_city.csv',

              'washington': 'washington.csv' }



MONTH_DATA = {'january', 'february', 'march', 'april', 'may', 'june', 'all'}



DAY_DATA = {'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'}





def get_filters():

    """

    Asks user to specify a city, month, and day to analyze.



    Returns:

        (str) city - name of the city to analyze

        (str) month - name of the month to filter by, or "all" to apply no month filter

        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    """

    print('Hi there! Let\'s explore some US bikeshare data!')



    # get specified city  

    while True:

        city = input('Which city would you like hear about?\n').lower()

        if city in CITY_DATA:

            city

            print("\nGreat Choice! Now it is time to pick a month.\n")

            break

        else:

            print("\nOops! Looks like you didn't type in one of the stored cities! Try again!")

    

    print('-'*40)

    

    # get specified month  

    while True:

        month = input('Which month would you like hear about?\n').lower()

        if month in MONTH_DATA:

            month

            print("\nGood One! Now it is time to pick a day.\n")

            break

        else:

            print("\nOops! Looks like you didn't type in one of the stored months! Try again!")  



    print('-'*40)

    

    # get specified day 

    while True:

        day = input('Which day would you like hear about?\n').lower()

        if day in DAY_DATA:

            day

            print("\n Good to go! Now it is time to make some calculations.\n")

            break

        else:

            print("\nOops! Looks like you didn't type in one of the stored days! Try again!")  



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

    # load data file into a dataframe

    df = pd.read_csv(CITY_DATA[city])



    # convert the Start Time column to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])



    # extract month, day of week and hour from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    df['hour'] = df['Start Time'].dt.hour



    # filter by month if applicable

    if month != 'all':

        # use the index of the months list to get the corresponding int

        months = ['january', 'february', 'march', 'april', 'may', 'june']

        month = months.index(month) + 1



        # filter by month to create the new dataframe

        df = df[df['month'] == month]



    # filter by day of week if applicable

    if day != 'all':

        # filter by day of week to create the new dataframe

        df = df[df['day_of_week'] == day.title()]





    return df





def time_stats(df):

    """Displays statistics on the most frequent times of travel."""



    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()



    # display the most common month

    month_dict= {'1': 'January', '2': 'February', '3': 'March',

                 '4': 'April', '5': 'May','6': 'June'}

    

    common_month = df['month'].mode()[0]

    common_month = month_dict[str(common_month)]

    print("The Most Common Month: {}".format(common_month))





    # display the most common day of week

    common_day = df['day_of_week'].mode()[0]

    print("The Most Common Day of the Week: {}".format(common_day))





    # display the most common start hour

    common_hour = df['hour'].mode()[0]

    print('The Most Common Start Hour: {}'.format(common_hour))





    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)





def station_stats(df):

    """Displays statistics on the most popular stations and trip."""



    print('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = time.time()



    # display most commonly used start station

    start_station = df['Start Station'].mode()[0]

    print('The Most Commonly Used Start Station: {}'.format(start_station))





    # display most commonly used end station

    end_station = df['End Station'].mode()[0]

    print('The Most Commonly Used End Station: {}'.format(end_station))



    # display most frequent combination of start station and end station trip

    combined_stations = df.groupby(['Start Station', 'End Station']).size().sort_values(axis=0, ascending=False).reset_index(name="counts")

    

    frequent_start_station = combined_stations['Start Station'][0]

    frequent_end_station = combined_stations['End Station'][0]



    print('Start Station of The Most Frequent Combination: {}'.format(frequent_start_station))

    print('End Station of The Most Frequent Combination: {}'.format(frequent_end_station))



    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)





def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""



    print('\nCalculating Trip Duration...\n')

    start_time = time.time()



    # display total travel time

    total_travel_time = df['Trip Duration'].sum()

    m, s = divmod(total_travel_time, 60)

    h, m = divmod(m, 60)

    print('Total Travel Time: {} hours {} minutes {} seconds'.format(h, m, s))





    # display mean travel time

    mean_travel_time = df['Trip Duration'].mean()

    print('Mean Travel Time: {} seconds'.format(mean_travel_time))





    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)





def user_stats(df):

    """Displays statistics on bikeshare users."""



    print('\nCalculating User Stats...\n')

    start_time = time.time()



    # Display counts of user types

    user_type_count = df["User Type"].value_counts()

    print('User Type Count:\n{}'.format(user_type_count))



    # Display counts of gender

    if 'Gender' in df.columns:

        gender_count = df['Gender'].value_counts()

        print('Gender Count:\n{}'.format(gender_count))

    else:

        print('Unfortunately, there is no gender info in the dataset.')





    # Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:

        earliest_birth_year = df['Birth Year'].min()

        latest_birth_year = df['Birth Year'].max()

        common_birth_year = df['Birth Year'].mode()

        

        print('The Earliest Year of Birth: {}'.format(earliest_birth_year))

        print('The Most Recent Year of Birth: {}'.format(latest_birth_year))    

        print('The Most Common Year of Birth: {}'.format(common_birth_year))       

        

    else:

        print('Unfortunately, there is no birth year info in the dataset.')



    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)



def show_rows(df):

    """

    Displays raw data from the csv files.

    It shows 5 rows of data for each time user input is "yes"

    

    """

    

    #get the user input

    user_input=input("All done! Do you want to see the first 5 rows of data? Please enter 'yes' or 'no'\n").lower()

    

    #start from the first row

    start_loc = 0

    

    #keep showing 5 rows until the user input is no 

    while user_input=='yes':

        

        print(df.iloc[start_loc:start_loc+5])

        start_loc += 5

        view_display = input("Do you wish to continue?: ").lower()

        if view_display != 'yes':

            break #break out of while loop above

        



def main():

    while True:

        city, month, day = get_filters()

        df = load_data(city, month, day)



        time_stats(df)

        station_stats(df)

        trip_duration_stats(df)

        user_stats(df)

        show_rows(df)



        restart = input('\nWould you like to restart? Enter yes or no.\n')

        if restart.lower() != 'yes':

            break





if __name__ == "__main__":

	main()