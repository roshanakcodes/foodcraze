from django.shortcuts import render
import requests

def index(request):
    query = request.GET.get('q', '') 
    if query:
        url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"
    else:
        url = "https://www.themealdb.com/api/json/v1/1/random.php"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        meals = data.get('meals')
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}") 
        meals = None
    context = {
        'meals': meals,
        'search_term': query,
    }
    return render(request, "foodapi/mainapi.html", context)