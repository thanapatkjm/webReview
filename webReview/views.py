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
    if(request.POST['Rname'] and request.POST['Rdes'] and request.POST['Radd'] and request.POST['Rphone'] != ""):
        add = Restaurant(name=request.POST['Rname'],description=request.POST['Rdes'],address=request.POST['Radd'],phone_num=request.POST['Rphone'],Category=request.POST['Rcate'])
        add.save()
        return HttpResponseRedirect(reverse('review:home'))
    else:
        return render(request,'add_rest.html',{'error':"You need to fill all Boxes Below"})

def res(request,rest_id):
    rest_descrip = get_object_or_404(Restaurant, pk=rest_id)
    rev =  Reviews.objects.filter(restau=rest_id)
    return render(request, 'rest.html',{'rest_descrip':rest_descrip,'rev':rev})

def add_review(request,rest_id):
    try:
        if(request.POST['Rname'] and request.POST['Rcomm'] and request.POST['Rating'] != ""):
            rest = Restaurant.objects.get(id=rest_id)
            add = Reviews(name=request.POST['Rname'],comment=request.POST['Rcomm'],rating=float(request.POST['Rating']),restau=rest)
            add.save()
            fil = Reviews.objects.filter(restau=rest_id)
            rate = 0
            for i in range (Reviews.objects.filter(restau=rest_id,).count()) :
                rate = rate + fil[i].rating
            rest.rating=rate/Reviews.objects.filter(restau=rest_id,).count()
            rest.save()
            return HttpResponseRedirect(reverse('review:res', args=(rest_id,)))
        else:
            rest_descrip = get_object_or_404(Restaurant, pk=rest_id)
            rev =  Reviews.objects.filter(restau=rest_id)
            return render(request, 'rest.html',{'rest_descrip':rest_descrip,'rev':rev,'error':"** You must fill all the data **"})
    except:
        rest_descrip = get_object_or_404(Restaurant, pk=rest_id)
        rev =  Reviews.objects.filter(restau=rest_id)
        return render(request, 'rest.html',{'rest_descrip':rest_descrip,'rev':rev,'error':"** You must Choose Rating **"})

def searching(request):
    if(request.POST['searchby']=='name'):
        list_rest = Restaurant.objects.filter(name__contains=request.POST['search'])
    else:
        if(request.POST['Rcate']==""):
            list_rest = Restaurant.objects.order_by("name")
        else:
            list_rest = Restaurant.objects.filter(Category=request.POST['Rcate'])
    return render(request,'home.html',{'list_rest':list_rest})
