from django.shortcuts import render
from .forms import StudentForms, StandardForms
from django.http import HttpResponseRedirect
from .models import Subject


# Create your views here.
def student_list(request):
    context = {"hello": "hello"}
    return render(request, "list.html", context)


def student_create(request):
    if request.method == "POST":
        form = StudentForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            context = {"form_error": form.errors, "form": StudentForms()}
            return render(request, "create.html", context)
    else:
        context = {"form": StudentForms()}
        return render(request, "create.html", context)


def standard_list(request):
    context = {"hello": "hello"}
    return render(request, "list.html", context)


def standard_create(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        form = StandardForms(request.POST)
        if form.is_valid():
            instance = form.save()
            Subject.objects.create(standard=instance, subject=subject)
            return HttpResponseRedirect("/standard_list/")
    else:
        context = {"form": StandardForms}
        return render(request, "subject.html", context)
