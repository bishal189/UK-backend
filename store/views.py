from django.shortcuts import render

def custom_404_view(request, exception):
    print('hello wrold')
    return render(request, '404.html', status=404)
