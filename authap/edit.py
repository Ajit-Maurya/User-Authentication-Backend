from django.shortcuts import render

def edit(request):
    if request.method != 'POST':
        return render(request,'error.html',{'message' : 'Only post method are allowed'})