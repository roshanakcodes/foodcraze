from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Favourite
import requests

# Create your views here.
@login_required(login_url='userauth:login')
def fav(request):
    if request.method == "POST":
        fav_id = request.POST.get('id')
        already_exists = Favourite.objects.filter(user=request.user, meal_id=fav_id).exists()
        if not already_exists:
            url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={fav_id}"
            response = requests.get(url)
            data = response.json()

            if data.get('meals'):
                meal_details = data['meals'][0]
                Favourite.objects.create(
                    meal_id=fav_id,
                    user=request.user,
                    name=meal_details['strMeal'],
                    image_url=meal_details['strMealThumb'],
                    category=meal_details['strCategory'],
                    cuisine=meal_details['strArea'],
                    youtube_url=meal_details['strYoutube'],
                    source_url=meal_details['strSource']
                )
        return redirect(request.META.get('HTTP_REFERER', 'userauth:index'))
    else:
        user_favourites = Favourite.objects.filter(user=request.user)
        context = {
          'tasks_list': user_favourites
        }
        return render(request, "userauth/home.html", context)


def remove_fav(request, id):
    Favourite.objects.filter(user=request.user, id=id).delete()
    return redirect('userauth:dash')
