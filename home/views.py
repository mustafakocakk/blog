from django.shortcuts import render,HttpResponse



def home_view(request):
    if 1==1:
        context = {
            'isim':'Mustafa akocak',
        }
    else:
        context = {
            'isim':'Misafir pezo'
        }
    return render(request,'home.html',context)

