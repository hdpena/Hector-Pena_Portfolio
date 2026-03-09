# DSC 510
# Week 10
# Programming Assignment 10.2 Final Assignment
# Author Hector Pena
# 8/12/2022


import requests
import json
import time

# display welcome message to user
print('Welcome User to the Weather Lookup System!\n'
      "For a forcast of a precise location, please enter the Zip Code for the location \n"
      "or enter the city's name followed by a comma, and 2-letter state code.\n"
      "Examples include: Las Vegas, NV; Hawthorne, CA, 90201, 90240, etc.\n"
      "Have fun looking up weather! \n")


# define main function, allow users to input location data for weather lookup, set url for api key and get requests
def main():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    url_2 = 'https://api.openweathermap.org/data/2.5/forecast'
    weather_location = input('Please enter the Location you wish to Lookup: ')
    while True:
        try:
            current_weather(weather_location, url)
            extended_weather(weather_location, url_2)
            print('')
            more_weather()
            break
        except LookupError:
            print('')
            more_weather()
            break


# set a get request to the url to verify connection and display the data
def current_weather(location, url):
    if location.isdigit() is True:
        weather_params = {'zip': location, 'APPID': 'aeb2fb28b46ce2e44d355176c5c24dbc'}
    else:
        weather_params = {'q': location, 'APPID': 'aeb2fb28b46ce2e44d355176c5c24dbc'}
    response = requests.get(url, params=weather_params)
    try_web(response, location)
    if response.status_code == 200:
        print('Connection Successful----------Location Was Found')
    current_parsed = json.loads(response.text)
    current_formatted(current_parsed)


def extended_weather(location, url_ext):
    """Makes a GET request to the url for extended forecast, parses and displays the data"""
    if location.isdigit() is True:
        query_params = {'zip': location, 'cnt': 16, 'APPID': 'aeb2fb28b46ce2e44d355176c5c24dbc'}
    else:
        query_params = {'q': location, 'cnt': 16, 'APPID': 'aeb2fb28b46ce2e44d355176c5c24dbc'}
    response = requests.get(url_ext, params=query_params, timeout=10)
    try_web(response, location)
    ext_parsed = json.loads(response.text)
    ext_formatted(ext_parsed)


# convert temperature data to Fahrenheit, Celsius
def converted_temp(temp):
    f_degree = round((((temp - 273.15) * 9) / 5) + 32)
    c_degree = round(temp - 273.15)
    return f'{f_degree}{chr(176)}F / {c_degree}{chr(176)}C'


def try_web(response, location):
    """Try Except block to test the request was successful, additionally checking if the city or
    zip code entered is valid by using 404 status code"""
    try:
        response.raise_for_status()
    except requests.HTTPError as error0:
        if response.status_code == 404:
            if location.isdigit() is True:
                print(f"The zip code entered '{location}' was not found or is not valid.")
            else:
                if location.__contains__(','):
                    print(f"The city entered '{location[0:-2].title() + location[-2:].upper()}' was not found.")
                else:
                    print(f"The city entered '{location.title()}' was not found.")
        else:
            print('Even we do not have access to single digit zip codes.')
            print(f'{error0}')
    except requests.ConnectionError as error1:
        print('Connection Error')


# decodes the json data, define current formatted weather data as well as print data in nicely formatted manner
def current_formatted(parsed):
    city = str(json.dumps(parsed['name'])).replace('"', '')
    country = str(json.dumps(parsed['sys']['country'])).replace('"', '')
    timezone = int(json.dumps(parsed['timezone']))
    data_time = int(json.dumps(parsed['dt']))
    true_time = data_time + timezone
    current_time = time.strftime("%A, %b %d, %Y %I:%M %p (local time)", time.gmtime(true_time))
    temp = float(json.dumps(parsed['main']['temp']))
    conditions = str(json.dumps(parsed['weather'][0]['description'])).replace('"', '').title()
    print(f'Weather Report for {city}, {country} \n'
          f'Current Data: {current_time}:\n'
          f'Current Temperature: {converted_temp(temp)}\n'
          f'Current Conditions:: {conditions}\n')


# decode the json time data, run a loop to pull data from every 6 hours to return a roughly 36hr forcast, format data
# ask user if they would like a 36hr forecast for the location they selected
def ext_formatted(parsed):
    print(f"{'36 Hour Forecast:':28}{'Temperature:':24}{'Conditions:'}")
    for i in range(1, 15):
        temp = float(json.dumps(parsed['list'][i]['main']['temp']))
        conditions = str(json.dumps(parsed['list'][i]['weather'][0]['description'])).replace('"', '').title()
        time_data = int(json.dumps(parsed['list'][i]['dt']))
        timezone = int(json.dumps(parsed['city']['timezone']))
        correct_time = time_data + timezone
        future_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime(correct_time))
        print(f'{future_time:30}{converted_temp(temp):22}{conditions}')


# define more_weather function to allow users to look up another location with a loop
def more_weather():
    weather_again = str(input('Would you like to enter another location, Yes or No? ')).lower().strip()
    while not (weather_again == 'yes' or weather_again == 'no'):
        option = str(input('You did not enter a valid selection.\n'
                           'Please enter Yes to search another location or No to exit: ')).lower().strip()
    if weather_again == 'yes':
        print('')
        main()
    if weather_again == 'no':
        print('Thank you for using weather lookup! Have a good day!')


if __name__ == "__main__":
    main()
