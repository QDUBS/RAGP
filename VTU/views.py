from django.shortcuts import render

# Create your views here.


def Home(request):

    context = {

    }
    
    return render(request, 'vtu/home.html', context)


def ContactUs(request):
    
    context = {

    }
    
    return render(request, 'vtu/contactUs.html', context)


def AboutUs(request):
    
    context = {

    }
    
    return render(request, 'vtu/aboutUs.html', context)

def BizInfo(request):
    
    context = {

    }
    
    return render(request, 'vtu/bizinfo.html', context)
