from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
import random


def index(request):
    return HttpResponse("probando ninjagold")


def ninjagold(request):
    if "counter" not in request.session:
        request.session["counter"] = 0
    if "activities" not in request.session:
        request.session["activities"] = []
    return render(request, "home.html")


def goldengain(request, place):
    if place == "Farm":
        new_gold = random.randint(10, 20)
    elif place == "Cave":
        new_gold = random.randint(5, 10)
    elif place == "House":
        new_gold = random.randint(3, 5)
    else:
        new_gold = random.randint(-50, 50)
    request.session["counter"] += new_gold
    if new_gold >= 0:
        request.session["activities"].append(
            {
                "txtbox": f"- You WON {new_gold} golds at {place}",
                "counter": new_gold,
            }
        )
    else:
        request.session["activities"].append(
            {
                "txtbox": f" - You LOST {new_gold} golds at {place} :(",
                "counter": new_gold,
            }
        )
    request.session.save()
    return redirect("/ninjagold")


def reset(request):
    request.session.flush()
    return redirect("/ninjagold")
