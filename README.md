# NBA MVP API
This API contains information regarding every NBA MVP in history, 
obtained via 4 different endpoints.

## Endpoints
**All endpoints implement a `GET` method**

* `/getbasicstats` - This endpoint will return a JSON containing
basic stats from every MVP season.
* `/getadvancedstats` - This endpoint will return a JSON containing
advanced stats from every MVP season.
* `/getplayerbasicstats/<player>/<season>` - This endpoint will return a JSON containing
basic stats from a specified `player` and `season`. The `player` parameter
expects first and last name capitalized and separated by a space `Stephen Curry`. The `season` parameter
expects an input of the format `XXXX-XY`, for example `2015-16`.
* `/getplayeradvancedstats/<player>/<season>` - This endpoint will return a JSON containing
advanced stats from a specified `player` and `season`. The `player` parameter
expects first and last name capitalized and separated by a space `Stephen Curry`. The `season` parameter
expects an input of the format `XXXX-XY`, for example `2015-16`.
* `/update_stats` (POST) - This endpoint allows adding a new column or updating an existing column for a specific player and season in the specified CSV file. It accepts JSON input containing details about the CSV file, player, season, column, and the new value. This endpoint does not implement the GET method.

## Making GET Requests
Making requests to the API requires the URL and any parameters required by the endpoint.
To make valid `HTTP` requests from your python application, make sure to import the requests
library:

```import requests```

If you do not have the `requests` library installed, install it using `pip`:

```!pip install requests```

Once you have the `requests` library imported, copy and paste this URL and store it in 
a variable:

https://popular-yeti-subtly.ngrok-free.app/

Additionally, in order to make requests via one of the endpoints, make sure to 
specify the endpoint after the last `/` like so:

```
base_url = 'https://popular-yeti-subtly.ngrok-free.app/
url = f"{base_url}getbasicstats"
```

If your endpoint requires parameters, put those parameters into a dictionary and
pass in the dictionary in the `params` argument like so:

```
params = {
    'player': 'LeBron James', 
    'season': '2012-13'
} 

response = requests.get(url, params=params)
```

You can retrieve the data and turn it into a `pandas` dataframe like so:

```
data = response.json()
df = pd.DataFrame(data)
```

If you haven't imported `pandas`, make sure to do that as well.

## Making POST Requests
The `update_stats` endpoint takes in the following parameters:
* "csv_file"
* "player_name"
* "season"
* "column_name"
* "new_value"

This allows the user to update a particular stat within a specific `.csv` file for a particular player's MVP season. Here is an example of adding a "Team Wins"
column and updating Stephen Curry's 2015-16 team wins value.

```
post_url = f'{base_url}update_stats'

# Headers to indicate that the content type is JSON
headers = {
    'Content-Type': 'application/json'
}

# Data to be sent in JSON format
data = {
    "csv_file": "mvp_basic_stats.csv",
    "player_name": "Stephen Curry",
    "season": "2014-15",
    "column_name": "Team Wins",
    "new_value": 67
}

# Sending the POST request
response = requests.post(post_url, json=data, headers=headers)

# Checking the response from the server
if response.status_code == 200:
    print('Success!')
    print(response.json())  # Print the JSON response from the server
else:
    print('Failed to make the request:', response.status_code)
    print(response.text)  # Print the text response from the server```
