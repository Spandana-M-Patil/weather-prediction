# Weather API Script

This repository contains a Python script to fetch and display the current weather information for a given city using the WeatherAPI.

## Features

- Takes city name as input from the user
- Fetches current weather data including location, local time, temperature, and weather condition.
- Handles various errors such as network issues, JSON decoding errors, and data extraction errors.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone this repository:

```sh
git clone https://github.com/yourusername/weather-api-script.git
cd weather-api-script
```
2. Install the required Python library:
```bash
pip install requests
```
## Usage
1. Replace <YOUR_API_KEY> with your actual api key from WeatherAPI.
2. Run the script
```bash
python script.py
```
3. Enter the name of the city when prompted.
## Example
```bash
Enter the city name: bangalore
Location : Bangalore
Local time : 2024-06-16 12:52
Temperature : 29.4 C
Condition : Partly cloudy
```
## Error Handling
- **Network Error:** Occurs when there is a network-related issue.
- **JSON Decoding Error:** Occurs when there is an issue with decoding the JSON response.
- **Data Extraction Error:** Occurs when the expected data is not found in the response.
