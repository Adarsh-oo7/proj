from django.shortcuts import render
import math 

# Create your views here.
def index(request):
    if request.method == "POST":
        val1=int(request.POST['n1'])
        val2=int(request.POST['n2'])
        sp=val2/val1
        return render(request,'sum.html',{'nu':sp})
    return render(request,'sum.html')

def main(request):
    return render(request,'main.html')

def factoril(request):
    if request.method =="POST":
        va=int(request.POST['f'])
        r =1
        for i in range(1,va + 1):
            r *= i
        return render(request,'factoril.html',{'res':r})
        
        
    return render(request,'factoril.html')

def percentage(request):
    if request.method =="POST":
        val1=int(request.POST['p1'])
        val2=int(request.POST['p2'])
        pr=(val2*100)/val1
        return render(request,'percentage.html',{'pre':pr})

    
    return render(request,'percentage.html')