from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


from .models import Restaurant, Reviews

def home(request):
    list_rest= Restaurant.objects.order_by("name")
    return render(request,'home.html',{'list_rest':list_rest})

def add_rest(request):
    return render(request, 'add_rest.html')

def creating(request):
    add = Restaurant(name=request.POST['Rname'],description=request.POST['Rdes'],address=request.POST['Radd'],phone_num=request.POST['Rphone'],Category=request.POST['Rcate'])
    add.save()
    return HttpResponseRedirect(reverse('review:home'))

def res(request,rest_id):
    rest_descrip = get_object_or_404(Restaurant, pk=rest_id)
    # try:
    rev =  Reviews.objects.filter(restau=rest_id)
# except:
    # print('aaaaaaaaaaaaa')
    # return render(request, 'rest.html',{'rest_descrip':rest_descrip})
# else:
    return render(request, 'rest.html',{'rest_descrip':rest_descrip,'rev':rev})
    # return render(request, 'rest.html',{'rest_descrip':rest_descrip})

def add_review(request,rest_id):
    rest = Restaurant.objects.get(id=rest_id)
    add = Reviews(name=request.POST['Rname'],comment=request.POST['Rcomm'],rating=request.POST['Rating'],restau=rest)
    add.save()
    fil = Reviews.objects.filter(restau=rest_id)
    rate = 0
    for i in range (Reviews.objects.filter(restau=rest_id,).count()) :
        rate = rate + fil[i].rating
    rest.rating=rate/Reviews.objects.filter(restau=rest_id,).count()
    rest.save()
    return HttpResponseRedirect(reverse('review:res', args=(rest_id,)))
