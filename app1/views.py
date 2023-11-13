from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Movie,favorite
# Create your views here.
def display(request):
    data=Movie.objects.all()
    return render(request,'home.html',{'data':data})

def search(request):
        data=None
        search_data=None
        if request.method=="GET":
            search=request.GET.get('search')
            if search:
                search_data=Movie.objects.filter(title__icontains=search)
            else:
                data=Movie.objects.all()
        return render(request,'home.html',{'data': data,'movie': search_data})

def movie(request,id):
        if request.method =='GET':
            data1=Movie.objects.get(id=id)
            context = {
                'movie': data1
            }
            return render(request,'Movie.html',context)
        else:
            return redirect(display)


def add(request):
    if request.method == 'POST':
        movieid = request.POST["movieid"]
        currentmovie = Movie.objects.get(id=movieid)
        if favorite.objects.filter(title=currentmovie).exists():
            return HttpResponse("Already in your favorites")
        else:
            data = favorite.objects.create(title=currentmovie)
            data.save()
            return HttpResponse("Added to favorites")
    else:
        return render(request,'Movie.html')

def favorites(request):
    data=favorite.objects.all()
    return render(request,'favorites.html',{'data':data})

def back(request):
    return redirect(display)

def delete(request,id):
    if request.method=='POST':
        data = favorite.objects.get(id=id)
        data.delete()
        return redirect(favorites)
