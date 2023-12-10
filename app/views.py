from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
    print(request.method, request.user)
    # return HttpResponse("hi")
    return render(request, "home.html")