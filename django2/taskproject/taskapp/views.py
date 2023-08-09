from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    # return HttpResponse("hello world")
    return render(request,'./maintemplate/home.html')
def handleday(request,day):
    if day == 1:
        x = 'monday'
    elif day==2:
        x ='tuesday'
    elif day ==3:
        x = 'wednesday'
    elif day == 4:
        x ='thrusday'
    elif day ==5:
        x = 'friday'
    elif day ==6:
        x = 'saturday'
    elif day ==7:
        x ='sunday'

    return render(request,'maintemplate/showday.html',{'day':x})
    # return render(request,"maintemplate/about.html",x)
    # # return render(request,'./maintemplate/home.html')
def contact(request):
    return render(request,"maintemplate/contact.html")
def about(request):
    return render(request,"maintemplate/about.html")
def daylist(request):
    # print(request.Get.get('name','defualt'))
    return render(request,"maintemplate/daylist.html")