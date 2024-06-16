import requests
import json

user = input('Enter the city name: ')
api_key = '<YOUR_API_KEY>'
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={user}'
response = requests.get(url)

def weatherResult():
    my_dict = {}
    try:
        if response.status_code == 200:
            content_str = response.content.decode('UTF-8')
            data = json.loads(content_str)
            my_dict['Location '] = data['location']['name']
            my_dict['Local time '] = data['location']['localtime']
            my_dict['Temperature '] = f'{data['current']['temp_c']} C'
            my_dict['Condition '] = data['current']['condition']['text']
            for key, value in my_dict.items():
                print(f'{key}: {value}')
        else:
            print('Sorry, we can\'t find the city name.')

    except requests.exceptions.RequestException as e:
        print('Network Error: ',e)
        return None
    
    except json.JSONDecodeError as j:
        print('Json decodeing Error: ',j)
        return None
    
    except KeyError as k:
        print('Data extraction Error: ',k)
        return None

weatherResult()
