from django.shortcuts import render

# Create your views here.
def mainwindow(request):
    context={}
    
    if request.method=="GET":
        return render(request,"mainwindow/templates/mainwindow.html",context="")
