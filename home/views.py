from django.shortcuts import render

def evenodd(request):
    c=''
    if request.method=="POST":
        n=eval(request.POST.get("num1"))
        if n%2==0:
            c="its a even number"
        else:
            c="its a odd number"    

    return render(request,'index.html',{'c':c})
# Create your views here.
