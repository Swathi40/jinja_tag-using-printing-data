from django.shortcuts import render

# Create your views here.

def jinja_print(request):
    d={'name':'Swathi','name2':'Sai Ganesh'}
    return render(request,'jinja_print.html',context=d)
