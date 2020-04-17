## Project #1  - Bikesharing prediction.

###  Background

We are going to work on a problem that will help us to get insights about a new generation or way to use bikes on a city through Bike sharing Systems. 

This systems allow users of a city to rent a bike, ride it from a particular position and return it, the system is not only great but it has richful information about when the bike was taken and where it  was returned , therefore it's helpful for having data about mobility in the city. 

The idea of the project is to be able to predict the bike sharing data based on the data extracted from: [Capital Bikeshare System](http://capitalbikeshare.com/system-data), a system for renting bikes available in Washington, DC. United States.

### Dataset background

Before starting diving down to the project, It's really good to get an understanding of the data you are handling. 

In this case we are dealing with information about riderhip on  bike service system described on the previous section, the data constains details from 2011 and 2012 and aggregted counts hourly and daily. 

- Total of records for hourly dataset: 17379 hours

#### Characteristics of the data
	
Both hour.csv and day.csv have the following fields, except hr which is not available in day.csv
	
- instant: record index
- dteday : date
- season : season (1:springer, 2:summer, 3:fall,4:winter)
- yr : year (0: 2011, 1:2012)
- mnth : month ( 1 to 12)
- hr : hour (0 to 23)
- holiday : weather day is holiday or not(extracted from http://dchr.dc.gov/pageholiday-schedule)
- weekday : day of the week
- workingday : if day is neither weekend norholiday is 1, otherwise is 0.
- weathersit : 
	- 1: Clear, Few clouds, Partly cloudy, Partly cloudy
	- 2: Mist + Cloudy, Mist + Broken clouds, Mist+ Few clouds, Mist
	- 3: Light Snow, Light Rain + Thunderstorm +Scattered clouds, Light Rain + Scattered clouds
	- 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
- temp : Normalized temperature in Celsius. The values are divided to 41 (max)
- atemp: Normalized feeling temperature in Celsius. The values are divided to 50 (max)
- hum: Normalized humidity. The values are dividedto 100 (max)
- windspeed: Normalized wind speed. The values aredivided to 67 (max)
- casual: count of casual users
- registered: count of registered users
- cnt: count of total rental bikes including both casual and registered