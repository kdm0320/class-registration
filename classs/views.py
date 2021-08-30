from django.shortcuts import render


def home(request):
    template_name = "class/viewSchedule.html"

    return render(request, template_name)
