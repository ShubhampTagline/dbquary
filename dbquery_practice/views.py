from django.shortcuts import render

# Create your views here.
def student(request):
    context = {"hello" : "hello"}
    return render(request, "home.html", context)