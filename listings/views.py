from django.http import JsonResponse

def hello_world(request):
    return JsonResponse({"message": "Welcome to ALX Travel App Listings API"})

