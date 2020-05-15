from django.shortcuts import render


def form(request):
    if request.method == 'GET':

        template = 'form.html'
        return render(request, template)