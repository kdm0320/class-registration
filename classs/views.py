from django.shortcuts import render


def home(request):
    template_name = "class/viewSchedule.html"
    data = request.GET.get("subject")
    data1 = request.GET.get("college")

    print(data, data1)

    return render(request, template_name)
