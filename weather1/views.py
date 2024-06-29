from django.shortcuts import render

def index(request):
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8c59428e6f5bb0ce710e1cabd82f1ec4'

    city = 'Las Vegas'

    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
    return render(request, 'weather1/index.html') #returns the index.html template
