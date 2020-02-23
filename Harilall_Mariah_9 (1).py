cities = ['new york','boston','philidelphia','atlanta']
print('Your Weather Report')
print()
print('Current observations are available for: \n- New York \n- Boston \n- Philidelphia \n- Atlanta')
cities = ['new york','boston','philidelphia','atlanta']

#prompt user
user_city = input('Enter the city you would like a weather report for: ').lower()
while user_city not in cities:
    user_city = input('No data available. Please enter another city: ').lower()

print()
print('Accessing weather data...')
print()

#access web 
import urllib.request

if user_city == 'new york':
    url = "https://w1.weather.gov/xml/current_obs/display.php?stid=KJRB"
elif user_city == 'boston':
    url = 'https://w1.weather.gov/xml/current_obs/display.php?stid=KBOS'
elif user_city == 'philidelphia':
    url = 'https://w1.weather.gov/xml/current_obs/display.php?stid=KPHL'
elif user_city == 'atlanta':
    url = 'https://w1.weather.gov/xml/current_obs/display.php?stid=KFFC'
try:
    response = urllib.request.urlopen( url )
    alldata = response.read().decode('utf-8')
except:
    print('Sorry could not access data for', user_city)
else:
    print('The current weather has been accessed for', user_city)

#Gather data
words = alldata.split('\n')
location = words[24][11:-11]
weather = words[30][10:-10]
temp = words[31][21:-22]
humidity = words[34][20:-20]+'%'
wind = words[35][14:-14]
observation = words[28][19:-20]

#Put data into dictionary
city_weather = {'location':location,
                'weather':weather,
                'temperature':temp,
                'humidity':humidity,
                'wind':wind,
                'observation':observation}

#Prompt user for what data they would like
print()
print('Information available:\n- Location\n- Weather\n- Temperature\n- Humidity\n- Wind\n- Observation')
print()

while True:
    user_info = input('What weather information would you like? Or, to end, enter "done". ').lower()
    if user_info in city_weather:
        print('The', user_info, 'in', user_city,'is', city_weather.get(user_info))
    elif user_info == 'done':
        print('Okay all done!')
        break
    else:
        print('That data is not available.')

print()
user_file = input('Would you like to export the full weather report? (yes/no) ')

#Close previous file and write to new one
response.close()

if user_file == 'yes':    
    #Iterate over each line in file and evaluate the data
    weather_file = open('WeatherReport.txt','w+')
    weather_file.write('Weather for '+user_city)
    weather_file.write('\n')
    for key, value in city_weather.items():
        weather_file.write(key)
        weather_file.write(': ')
        weather_file.write(value)
        weather_file.write('\n')
    weather_file.close()
    print('Your weather report has been stored in an external file!')

elif user_file == 'no':
    print()
     






