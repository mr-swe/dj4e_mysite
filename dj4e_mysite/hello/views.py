from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def cookie(request):
    resp = HttpResponse('cookie is here')
    resp.set_cookie('dj4e_cookie', '3493d96f', max_age=1000)
    return resp


def ssfun(request):
    num_count = request.session.get('num_count', 0) + 1
    request.session['num_count'] = num_count
    if num_count > 4:
        del (request.session['num_count'])
    return HttpResponse('view count=' + str(num_count))
