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

## Making Requests
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

`url = 'https://popular-yeti-subtly.ngrok-free.app/getbasicstats`

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
