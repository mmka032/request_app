import requests

url = "https://weather.tsukumijima.net/api/forecast"

params = {
    "大阪": "270000",
    "兵庫": "280010",
    "奈良": "290010",
    "和歌山": "300010",
    "京都": "260010",
    "滋賀": "250010",
    "三重": "240010"
}

params2 = {
    "city": "270000"
}

def fetch_weather(place):
    response = requests.get(url, params={"city":place})
    deta = response.json()

    prefecture = deta["location"]['prefecture']
    date = deta["forecasts"][0]["date"]
    image = deta["forecasts"][0]["image"]["url"]
    fetch_image = requests.get(image).text
    weather = deta["forecasts"][0]["detail"]["weather"]
    max = deta["forecasts"][0]["temperature"]["max"]["celsius"]
    min = deta["forecasts"][0]["temperature"]["min"]["celsius"]

    context = {
        "prefecture": prefecture,
        "date": date,
        "image": fetch_image,
        "weather": weather,
        "max": max,
        "min": min,
    }

    print(context)

    return context
