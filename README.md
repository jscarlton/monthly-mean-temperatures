# Monthly Mean Temperatures

## Introduction
This is a Python script to download the monthly mean temperatures at a user-supplied airport weather station for a user-supplied range of years. The script uses `urllib` to query [Weather Underground] (http://www.wunderground.com). It does not require Weather Underground API access.

## Usage
When you execute the script, it will ask you for the following:

1. A 4-letter [ICAO](https://en.wikipedia.org/wiki/International_Civil_Aviation_Organization_airport_code) airport code. Wikipedia has a list of airport codes for the [contiguous United States](https://en.wikipedia.org/wiki/List_of_airports_by_ICAO_code:_K), [Alaska](https://en.wikipedia.org/wiki/List_of_airports_by_ICAO_code:_P#PA), and [Hawaii](https://en.wikipedia.org/wiki/List_of_airports_by_ICAO_code:_P#PH_-_Hawaii). Note that Weather Underground may not have data for all of the stations. I haven't found any where they don't, but I haven't exhaustively tested, either
2. A starting year. The Weather Underground database goes from 1948–present, although there may be missing months or years for some stations.
3. An ending year. This can be the same as the starting year. If your ending year is earlier than your starting year, the script will execute but nothing will happen.

Once you enter a station, starting, and ending year, the script will create a data directory (assuming it doesn't already exist) and create a file called historicalMonthlyMeans\_STATION\_STARTYEAR-ENDYEAR.csv. The csv will have the year, month, station, and mean temperature for the years that you entered.

Note that the script is slow since it runs each query one after another. Patience: still virtuous.